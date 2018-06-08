FROM python:slim-stretch  
  
  
# Copy the code  
ADD . /code  
WORKDIR /code  
  
# install deps  
RUN apt-get update && apt-get install -y gcc && \  
pip install --no-cache-dir -r requirements.txt && \  
apt-get remove -y gcc && apt-get autoremove -y  
  
# configure django  
ENV DJANGO_SETTINGS_MODULE=settings  
  
# configure uwsgi  
ENV UWSGI_WSGI_FILE=wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2
UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1
UWSGI_WSGI_ENV_BEHAVIOR=holy  
  
# collect static files  
RUN python manage.py collectstatic  
  
CMD sleep 5 && python manage.py migrate && uwsgi  

