FROM ubuntu:16.04  
MAINTAINER Francois-Xavier Derue  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
supervisor \  
curl \  
libssl-dev \  
libffi-dev \  
python-dev \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
python-pip  
  
RUN pip install --upgrade pip setuptools  
RUN pip install gunicorn  
  
COPY requirements.txt /opt/local/src/magpie/requirements.txt  
RUN pip install -r /opt/local/src/magpie/requirements.txt  
COPY ./ /opt/local/src/magpie/  
RUN pip install /opt/local/src/magpie/  
  
RUN make docs -f /opt/local/src/magpie/Makefile  
  
ENV POSTGRES_USER=pavics  
ENV POSTGRES_DB=pavics  
ENV POSTGRES_PASSWORD=qwerty  
ENV POSTGRES_HOST=postgres  
ENV POSTGRES_PORT=5432  
ENV DAEMON_OPTS --nodaemon  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "--nodaemon"]  
#WORKDIR /  
#ENTRYPOINT exec gunicorn -b 0.0.0.0:2001 --paste
/opt/local/src/magpie/magpie/magpie.ini  

