.PHONY: info deploy run_local build_local clean

REPO_NAME := bot-checker
IMAGE_NAME := obsrv
VERSION := 0.3.0
CONTAINER_NAME := bot-checker

info:
	@echo "Makefile for tg-bot"
	@echo "Usage:"
	@echo "  make deploy - deploy bot to server"
	@echo "  make run_local - run bot locally"
	@echo "  make build_local - build bot locally"
	@echo "  make clean - remove all containers and images"

deploy:
	cd deploy && \
		./deploy.yaml \
			-l $(TARGET) \
			-e repo_name=$(REPO_NAME) \
			-e image_name=$(IMAGE_NAME) \
			-e tag=$(VERSION) \
			-e container_name=$(CONTAINER_NAME) \
			-e build_path="/opt" \
			-e folder_path="/opt/$(REPO_NAME)"

run_local:
	docker run -d --name $(CONTAINER_NAME) -p 8080:8080 $(IMAGE_NAME):$(VERSION)

clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME):$(VERSION) || true
