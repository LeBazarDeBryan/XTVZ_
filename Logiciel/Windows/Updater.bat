@echo off
mode con: cols=16 lines=1
chcp 65001
title XTVZ_ Updater by Félix
setlocal
set LOCAL_VERSION_FILE=Data\version.txt
set VERSION_URL=https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/Windows/Data/version.txt
set TEMP_VERSION_FILE=%TEMP%\latest_version.txt
mode con: cols=75 lines=20
cls
if exist %LOCAL_VERSION_FILE% (
    set /p LOCAL_VERSION=<%LOCAL_VERSION_FILE%
) else (
    echo Local version file not found! Aborting update process.
    exit
)
curl -s %VERSION_URL% > %TEMP_VERSION_FILE%
if not exist %TEMP_VERSION_FILE% (
    echo Failed to retrieve the latest version information. Check your internet connection.
    exit
)
set /p LATEST_VERSION=<%TEMP_VERSION_FILE%
if "%LOCAL_VERSION%"=="%LATEST_VERSION%" (
    echo You are using the latest version: %LOCAL_VERSION%.
) else (
    echo A new version is available: %LATEST_VERSION%
    echo Updating...
    rmdir /s /q Data
    rmdir /s /q Logs
    del /f /q requirements.bat
    del /f /q XTVZ_.bat
    mkdir Data
    curl -s %VERSION_URL% -o Data\version.txt
    curl -s https://github.com/LeBazarDeBryan/XTVZ_/releases/download/%LATEST_VERSION%/Windows.zip -o tmp.zip
    if exist tmp.zip (
        echo Extracting files...
        powershell -command "Expand-Archive -Path 'tmp.zip' -DestinationPath './' -Force"
        del tmp.zip
        echo Update completed.
    ) else (
        echo Failed to download the update. Please check your internet connection or the update URL.
    )
)
del %TEMP_VERSION_FILE%
endlocal
pause
exit