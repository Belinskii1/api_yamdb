from logging import error


class APIErrors(Exception):
    """базовый класс для всех исключений."""
    pass


class UserValueException(APIErrors):
    """Имя пользователя не уникально или me"""
    pass
 


class MailValueException(APIErrors):
    """Адрес почты не уникален"""
    pass
