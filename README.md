# Задание 2: "API-тесты" курс ЯндексПрактикум | Diplom_2
Для тестирования был выбран сервис [Stellar Burgers](https://stellarburgers.education-services.ru/) | [API Stellar Burgers](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/Api-Stellar_Burgers.pdf)

В связи с грядущим релизом, был покрыт автотестами следующий набор тестов: 

[Создание пользователя](tests/test_create_user.py)
- Создание уникального пользователя
- Создание пользователя, который уже зарегистрирован
- Создание пользователя с незаполненными одним из обязательных полей

[Логин пользователя](tests/test_login_user.py)
- Логин под существующим пользователем
- Логин с неверным логином и паролем

[Создание заказа](tests/test_create_order.py)
- C авторизацией / Без авторизации
- С ингредиентами / Без ингредиентов 
- С неверным хешем ингредиентов

---
### Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
### Запустить все тесты из директории tests
```shell
pytest tests -v --alluredir=allure_results
```
### Посмотреть отчет в веб версии пройденного прогона
```shell
allure serve allure_results
```