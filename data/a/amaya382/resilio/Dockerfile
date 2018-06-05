FROM frolvlad/alpine-glibc:latest  
MAINTAINER amaya <mail@sapphire.in.net>  
  
WORKDIR /usr/local/resilio/  
  
RUN apk add --no-cache curl && \  
curl https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz
| tar xfz -  
  
VOLUME /settings/ /resilio/  
  
EXPOSE 80 55555  
CMD ["./rslsync", "--config", "/etc/rslsync.conf", "--log",
"/var/log/rslsync.log", "--nodaemon"]  

