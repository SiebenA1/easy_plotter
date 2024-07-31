@echo off
rem create email layout for ticket to IAV Easyplotter Service Desk
rem !!! NOT FOR USER - SYSTEM PART

title IAV Easyplotter Service Desk - Error Report Mail

set ADDRESS=support+cn-tv-a-toolchain-post-processing-easyplotter-17816-issue-@gitlab.iav.com
set LINE=//--------------------------------------
set NL=%%0D%%0A
set WS=%%20

color 47
echo.
echo %LINE%
echo // Send error report mail to IAV Easyplotter Service Desk
echo // %ADDRESS%
echo //
echo // !!! INTERNET CONNECTION REQUIRED !!!
echo // !!! DO NOT CHANGE THE SYNTAX AND FORMATTING !!!
echo %LINE%
echo.
color 07

start mailto:%ADDRESS%?subject=[easyplotter][ErrorReport]%WS%Topic%WS%(modify)%WS%-%WS%brief%WS%(modify)^
&body="#%WS%problem%WS%description:%NL%%NL%%NL%#%WS%software%WS%version:%NL%%NL%%NL%#%WS%priority:%NL%%NL%%NL%#%WS%contact:%NL%%NL%%NL%"^
"#%WS%input%WS%data%WS%(optionally):%NL%%NL%%NL%#%WS%comment%WS%(optionally):%NL%%NL%%NL%#%WS%proposed%WS%solution%WS%(optionally):%NL%%NL%%NL%"
pause
