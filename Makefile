DOCKER_COMPOSE = docker-compose

.PHONY: help build up down ps

help:
	@echo "Available targets:"
	@echo "  - build: Build Docker images."
	@echo "  - up: Start Docker containers."
	@echo "  - down: Stop and remove Docker containers."
	@echo "  - ps: Show Docker container status."
	@echo "  - logs: Show Docker container logs."

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

ps:
	$(DOCKER_COMPOSE) ps

logs:
	$(DOCKER_COMPOSE) logs -f