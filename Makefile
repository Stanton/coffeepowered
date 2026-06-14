COMPOSE := docker compose

.PHONY: up down restart ps logs logs-tunnel logs-web

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down
	$(COMPOSE) up -d

ps:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f

logs-tunnel:
	$(COMPOSE) logs -f tunnel

logs-web:
	$(COMPOSE) logs -f web
