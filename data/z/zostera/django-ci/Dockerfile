FROM ubuntu:17.10  
MAINTAINER Zostera B.V.  
LABEL version="0.2.2"  
# Based on work by Janusz Skonieczny @wooyek  
# Install tooling for test debugging and libraries needed by geodjango.  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get install -y git unzip wget sudo curl build-essential \  
python python-dev python-pip python-virtualenv \  
python3.6 python3.6-dev \  
postgresql-client-common libpq-dev \  
postgresql postgresql-contrib postgis \  
libmemcached11 libmemcachedutil2 libmemcached-dev libz-dev memcached \  
libproj-dev libfreexl-dev libgdal-dev gdal-bin  
  
# install recent version of nodejs  
RUN apt-get -y install python-software-properties && \  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
apt-get -y install nodejs  
  
RUN python -m pip install pip -U && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
pip install -U tox setuptools  
  
ENV PYTHONIOENCODING=utf-8  
ENV LANG=en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Pass this environment variables through a file  
# https://docs.docker.com/engine/reference/commandline/run/#set-environment-
variables--e---env---env-file  
# They will be used to create a default database on start  
ENV DB_NAME=application-db \  
DB_PASSWORD=application-db-password \  
DB_USER=application-user-user \  
DB_HOST=127.0.0.1 \  
DB_TEST_NAME=application-test-db  
  
COPY django-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/django-entrypoint.sh  
ENTRYPOINT ["django-entrypoint.sh"]  

