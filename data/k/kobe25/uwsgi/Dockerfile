FROM python:3.5  
MAINTAINER Antonio Esposito "kobe@member.fsf.org"  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt update && apt install -y \  
build-essential \  
python-dev \  
python-setuptools && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install 'uWSGI >=2.0, <2.1'  
RUN groupadd --system --gid 1000 app && \  
useradd --system --gid 1000 --uid 1000 --home-dir /code app  
ENV UWSGI_UID app  
ENV UWSGI_GID app  
  
# Process  
ENV UWSGI_MASTER true  
ENV UWSGI_MASTER_AS_ROOT false  
ENV UWSGI_NO_ORPHANS true  
ENV UWSGI_VACUUM true  
ENV UWSGI_LOG_DATE true  
  
# Application  
ENV UWSGI_AUTOLOAD false  
ENV UWSGI_LAZY_APPS false  
ENV UWSGI_WORKERS 4  
ENV UWSGI_THREADS 1  
ENV UWSGI_ENABLE_THREADS true  
ENV UWSGI_BUFFER_SIZE 65536  
ENV UWSGI_MAX_REQUESTS 512  
ENV UWSGI_HARAKIRI 60  
ENV UWSGI_HARAKIRI_VERBOSE true  
ENV UWSGI_THUNDER_LOCK true  
  
# Socket  
ENV UWSGI_UWSGI_SOCKET 0.0.0.0:5000  
EXPOSE 5000  
# Python specific  
ENV PYTHONUNBUFFERED 1  
ENV PYTHONPATH /code:/usr/local/lib/python3.5/site-packages  
ENV UWSGI_CALLABLE app  
  
# PostgreSQL specific  
ENV PGDATABASE app  
ENV PGUSER app  
ENV PGPASSWORD app  
ENV PGHOST db  
ENV PGPORT 5432  
CMD ["uwsgi"]  

