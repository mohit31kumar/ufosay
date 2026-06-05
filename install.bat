@echo off
echo Installing ufosay...
pip install .

echo Creating wrapper scripts for mistype triggers...
set "TRIGGER_DIR=%USERPROFILE%\ufosay-triggers"
if not exist "%TRIGGER_DIR%" mkdir "%TRIGGER_DIR%"

for %%t in (ks cl xl lw lz) do (
    echo @echo off > "%TRIGGER_DIR%\%%t.bat"
    echo python -m ufosay "Did you mean ls?" >> "%TRIGGER_DIR%\%%t.bat"
)

echo.
echo ufosay installed!
echo Add %%USERPROFILE%%\ufosay-triggers to your PATH to enable mistype triggers.
echo.
echo Try: ufosay "Hello from space!"
