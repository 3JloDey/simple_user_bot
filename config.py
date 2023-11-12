from dataclasses import dataclass

from environs import Env


@dataclass
class UserBot:
    api_id: int
    api_hash: str


@dataclass
class Config:
    user_bot: UserBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        user_bot=UserBot(
            api_id=env.int("API_ID"),
            api_hash=env.str("API_HASH"),
        ),
    )
