FROM python:3.6-slim-jessie  
  
ENV PYTHONUNBUFFERED 1  
ENV PG_MAJOR 9.6  
RUN apt-get update && apt-get install -y --no-install-recommends gnupg dirmngr  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
RUN set -ex; \  
# pub 4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]  
# Key fingerprint = B97B 0AFC AA1A 47F0 44F2 44A0 7FCC 7D46 ACCC 4CF8  
# uid PostgreSQL Debian Repository  
key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \  
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys $key  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# building  
build-essential python3-dev git-core \  
# psycopg2 dependencies  
libpq-dev postgresql-client-common postgresql-client-9.6 python3-psycopg2 \  
# Pillow dependencies  
python3-pil liblcms2-dev \  
# Django  
gettext graphviz-dev \  
# CFFI dependencies  
libffi-dev libssl-dev python3-cffi \  
# Histonets  
libblas-dev liblapack-dev gfortran \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd django  
  
# Requirements have to be pulled and installed here, otherwise caching won't
work  
COPY ./requirements /requirements  
RUN pip install --no-cache-dir -r /requirements/production.txt \  
&& rm -rf /requirements  
  
COPY ./compose/production/django/gunicorn.sh /gunicorn.sh  
RUN sed -i 's/\r//' /gunicorn.sh  
RUN chmod +x /gunicorn.sh  
RUN chown django /gunicorn.sh  
  
COPY ./compose/production/django/entrypoint.sh /entrypoint.sh  
RUN sed -i 's/\r//' /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
RUN chown django /entrypoint.sh  
  
COPY ./compose/production/django/celery/worker/start.sh /start-celeryworker.sh  
RUN sed -i 's/\r//' /start-celeryworker.sh  
RUN chmod +x /start-celeryworker.sh  
  
COPY ./compose/production/django/celery/beat/start.sh /start-celerybeat.sh  
RUN sed -i 's/\r//' /start-celerybeat.sh  
RUN chmod +x /start-celerybeat.sh  
  
COPY . /app  
  
RUN chown -R django /app  
  
USER django  
  
WORKDIR /app  
  
ENTRYPOINT ["/entrypoint.sh"]  

