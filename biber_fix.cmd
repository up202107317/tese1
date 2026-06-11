@echo off
rem ============================================================
rem Wrapper do biber: o biber 2.21 falha quando o caminho do
rem projeto contem parenteses/espacos ("meec-distrib-v2024 (2)").
rem Este script copia o .bcf e o references.bib para %TEMP%,
rem corre o biber la, e copia o .bbl de volta.
rem Uso: biber_fix.cmd meec_thesis   (ou meec_thesis.bcf)
rem ============================================================
setlocal
set "NAME=%~n1"
set "SRCDIR=%~dp1"
if "%SRCDIR%"=="" set "SRCDIR=%CD%\"
set "TMPD=%TEMP%\thesisbib"
if not exist "%TMPD%" mkdir "%TMPD%"
copy /y "%SRCDIR%%NAME%.bcf" "%TMPD%\" >nul || exit /b 1
copy /y "%~dp0references.bib" "%TMPD%\" >nul
pushd "%TMPD%"
biber "%NAME%"
set "ERR=%ERRORLEVEL%"
popd
if exist "%TMPD%\%NAME%.bbl" copy /y "%TMPD%\%NAME%.bbl" "%SRCDIR%" >nul
if exist "%TMPD%\%NAME%.blg" copy /y "%TMPD%\%NAME%.blg" "%SRCDIR%" >nul
exit /b %ERR%
