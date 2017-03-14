CSG_HOST_ADMIN = 'http://gateway:4985/db/'
CELERY_ACCEPT_CONTENT = ['json', 'application/x-python-serialize']
BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_TASK_SERIALIZER = 'json'
CELERYD_USER = "celery"
CELERYD_GROUP = "celery"
