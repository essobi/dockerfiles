FROM python:3.6-alpine  
  
ADD requirements.txt /requirements.txt  
  
RUN set -ex \  
&& buildDeps="gcc make libc-dev musl-dev linux-headers pcre-dev postgresql-dev
postgresql-client" \  
# && runDeps="postgresql-client postgresql-dev" \  
&& apk add \--no-cache --virtual .build-deps $buildDeps \  
&& python3.6 -m venv /venv \  
&& /venv/bin/pip install -U pip \  
&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir
-r /requirements.txt" \  
# && apk del .build-deps $buildDeps \  
&& apk add \--no-cache --update --virtual .python-rundeps  
# $runDeps  
# Copy your application code to the container (make sure you create a
.dockerignore file if any large files or directories should be excluded)  
RUN mkdir /code/  
WORKDIR /code/  
COPY . /code/  
RUN touch /code/salversion.log && chmod 777 /code/salversion.log  
  
# uWSGI will listen on this port  
EXPOSE 8000  
  
# Add any custom, static environment variables needed by Django or your
settings file here:  
# ENV DJANGO_SETTINGS_MODULE=my_project.settings.deploy  
# uWSGI configuration (customize as needed):  
ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=salversion/wsgi.py UWSGI_HTTP=:8000
UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000
UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy  
  
ENV RUNNING_ENVIRONMENT=docker  
  
# Call collectstatic (customize the following line with the minimal
environment variables needed for manage.py to run):  
# RUN DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput  
RUN chmod +x /code/docker-entrypoint.sh  
ENTRYPOINT ["/code/docker-entrypoint.sh"]  
  
# Start uWSGI  
CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]  

