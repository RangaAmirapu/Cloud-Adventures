##Script for checking whether a program exists in uninstall folder in local or remote machine

## This scripts checks if Microsoft Visual C++ (32 bit and 64 bit) Redist is installed 

clear

## Defining an array of machines to check for a particular program
 
$arrMachineNames  = @("301","302","303","304")

##Looping through all machines   
   foreach($machine in $arrMachineNames)
   {
   
   $computername= $machine
 
 ##Setting variable with the program to be checked.
 
   $RedistVersion  = '*Microsoft Visual C++ 2017*';
 
   $array = @()
   
##Defining Registry key paths for 32 and 64 bit in HKLM   
  
  $UninstallKey="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"  
 
  $UninstallKey32 ="SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall"  
 
 ##Going into registry folder
 
  $reg=[microsoft.win32.registrykey]::OpenRemoteBaseKey('LocalMachine',$computername)  
 
  $regkey=$reg.OpenSubKey($UninstallKey)  
  $subkeys=$regkey.GetSubKeyNames()  
 
 
  $regkey32=$reg.OpenSubKey($UninstallKey32)  
  $subkeys32=$regkey32.GetSubKeyNames()  
 
 ## Looping through all subkeys
 
    foreach($key in $subkeys){
 
        $thisKey=$UninstallKey+"\\"+$key 
 
        $thisSubKey=$reg.OpenSubKey($thisKey) 
 
         $obj = New-Object PSObject
 
            $obj | Add-Member -MemberType NoteProperty -Name "ComputerName" -Value $computername
 
          $obj | Add-Member -MemberType NoteProperty -Name "DisplayName" -Value $($thisSubKey.GetValue("DisplayName"))
 
 
             $array += $obj
        }
 
 
 
    foreach($key32 in $subkeys32){
 
        $thisKey32=$UninstallKey32+"\\"+$key32 
 
        $thisSubKey32=$reg.OpenSubKey($thisKey32) 
 
         $obj = New-Object PSObject
 
          $obj | Add-Member -MemberType NoteProperty -Name "ComputerName" -Value $computername
 
          $obj | Add-Member -MemberType NoteProperty -Name "DisplayName" -Value $($thisSubKey32.GetValue("DisplayName"))
 
 
             $array += $obj
        }
 
 
##Checking if the required program is found and printing message
 
       $Has2017 =  $array | Where-Object { $_.DisplayName -like $RedistVersion} | select ComputerName, DisplayName | ft -auto
 
       if($Has2017)
       { 
         $Has2017
       }
 
       else
       {
          Write-Host $computername - "Not found " - $RedistVersion
       }
 
}
 
 
