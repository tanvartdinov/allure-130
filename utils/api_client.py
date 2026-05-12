import allure
import requests


class APIClient:
    base_url = 'https://fe.rc.smotreshka.tv'

    @allure.step('Отправка запроса авторизации для старых устройств')
    def login(self, login, password):
        data = f'email={login}&password={password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(f'{self.base_url}/login',
                                 headers=headers,
                                 data=data)
        allure.attach('https://fe.rc.smotreshka.tv/login', name='URL', attachment_type=allure.attachment_type.TEXT)
        allure.attach(data, name='Payload', attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response json', attachment_type=allure.attachment_type.JSON)

        return response

    @allure.step('Отправка запроса авторизации для новых устройств')
    def login_v2(self, login, password):
        data = f'email={login}&password={password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(f'{self.base_url}/v2/login',
                                 headers=headers,
                                 data=data)
        allure.attach('https://fe.rc.smotreshka.tv/v2/login', name='URL', attachment_type=allure.attachment_type.TEXT)
        allure.attach(data, name='Payload', attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response json', attachment_type=allure.attachment_type.JSON)

        return response
