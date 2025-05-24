# celery
- Celery is a task queue
- It offloads time, process intensive tasks to different instance, so that our main instance/app doesn't get blocked


# How to run?
- Up the redis instance using "docker-compose up"
- Run the celery instance using the command "celery -A app.celery worker --loglevel=info"
- Run the flask app using the command "python app.py"