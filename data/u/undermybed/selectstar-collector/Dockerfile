#  
# Selectstar Collector Alpine Container  
# Maintainer: Matt Shipman  
# https://github.com/UnderMyBed  
# Enviroment Variables:  
# COLLECTOR_NAME  
# SELECTSTAR_SECRET_KEY  
#  
FROM openjdk:8-alpine  
LABEL maintainer "Matt Shipman <undermybed@undermybed.info>"  
  
# Install extra pre-reqs for the collector  
RUN apk update && apk add curl  
  
COPY *.sh /  
  
RUN ["chmod", "+x", "/collector-install.sh"]  
  
RUN ./collector-install.sh  
  
RUN ["chmod", "+x", "/collector-start.sh"]  
  
CMD ./collector-start.sh

