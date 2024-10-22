from src.docker_api import check_container_health
from aiohttp import web
import docker
import logging

logging.basicConfig(level=logging.INFO)


def create_health_check_handler(docker_client: docker.DockerClient):
    async def health_check_handler(request):
        try:
            container_name = request.match_info.get(
                'container_name', "your_container_name")  # container_name from url
            logging.info(f"Checking health of container: {container_name}")

            health_status = await check_container_health(container_name, docker_client)
            logging.info(f"Health status: {health_status}")

            if isinstance(health_status, dict):
                return web.json_response(health_status)
            else:
                logging.error(
                    f"Invalid response from check_container_health: {health_status}")
                return web.json_response({"error": "Invalid response from check_container_health"}, status=500)

        except Exception as e:
            logging.error(f"Error in health_check_handler: {e}")
            return web.json_response({"error": str(e)}, status=500)

    return health_check_handler
