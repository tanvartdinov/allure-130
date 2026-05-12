import allure
import pytest

@pytest.fixture
@allure.step('Подготовка валидных тестовых данных')
def valid_credentials():
    return 'testatr0207251', '123456'

@pytest.fixture
@allure.step('Подготовка невалидных тестовых данных')
def invalid_credentials():
    return 'testatr0207251', '123'