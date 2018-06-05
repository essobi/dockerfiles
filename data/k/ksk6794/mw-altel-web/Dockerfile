FROM python:3.6-alpine  
  
# Required system libraries  
RUN apk add --no-cache bash gcc libc-dev unixodbc-dev python3-dev postgresql-
dev py-psycopg2  
  
# Project  
ADD ./src /www  
ADD ./requirements.txt /home  
ADD ./docker/web/docker-command.sh /home/  
  
# Migrations  
ADD ./alembic /migrations/alembic  
ADD ./docker/web/alembic.ini /migrations  
  
WORKDIR /www  
  
# Project requirements installation  
RUN pip install -r /home/requirements.txt  
  
# Patch the module  
ADD ./docker/web/builders.py.patch /usr/local/lib/python3.6/site-
packages/aiohttp_swagger/helpers/builders.py  

