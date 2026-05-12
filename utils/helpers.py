import allure


@allure.step('Проверка статуса ответа')
def assert_response_statuscode(response, expected_statuscode):
    assert response.status_code == expected_statuscode, \
        f'Ожидался статус {expected_statuscode}, но получен {response.status_code}'