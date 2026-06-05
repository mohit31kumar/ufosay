Write-Host "Installing ufosay..."
pip install .

Write-Host "Adding ufosay aliases to PowerShell profile..."
$content = @'

# ufosay - mistype triggers for ls
function ks { ufosay "Did you mean ls?" }
function cl { ufosay "Did you mean ls?" }
function xl { ufosay "Did you mean ls?" }
function lw { ufosay "Did you mean ls?" }
function lz { ufosay "Did you mean ls?" }
'@

if (Test-Path $PROFILE) {
    $existing = Get-Content $PROFILE -Raw
    if ($existing -match "ufosay") {
        Write-Host "ufosay aliases already present in profile"
    } else {
        Add-Content -Path $PROFILE -Value $content
        Write-Host "Added ufosay aliases to $PROFILE"
    }
} else {
    New-Item -Path $PROFILE -ItemType File -Force
    Add-Content -Path $PROFILE -Value $content
    Write-Host "Created profile and added ufosay aliases to $PROFILE"
}

Write-Host ""
Write-Host "ufosay installed! Restart PowerShell or run:"
Write-Host "  . `$PROFILE"
Write-Host ""
Write-Host "Try: ufosay 'Hello from space!'"
