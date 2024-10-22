from pydantic import BaseModel
from typing import Optional
import yaml
import docker


class AppConfig(BaseModel):
    port: int


class DockerClientConfig(BaseModel):
    base_url: str

    def create_client(self):
        return docker.DockerClient(base_url=self.base_url)


class Config(BaseModel):
    app: AppConfig
    docker: DockerClientConfig


def load_config(config_file: Optional[str] = 'config.yaml') -> Config:
    with open(config_file, 'r') as file:
        config_data = yaml.safe_load(file)
    return Config(**config_data)
