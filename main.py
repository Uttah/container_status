from src.config import load_config
from src.health_api import create_health_check_handler
from aiohttp import web


async def init_app():
    config_data = load_config('config.yaml')

    docker_client = config_data.docker.create_client()

    app = web.Application()
    app.add_routes(
        [web.get('/health/{container_name}', create_health_check_handler(docker_client))])
    return app

if __name__ == "__main__":
    config = load_config('config.yaml')
    web.run_app(init_app(), port=config.app.port)
