mode con: cols=16 lines=1
@echo off
chcp 65001
title XTVZ_ by Félx
mkdir "Logs/TNT"
mkdir "Logs/Twitch"
:MENU
title Menu
mode con: cols=32 lines=9
cls
call :LOGO
echo ' 001 ' France                 '
echo '-----'------------------------'
echo '  P  ' Paramètres             '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
cls
if %input%==P goto PARAMETRES
if %input%==001 goto FRANCE
goto MENU
exit

:PARAMETRES
title Paramètres
mode con: cols=32 lines=9
cls
call :LOGO
echo ' TF1 ' Compte TF1  (Mail/MDP) '
echo '-----'------------------------'
echo '  M  ' Menu                   '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
cls
if %input%==M goto MENU
if %input%==m goto MENU
if %input%==TF1 goto COMPTE_TF1
goto PARAMETRES
exit

:COMPTE_TF1
title Compte TF1
mode con: cols=75 lines=20
cls
set /p email="E-Mail : "
set /p password="Mot De Passe : "
cd Data
echo email=%email%> compte_tf1.txt
echo password=%password%>> compte_tf1.txt
cd..
goto PARAMETRES
exit

:FRANCE
title France
mode con: cols=32 lines=10
cls
call :LOGO
echo ' 001 ' TNT                    '
echo ' 002 ' Twitch                 '
echo '-----'------------------------'
echo '  M  ' Menu                   '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
cls
if %input%==M goto MENU
if %input%==m goto MENU
if %input%==001 goto TNT
if %input%==002 goto TWITCH
goto FRANCE
exit

:TNT
title France TNT (1^/2)
mode con: cols=32 lines=30
cls
call :LOGO
echo ' 001 ' TF1                    '
echo ' 002 ' France 2               '
echo ' 003 ' France 3               '
echo ' 004 ' Canal+                 '
echo ' 005 ' France 5               '
echo ' 006 ' M6                     '
echo ' 007 ' Arte                   '
echo ' 008 ' C8                     '
echo ' 009 ' W9                     '
echo ' 010 ' TMC                    '
echo ' 011 ' TFX                    '
echo ' 012 ' NRJ 12                 '
echo ' 013 ' LCP                    '
echo ' 014 ' France 4               '
echo ' 015 ' BFM TV                 '
echo ' 016 ' CNews                  '
echo ' 017 ' CStar                  '
echo ' 018 ' Gulli                  '
echo ' 019 ' TF1 Séries Films       '
echo ' 020 ' L'Équipe TV            '
echo '-----'------------------------'
echo '   b ' Page Suivante    (1/2) '
echo '-----'------------------------'
echo '  M  ' Menu                   '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
for /f "tokens=1,2 delims==" %%A in (Data\compte_tf1.txt) do (
    if "%%A"=="email" set email=%%B
    if "%%A"=="password" set password=%%B
)
cls
if %input%==b goto TNT_2
if %input%==M goto MENU
if %input%==m goto MENU
if %input%==001 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/TF1 -o %temp%/TF1.bat && call %temp%/TF1.bat
if %input%==002 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/France2 -o %temp%/France2.bat && call %temp%/France2.bat
if %input%==003 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/France3 -o %temp%/France3.bat && call %temp%/France3.bat
if %input%==004 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/CanalPlus -o %temp%/CanalPlus.bat && call %temp%/CanalPlus.bat
if %input%==005 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/France5 -o %temp%/France5.bat && call %temp%/France5.bat
if %input%==006 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/M6 -o %temp%/M6.bat && call %temp%/M6.bat
if %input%==007 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/Arte -o %temp%/Arte.bat && call %temp%/Arte.bat
if %input%==008 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/C8 -o %temp%/C8.bat && call %temp%/C8.bat
if %input%==009 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/W9 -o %temp%/W9.bat && call %temp%/W9.bat
if %input%==010 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/TMC -o %temp%/TMC.bat && call %temp%/TMC.bat
if %input%==011 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/TFX -o %temp%/TFX.bat && call %temp%/TFX.bat
if %input%==012 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/NRJ12 -o %temp%/NRJ12.bat && call %temp%/NRJ12.bat
if %input%==013 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/LCP -o %temp%/LCP.bat && call %temp%/LCP.bat
if %input%==014 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/France4 -o %temp%/France4.bat && call %temp%/France4.bat
if %input%==015 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/BFMTV -o %temp%/BFMTV.bat && call %temp%/BFMTV.bat
if %input%==016 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/CNews -o %temp%/CNews.bat && call %temp%/CNews.bat
if %input%==017 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/CStar -o %temp%/CStar.bat && call %temp%/CStar.bat
if %input%==018 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/Gulli -o %temp%/Gulli.bat && call %temp%/Gulli.bat
if %input%==019 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/TF1SF -o %temp%/TF1SF.bat && call %temp%/TF1SF.bat
if %input%==020 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/TNT/France2 -o %temp%/LEQUIPETV.bat && call %temp%/LEQUIPETV.bat
goto TNT
exit

:TNT_2
title France TNT (2^/2)
mode con: cols=32 lines=30
cls
call :LOGO
echo ' 021 '                        '
echo ' 022 '                        '
echo ' 023 '                        '
echo ' 024 '                        '
echo ' 025 '                        '
echo ' 026 '                        '
echo ' 027 '                        '
echo ' 028 '                        '
echo ' 029 '                        '
echo ' 030 '                        '
echo ' 031 '                        '
echo ' 032 '                        '
echo ' 033 '                        '
echo ' 034 '                        '
echo ' 035 '                        '
echo ' 036 '                        '
echo ' 037 '                        '
echo ' 038 '                        '
echo ' 039 '                        '
echo ' 040 '                        '
echo '-----'------------------------'
echo ' d   ' Page Précédente  (2/2) '
echo '-----'------------------------'
echo '  M  ' Menu                   '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
cls
if %input%==d goto TNT
if %input%==M goto MENU
if %input%==m goto MENU
if %input%==021 
if %input%==022 
if %input%==023 
if %input%==024 
if %input%==025 
if %input%==026 
if %input%==027 
if %input%==028 
if %input%==029 
if %input%==030 
if %input%==031 
if %input%==032 
if %input%==033 
if %input%==034 
if %input%==035 
if %input%==036 
if %input%==037 
if %input%==038 
if %input%==039 
if %input%==040 
goto TNT_2
exit

:TWITCH
title France Twitch (1^/1)
mode con: cols=32 lines=12
cls
call :LOGO
echo ' 001 ' Les Simpsons           '
echo ' 002 ' Ma Famille D'abord     '
echo ' 003 ' Malcolm                '
echo ' 004 ' South Park             '
echo '-----'------------------------'
echo '  M  ' Menu                   '
echo '-----'------------------------'
set /p input=# 
mode con: cols=16 lines=1
cls
if %input%==M goto MENU
if %input%==m goto MENU
if %input%==001 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/Twitch/LesSimpsons -o %temp%/LesSimpsons.bat && call %temp%/LesSimpsons.bat
if %input%==002 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/Twitch/MaFamilleDabord -o %temp%/MaFamilleDabord.bat && call %temp%/MaFamilleDabord.bat
if %input%==003 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/Twitch/Malcolm -o %temp%/Malcolm.bat && call %temp%/Malcolm.bat
if %input%==004 curl -s https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Logiciel/Twitch/SouthPark -o %temp%/SouthPark.bat && call %temp%/SouthPark.bat
goto TWITCH
exit

:LOGO
echo  ------------------------------
echo '            XTVZ_             '
echo '           by Félx            '
echo '------------------------------'