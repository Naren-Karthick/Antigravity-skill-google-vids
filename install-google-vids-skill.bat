@echo off
setlocal EnableExtensions
title Google Vids Skill Installer

echo.
echo ================================================
echo   Google Vids Video Creator - Antigravity
echo ================================================
echo.
echo This script installs or updates the skill globally
echo for Antigravity using the Skills CLI.
echo.

where npx >nul 2>nul
if errorlevel 1 (
    echo ERROR: npx was not found.
    echo Install Node.js (which includes npm/npx), then reopen Command Prompt.
    echo https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo Checking Node.js and npm...
node --version
call npx --version
if errorlevel 1 (
    echo ERROR: Node.js/npm is not working correctly.
    pause
    exit /b 1
)

echo.
echo Installing or updating Google Vids Video Creator...
echo.

call npx --yes skills add Naren-Karthick/Antigravity-skill-google-vids --skill google-vids-video-creator -g -a antigravity -y
if errorlevel 1 (
    echo.
    echo INSTALLATION FAILED.
    echo Check your internet connection and try again.
    echo You can also run this command manually:
    echo npx skills add Naren-Karthick/Antigravity-skill-google-vids --skill google-vids-video-creator -g -a antigravity -y
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo   Installation command completed successfully
echo ================================================
echo.
echo Restart Antigravity so it can discover the skill.
echo Then ask Antigravity to use: google-vids-video-creator
echo.
pause
endlocal
