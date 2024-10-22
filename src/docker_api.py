import docker
import logging

logging.basicConfig(level=logging.INFO)


async def check_container_health(container_name: str,
                                 docker_client: docker.DockerClient):
    try:
        container = docker_client.containers.get(container_name)
        logging.info(f"Container {container_name} status: {container.status}")

        if container.status == 'running':
            return {"container": container_name, "status": "running"}
        else:
            return {"container": container_name, "status": container.status}

    except docker.errors.NotFound:
        logging.error(f"Container {container_name} not found")
        return {"container": container_name, "status": "not found"}
    except Exception as e:
        logging.error(f"Error in check_container_health: {e}")
        return {"container": container_name, "status": f"error: {e}"}
