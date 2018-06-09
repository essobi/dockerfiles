FROM flxel/base:latest  
MAINTAINER elseym <elseym@me.com>  
  
# configure  
EXPOSE 9091  
ENV FLXEL_SERVICE_CMD transmission-daemon -f -a '*' -g /config/transmission
--log-info  
  
# install software  
RUN apt-get -qy install transmission-daemon  

