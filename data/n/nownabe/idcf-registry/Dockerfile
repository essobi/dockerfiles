FROM registry  
MAINTAINER nownabe <nownabe@gmail.com>  
  
ENV SETTINGS_FLAVOR prod  
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config.yml  
ENV GUNICORN_WORKERS 2  
ENV GUNICONR_OPTS [--preload]  
  
ADD config.yml /docker-registry/config/config.yml  
ADD boto.cfg /etc/boto.cfg  
  
EXPOSE 5000  
CMD ["docker-registry"]  

