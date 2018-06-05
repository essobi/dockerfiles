FROM homeassistant/home-assistant:latest  
  
MAINTAINER Kiall Mac Innes <kiall@macinnes.ie>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends miniupnpc libminiupnpc-dev
libminiupnpc10 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install miniupnpc

