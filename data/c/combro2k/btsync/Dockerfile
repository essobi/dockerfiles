FROM ubuntu-debootstrap:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN useradd btsync -b /data --no-create-home  
  
RUN apt-get update  
RUN apt-get dist-upgrade -yq  
RUN apt-get install tar curl -yq  
  
RUN mkdir -p /opt/btsync  
WORKDIR /opt/btsync  
  
RUN curl -k -L
http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable | tar
zxv  
ADD start.sh /opt/btsync/start.sh  
RUN chmod +x /opt/btsync/start.sh  
RUN chown -R btsync:btsync /opt/btsync  
  
EXPOSE 8888  
EXPOSE 55555  
VOLUME ["/data"]  
  
CMD ["/opt/btsync/start.sh"]  

