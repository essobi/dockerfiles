FROM flxel/base:latest  
MAINTAINER elseym <elseym@me.com>  
  
# configure  
EXPOSE 8080  
ENV FLXEL_SERVICE_CMD sabnzbdplus -f /config/sabnzbd  
  
# install software  
RUN apt-get -qy install par2 python-yenc python-openssl unzip unrar
sabnzbdplus  

