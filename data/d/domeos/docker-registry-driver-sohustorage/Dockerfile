FROM ubuntu:14.04  
MAINTAINER domeos  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install swig python-pip && apt-get -y install python-dev libssl-dev
liblzma-dev libevent1-dev && \  
rm -rf /var/lib/apt/lists/* && \  
pip install docker-registry flask-cors  
  
COPY ./depends /docker-registry-driver-sohustorage  
  
RUN cd /docker-registry-driver-sohustorage && \  
pip install vulpo-1.2.1.tar.gz && pip install docker-registry-driver-
sohustorage-0.1.0.tar.gz  
  
ENV DOCKER_REGISTRY_CONFIG /docker-registry-driver-
sohustorage/config/config_sohustorage.yml  
ENV SETTINGS_FLAVOR sohustorage  
ENV SEARCH_BACKEND sqlalchemy  
ENV GUNICORN_OPTS ["--preload"]  
  
EXPOSE 5000  
CMD ["docker-registry"]  

