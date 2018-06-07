FROM semtech/mu-nginx-spa-proxy:1.0.1  
MAINTAINER Aad Versteden <madnificent@gmail.com>  
  
ENV STATIC_FOLDERS_REGEX "^/(assets|font|images)/"  
RUN apt-get update; apt-get upgrade -y; apt-get install -y unzip wget;  
COPY package.json /package.json  
RUN mkdir /app; cd /app; wget https://github.com/big-data-europe/ember-swarm-
ui-frontend/releases/download/v$(cat /package.json | grep version | head -n 1
| awk -F: '{ print $2 }' | sed 's/[ ",]//g')/dist.zip  
RUN cd /app; unzip dist.zip; mv dist/* .  
RUN rm /app/dist.zip package.json  

