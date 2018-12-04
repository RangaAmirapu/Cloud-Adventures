#Script for getting the logged in user.

#Setting the list of machines to check in a txt file 

cls

#Reading the list of machines file and looping through them
#Printing the computer name and login username 
Get-Content -Path c:\ListOfMachines.txt | % {
  Get-WmiObject -ComputerName $_ -Namespace root\cimv2 -Class Win32_ComputerSystem -erroraction silentlycontinue | % {
    "$($_.Name): $($_.username)"
  }
  Write-Output "****************************************************************** `r`n";
 
}
