from dataclasses import dataclass
from environs import Env


@dataclass
class PaCredentials:
    pa_login: str        # Логин в PT
    pa_password: str      # Токен в PT


@dataclass
class Config:
    pa_creds: PaCredentials


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями pa_login и pa_password
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(PaCredentials(pa_login=env('PA_LOGIN'), pa_password=env('PA_PASSWORD')))

