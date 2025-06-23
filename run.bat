@REM @REM @echo off
@REM @REM rmdir /s /q reports\allure-results && docker-compose up -d &&
@REM @REM pytest -s -v -m "sanity" --reruns 2 --reruns-delay 2 --alluredir=reports\allure-results -n 2 testCases\ --browser edge && allure generate reports\allure-results -o reports\allure-html --clean && allure open reports\allure-html


@echo off

:: ====================================================
:: [Constants / Paths]
:: ====================================================
set ALLURE_RESULTS=reports\allure-results
set ALLURE_HTML=reports\allure-html
set PYTEST_HTML=reports\report.html

:: ====================================================
:: Step 1: Create virtual environment
:: ====================================================
echo Creating Virtual Environment...
python -m venv venv

:: ====================================================
:: Step 2: Activate the virtual environment
:: ====================================================
echo Activating Virtual Environment...
call venv\Scripts\activate.bat

:: ====================================================
:: Step 3: Set a custom temporary directory for pytest
:: ====================================================
echo Setting temporary directory for Pytest to avoid file permission errors...
set PYTEST_TMPDIR=%cd%\pytest-tmp
:: Create the directory if it doesn't exist
if not exist "%PYTEST_TMPDIR%" (
    mkdir "%PYTEST_TMPDIR%"
)

:: ====================================================
:: Step 4: Restart Docker containers (Selenium Grid, etc.)
:: ====================================================
echo Restarting Docker containers...
docker-compose down
docker-compose up -d

:: ====================================================
:: Step 5: Install required Python packages
:: ====================================================
echo Installing/updating required packages...
pip install -r requirements.txt

:: ====================================================
:: Step 6: Clean up previous test reports (Allure + HTML)
:: ====================================================
echo Cleaning previous test reports...
rmdir /s /q %ALLURE_RESULTS% || exit 0
rmdir /s /q %ALLURE_HTML% || exit 0
del %PYTEST_HTML% || exit 0

:: ====================================================
:: Step 7: Run Pytest tests with marker, reruns, parallel, HTML + Allure reporting
:: ====================================================
echo Running tests...
pytest -s -v ^
 --reruns=2 --reruns-delay=2 ^
 --alluredir=%ALLURE_RESULTS% ^
 --html=%PYTEST_HTML% --self-contained-html ^
 testCases/

:: ====================================================
:: Step 8: Shut down Docker containers
:: ====================================================
echo Shutting down Docker containers...
docker-compose down

:: ====================================================
:: Step 9: Generate and open Allure report
:: ====================================================
echo Generating and opening Allure report...
allure generate %ALLURE_RESULTS% -o %ALLURE_HTML% --clean && allure open %ALLURE_HTML%

