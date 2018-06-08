FROM registry  
  
RUN apt-get update && \  
apt-get install -yq libxml2-dev libxslt1-dev build-essential python-pip
python-dev lib32z1-dev  
RUN pip install docker-registry-driver-swift  
  
RUN mkdir -p /registry  
  
ADD swift_config.yml /docker-registry/config/config.yml  
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config.yml  
ENV STORAGE_PATH /registry  
ENV SETTINGS_FLAVOR local  
  
VOLUME /registry  
  
EXPOSE 5000  
CMD exec docker-registry  

