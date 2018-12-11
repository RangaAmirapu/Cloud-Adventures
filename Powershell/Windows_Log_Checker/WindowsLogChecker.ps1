## Script for getting the windows event log within a given time frame 

## Defining parameters
param([string]$ComputerName  = 'localhost' , [datetime] $StartTimeStamp ,  [datetime] $EndTimeStamp )

$Logs  =  (Get-WinEvent -ListLog * -ComputerName $ComputerName | where {$_.RecordCount}).LogName

$FilterTable  = @{
'StartTime' = $StartTimeStamp
'EndTime' = $EndTimeStamp
'LogName' = $Logs

}

# Getting events
Get-WinEvent -ComputerName $ComputerName -FilterHashtable $FilterTable -ErrorAction 'SilentlyContinue'



