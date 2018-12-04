##Script for interrogating text log files

##Defining Parameters

## Setting default Computername as localhost and default log file extension as log

param([string] $ComputerName = 'localhost', [datetime] $StartTimeStamp, [datetime] $EndTimeSTamp, [string] $LogFileExtenssion  = 'log')

## defining the drives tolook for log files , Getting the locally attached drives in case (DriveType = 3) of localmachine else enumerating through the network drives.

    if($ComputerName -eq 'localhost' )
    {
            $location =  (Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType = '3'").DeviceID
    
    }
    else
    {
          ##Enumerating through all the available shares

          ## Getting the share names such as C$, D$ etc.

          $shares = Get-CimInstance -ComputerName $ComputerName -Class Win32_Share | where{$_.path -match '^\w{1}:\\$'}

          [System.Collection.ArrayList] $location  = @()

          foreach($share in $shares)
          {
            $share =  "\\$ComputerName\$($share.Name)"

            if(!(Test-Path $share))
            {
                    Write-Warning "Unable to access the '$share' share on '$ComputerName'"
            }
            else{
                   $location.Add($share) | Out-Null
            }

          }

     }

## Building a hash table to perform filter

$GciParams  = @{
    Path = $location
    Filter  =  "*.$LogFileExtenssion"
    Recurse  = $true
    Force  = $true
    ErrorAction  = 'SilentlyContinue'
    File  = $true
}

## Filter Condition to perform on the table

$whereFilter  =  {($_.LastWriteTime -ge $StartTimeStamp) -and ($_.LasWriteTime -le $EndTimeSTamp) -and ($_.Length -ne 0)}

## Find the ones matching the filter condition

Get-ChildItem @GciParams | Where-Object $whereFilter