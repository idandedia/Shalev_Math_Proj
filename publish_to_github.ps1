param(
    [Parameter(Mandatory = $true)]
    [string]$GithubUser,

    [Parameter(Mandatory = $true)]
    [string]$RepoName
)

$ErrorActionPreference = 'Stop'

Write-Host "==> מעבר לתיקיית הפרויקט" -ForegroundColor Cyan
Set-Location -Path $PSScriptRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git לא מותקן או לא זמין ב-PATH"
}

Write-Host "==> בדיקת אתחול git" -ForegroundColor Cyan
if (-not (Test-Path ".git")) {
    git init
}

Write-Host "==> הגדרת branch ראשי" -ForegroundColor Cyan
git branch -M main

Write-Host "==> הוספת קבצים" -ForegroundColor Cyan
git add .

Write-Host "==> יצירת commit" -ForegroundColor Cyan
$hasChanges = git diff --cached --name-only
if ($hasChanges) {
    git commit -m "Initial commit - math app"
} else {
    Write-Host "אין שינויים חדשים ל-commit" -ForegroundColor Yellow
}

$remoteUrl = "https://github.com/$GithubUser/$RepoName.git"

Write-Host "==> הגדרת origin" -ForegroundColor Cyan
$remoteExists = git remote
if ($remoteExists -contains "origin") {
    git remote set-url origin $remoteUrl
} else {
    git remote add origin $remoteUrl
}

Write-Host "==> דחיפה ל-GitHub" -ForegroundColor Cyan
git push -u origin main

Write-Host "==> הושלם בהצלחה" -ForegroundColor Green
Write-Host "Repo URL: https://github.com/$GithubUser/$RepoName" -ForegroundColor Green
Write-Host "עכשיו פתח: https://share.streamlit.io כדי לפרוס את app.py" -ForegroundColor Green
