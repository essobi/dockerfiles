FROM python:3.6  
MAINTAINER mezz64 <jtmihalic@gmail.com>  
  
RUN apt-get update && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
VOLUME /conf  
  
# Grab source  
RUN git clone https://github.com/home-assistant/appdaemon.git .  
  
# INSTALL  
RUN pip3 install .  
  
CMD [ "appdaemon", "-c", "/conf" ]  

