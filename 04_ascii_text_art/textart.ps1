cd $PSScriptRoot
$letters = Get-Content -Path .\font.json | ConvertFrom-Json

$sentence = Read-Host -Prompt "Please enter a sentence. Only letters are regarded."
$sentence = $sentence.ToLower()
$sentence = $sentence -replace '[^a-z]',''
$sentence = $sentence.ToCharArray()

foreach ($character in $sentence){
    write-host $letters.$character.lower -NoNewline
}

Write-Host
foreach ($character in $sentence){
    Write-Host $letters.$character.upper -NoNewline
}