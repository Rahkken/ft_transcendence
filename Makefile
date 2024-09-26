all :
	sudo mkdir -p srcs/postgresql
	@ docker compose -f srcs/docker-compose.yml up --build

stop :
	@ docker compose -f srcs/docker-compose.yml down

prune : stop
	@ docker system prune --volumes -f

re : stop all

.PHONY: all stop prune re