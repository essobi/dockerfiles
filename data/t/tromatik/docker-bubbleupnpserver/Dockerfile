FROM ubuntu:latest  
  
RUN apt-get -y update && \  
apt-get -y install --no-install-recommends openjdk-7-jre-headless software-
properties-common && \  
add-apt-repository ppa:bubbleguuum/bubbleupnpserver && \  
apt-get -y update && apt-get -y install bubbleupnpserver && \  
add-apt-repository ppa:mc3man/trusty-media && \  
apt-get -y update && apt-get -y install ffmpeg  
  
EXPOSE 58050/tcp 58051/tcp 1900/udp  
  
ENTRYPOINT [ "/usr/share/bubbleupnpserver/launch.sh" ]  

