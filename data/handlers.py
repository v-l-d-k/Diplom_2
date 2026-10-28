class Urls:
    MAIN_URL = 'https://qa-stellarburgers.education-services.ru'


class Handlers:
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {"Content-Type": "application/json"}