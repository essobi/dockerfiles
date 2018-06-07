FROM phusion/baseimage:latest  
MAINTAINER VUTROX Entertainment <contact@vutrox.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG ECO_VERSION=0.7.4.6-beta  
ENV ECO_VERSION=${ECO_VERSION}  
LABEL eco.version=${ECO_VERSION}  
  
ENV PUID=1000  
ENV PGID=1000  
ENV KILL_PROCESS_TIMEOUT=300  
ENV KILL_ALL_PROCESSES_TIMEOUT=300  
ADD install-packages.sh /  
RUN chmod +x /install-packages.sh  
RUN /install-packages.sh  
RUN rm /install-packages.sh  
  
CMD ["/sbin/my_init"]  
EXPOSE 3000/udp 3001/tcp  
VOLUME ["/home/eco/ecoserver/Configs", "/home/eco/ecoserver/Storage",
"/home/eco/ecoserver/Logs"]  
WORKDIR /home/eco/ecoserver  
  
ADD start-server.sh ./start-server  
RUN chmod +x ./start-server  
  
ADD install-server.sh ./install-server.sh  
RUN chmod +x ./install-server.sh  
RUN ./install-server.sh  
RUN rm ./install-server.sh  
  
RUN mkdir -p /etc/my_init.d  
ADD eco-init.sh /etc/my_init.d/eco-init.sh  
RUN chmod +x /etc/my_init.d/eco-init.sh

