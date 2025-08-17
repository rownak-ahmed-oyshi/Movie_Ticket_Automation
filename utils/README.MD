run:
pytest --browser=firefox --alluredir=allure_test_report
allure serve allure_test_report

allure generate .\allure_test_report\ --clean -o .\allure_html_report\