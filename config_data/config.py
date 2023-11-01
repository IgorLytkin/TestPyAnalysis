from dataclasses import dataclass

from environs import Env


@dataclass
class PaCredentials:
    pa_login : str        # Логин в PT
    pa_password: str      # Токен в PT

@dataclass
class Config:
    pa_creds: PaCredentials


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
         pa_login = env('pa_login'),
         pa_password = env('pa_password')
    )
