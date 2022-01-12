setlocal

    @echo off
    rem docker run -it --rm litmos-etl:latest /bin/ash
    rem docker build --rm -f "Dockerfile" -t etl:latest .

    SET API_URL_PREFIX=/wombat
    SET TAG=itretl:latest
    SET /p ODBC_UID=Enter the odbc username for a linux-based client:
    SET /p ODBC_PWD=Enter the odbc password for a linux-based client:
    if "%~1"=="" (
        docker run -it -p 8888:8888 -p 8080:8080 -e ODBC_PWD=%ODBC_PWD% -e ODBC_UID=%ODBC_UID% -e API_URL_PREFIX=%API_URL_PREFIX% "%TAG%"
    ) else (
        docker run -it -p 8888:8888 -p 8080:8080 -e ODBC_PWD=%ODBC_PWD% -e ODBC_UID=%ODBC_UID% -e API_URL_PREFIX=%API_URL_PREFIX% "%TAG%"  "%~1"
    )

endlocal