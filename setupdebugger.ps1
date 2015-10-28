Param(
	[string]$ShowErrors
)

if ($ShowErrors -eq "yes") {
	$Debugger = Get-Process msvsmon 
}
else {
	$Debugger = Get-Process msvsmon -ErrorAction SilentlyContinue
}

if ($Debugger -ne $null) {
	Write-Host "Instance of msvsmon.exe found" -foregroundcolor blue
	
	if ($ShowErrors -eq "yes") {
		$Success = Stop-Process -processname msvsmon
	}
	else {
		$Success = Stop-Process -processname msvsmon -ErrorAction SilentlyContinue
	}

	if ($Success -eq 0) {
		Write-Host "Killed msvsmon.exe" -foregroundcolor blue
	}
	else {
		Write-Host "Could not kill msvsmon.exe" -foregroundcolor gray -backgroundcolor red
		Write-Host "Remaining instances of msvsmon.exe:"
		tasklist /fi "imagename eq msvsmon.exe"
		Exit
	}
}
else {
	Write-Host "No instances of msvsmon.exe found" -foregroundcolor blue
}

if ($ShowErrors -eq "yes") {
	$Ran = schtasks /run /tn StartMsvsmon
}
else {
	$Ran = schtasks /run /tn StartMsvsmon 2> $null
}

if ($Ran -eq 0) {
	Write-Host "Restarted remote debugger" -foregroundcolor blue -backgroundcolor green
	Write-Host "Existing instances of msvsmon.exe:" -foregroundcolor blue
	tasklist /fi "imagename -eq msvsmon.exe"
}
else {
	Write-Host "Could not start the Visual Studio remote debugger" -foregroundcolor gray -backgroundcolor red
	Exit
}