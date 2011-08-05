import os
# List of modules to import when celery starts.
CELERY_IMPORTS = []

## Result store settings.
## This is important, allows web2py to access the celery db directly
CELERY_RESULT_BACKEND = "database"
## This allows web2py to find the celery db
CELERY_RESULT_DBURI = "sqlite:///%s/mydatabase.db" % os.path.dirname(__file__)

## Broker settings.
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

## Worker settings
## If you're doing mostly I/O you can have more processes,
## but if mostly spending CPU, try to keep it close to the
## number of CPUs on your machine. If not set, the number of CPUs/cores
## available will be used.
CELERYD_CONCURRENCY = 10
# CELERYD_LOG_FILE = "celeryd.log"
# CELERYD_LOG_LEVEL = "INFO"

