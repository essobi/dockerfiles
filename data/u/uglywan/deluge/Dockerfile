FROM ubuntu:trusty  
MAINTAINER Ugly-Wan  
  
# Language set, using US for consistency  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
RUN update-locale LANG=$LANG  
RUN update-locale LANGUAGE=$LANG  
  
# Install time,  
RUN apt-get -qy update  
RUN apt-get -qy install deluged deluge-webui  
RUN apt-get -qy upgrade  
  
# Startup script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 8112 58846  
#Mount points  
VOLUME /mnt/blackhole  
VOLUME /mnt/downloads  
VOLUME /mnt/complete  
VOLUME /mnt/appdata  
  
ADD core.conf /mnt/appdata/core.conf  
  
CMD ["/start.sh"]  

