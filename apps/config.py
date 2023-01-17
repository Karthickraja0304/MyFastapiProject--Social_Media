from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    web_token_secret_key:str
    web_token_algorithm:str
    web_token_expiration_time:str

    class Config:
        env_file = ".env"

    


settings = Settings()

