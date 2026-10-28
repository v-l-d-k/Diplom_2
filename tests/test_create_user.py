import pytest
import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Создание нового пользователя')
    @allure.title('Создание нового пользователя')
    def test_create_new_user_success(self, cleanup_user):
        user_data = User.create_data_user()
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)    
        assert response.status_code == 200 and response.json()["success"] is True
        cleanup_user.append(response.json()["accessToken"])

    @allure.description('При создании дублирующего пользователя срабатывает allert ')
    @allure.title('Создание пользователя который уже есть в системе')
    def test_create_double_user_error(self, cleanup_user):
        user_data = User.create_data_user()
        reg_response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert reg_response.status_code == 200
        cleanup_user.append(reg_response.json()["accessToken"])
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('При создании пользователя с некорректыми данными срабатывает allert')
    @allure.title('Создание пользователя с некорректными данными/ с незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text