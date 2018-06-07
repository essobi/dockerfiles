FROM resin/armv7hf-debian-qemu:latest  
MAINTAINER Sebastian Schneider <mail@sesc.eu>  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y ruby build-essential curl python git unzip  
  
RUN curl -O http://node-arm.herokuapp.com/node_latest_armhf.deb \  
&& dpkg -i node_latest_armhf.deb  
  
RUN curl -O dashing.zip https://github.com/Shopify/dashing/zipball/master  
  
# && unzip dashing.zip "Shopify-dashing-*/*" -d /dashing \  
# && rm dashing.zip  
RUN [ "cross-build-end" ]  
  
EXPOSE 3030  

