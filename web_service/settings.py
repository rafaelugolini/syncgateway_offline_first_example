CSG_HOST_ADMIN = 'http://gateway:4985/db/'
CELERY_ACCEPT_CONTENT = ['json', 'application/x-python-serialize']
BROKER_URL = 'redis://redis:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERYD_USER = "celery"
CELERYD_GROUP = "celery"
