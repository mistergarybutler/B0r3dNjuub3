[CmdletBinding()]
Param(
	[Parameter(Mandatory=$False,Position=1)]
		[string]$Search="*.txt*",
	[Parameter(Mandatory=$False,Position=2)]
		[int32]$Count="10"
	)

Get-ChildItem -Filter $Search -Path C:\ -recurse -force -ErrorAction:SilentlyContinue | Select-Object -first $Count