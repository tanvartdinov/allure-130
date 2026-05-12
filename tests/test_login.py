# pytest -v --tb=short
# pip install pytest-html
# pytest -v --tb=short --html=report.html
# pip install allure-pytest
# pip install allure-python-commons

# Создание отчета allure
# pytest --alluredir=allure-results
# Запуск сервера с отчетами
# allure serve allure-results/
# python3 -m pytest --alluredir=allure-results

import requests
import allure

from utils.api_client import APIClient
from utils.helpers import assert_response_statuscode


@allure.epic('Авторизация')
@allure.feature('Авторизация по паролю')
class TestLoginPassword:
    @allure.title('Успешная авторизация для старых устройств')
    @allure.description("""Здесь может быть описание""")
    def test_login_success(self, valid_credentials):
        client = APIClient()
        login, password = valid_credentials
        response = client.login(login, password)
        assert_response_statuscode(response, 200)


    @allure.title('Неуспешная авторизация для старых устройств')
    @allure.description("""Здесь может быть описание""")
    def test_login_failed(self, invalid_credentials):
        client = APIClient()
        login, password = invalid_credentials
        response = client.login(login, password)
        assert_response_statuscode(response, 403)


    @allure.title('Успешная авторизация для новых устройств')
    @allure.description("""Здесь может быть описание""")
    def test_login_v2_success(self, valid_credentials):
        client = APIClient()
        login, password = valid_credentials
        response = client.login_v2(login, password)
        assert_response_statuscode(response, 200)


    @allure.title('Неуспешная авторизация для новых устройств')
    @allure.description("""Здесь может быть описание""")
    def test_login_v2_failed(self, invalid_credentials):
        client = APIClient()
        login, password = invalid_credentials
        response = client.login_v2(login, password)
        assert_response_statuscode(response, 403)
