from celery import Celery

def make_celery(app):
    """Create a Celery instance with the Flask app context."""
    celery = Celery(
        app.name, # TODO: What are the parameters?
        broker = app.config['CELERY_BROKER_URL'],
        backend = app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery