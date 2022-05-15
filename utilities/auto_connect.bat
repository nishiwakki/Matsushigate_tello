@echo off

rem connecting designated wifi automatically
rem This batchfile should be placed on utilities

set set_wifi=TELLO-ED4BD6
set get_wifi=null
set state=null

chcp 437
timeout /t 1 > nul
echo;

:loop
    for /f "usebackq tokens=3 delims= " %%i in (`netsh wlan show interface ^| find "State"`) do set state=%%i
    if not "%state%" == "connected" (
        echo CONNECTING NG
        netsh wlan connect name=%set_wifi% > nul
    ) else (
        for /f "usebackq tokens=3 delims= " %%i in (`netsh wlan show interface ^| find " SSID"`) do set get_wifi=%%i
        if not "%set_wifi%" == "%get_wifi%" (
            echo CONNECTING NG
            netsh wlan disconnect > nul
            timeout /t 3 > nul
            netsh wlan connect name=%set_wifi% > nul
        ) else (
            echo CONNECTING OK
        )
    )
    timeout /t 3 > nul
goto :loop