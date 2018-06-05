FROM bytesized/debian-base  
MAINTAINER maran@bytesized-hosting.com  
  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository 'deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu
trusty main' && apt-get update  
RUN apt-get install -y -t trusty deluged deluge-web  
  
EXPOSE 8112 58846 58946 58946/udp  
  
VOLUME /config /data /media  
  
COPY static/ /  

