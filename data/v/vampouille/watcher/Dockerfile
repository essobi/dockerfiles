FROM debian:jessie  
  
MAINTAINER vampouille "julien.acroute@camptocamp.com"  
RUN apt-get update && \  
apt-get install -y inotify-tools && \  
rm -rf /var/lib/apt/lists/* /usr/share/doc/* /usr/share/man/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME [ "/mnt/volume/" ]  
WORKDIR /mnt/volume/  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

