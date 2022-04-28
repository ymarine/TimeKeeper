@echo off

rem 代入①
set CURRENT_DIRECTORY1=%CD%
set CURRENT_DIRECTORY2=%~dp0

echo %%CD%%: %CURRENT_DIRECTORY1%
echo %%~dp0: %CURRENT_DIRECTORY2%

echo ==================
rem 代入②
for /f "usebackq" %%i in (`CD`) do (echo %%i)

cd %CURRENT_DIRECTORY1%

echo %CD%

pause >nul