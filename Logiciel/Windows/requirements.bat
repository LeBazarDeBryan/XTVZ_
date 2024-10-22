mode con: cols=16 lines=1
@echo off
if "%~s0"=="%~s1" ( cd %~sp1 & shift ) else (
  echo CreateObject^("Shell.Application"^).ShellExecute "%~s0","%~0 %*","","runas",1 >"%tmp%%~n0.vbs" & "%tmp%%~n0.vbs" & del /q "%tmp%%~n0.vbs" & goto :eof
)
chcp 65001
title XTVZ_ by Félx
:MENU
mode con: cols=36 lines=8
cls
call :LOGO
echo '     Install Streamlink/VLC?      '
echo '              (Y^/N)               '
echo '----------------------------------'
set /p input=# 
if %input%==Y goto INSTALL
if %input%==y goto INSTALL
if %input%==N exit
if %input%==n exit
goto MENU
exit

:INSTALL
mode con: cols=120 lines=30
cls
call :LOGO
winget install --id=Streamlink.Streamlink -e
winget install --id=VideoLAN.VLC -e
echo.
pause
exit

:LOGO
echo  ----------------------------------
echo '              XTVZ_               '
echo '             by Félx              '
echo '----------------------------------'