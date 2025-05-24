from celery import Celery
from time import sleep

# broker is going to be redis
app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def square(var):
    """Task to compute the square of a number."""
    x=5

    while x > 0:
        sleep(1)
        print(f"Processing {var}")
        x-=1

    
    return var * var
