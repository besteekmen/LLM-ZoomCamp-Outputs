run:
	uv run python assistant.py "How do I complete the course?"

chat:
	uv run streamlit run app.py

network:
	docker network create monitoring

# if codespase is turned off, use docker rm -f course-assistant-pg
# then call below as docker run -it...
postgres: network
	docker run -it \
		--name course-assistant-pg \
		--network monitoring \
		-e POSTGRES_USER=user \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_DB=course_assistant \
		-p 5432:5432 \
		-v pgdata:/var/lib/postgresql/data \
		postgres:17

# use detached mode (-d rather than -it) to hide logs
# if codespase is turned off, use docker start grafana
grafana:
	docker run -it \
		--name grafana \
		--network monitoring \
		-p 3000:3000 \
		-v grafana_data:/var/lib/grafana \
		grafana/grafana

getlist:
	docker exec -it course-assistant-pg psql -U user -d course_assistant \
    -c "SELECT id, question, response_time, cost FROM conversations;"

getlistdocker:
	docker compose exec postgres \
		psql -U user -d course_assistant \
		-c "SELECT id, question, response_time, cost FROM conversations;"

query:
	uv run python db_query.py

dashboard:
	uv run streamlit run dashboard.py --server.port 8502

judge:
	uv run python judge.py

fakedata:
	uv run python generate_data.py

fakedatadocker:
	docker compose exec streamlit python generate_data.py