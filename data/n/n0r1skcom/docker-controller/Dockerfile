FROM ubuntu:16.04  
MAINTAINER Mario Kleinsasser "mario.kleinsasser@gmail.com"  
MAINTAINER Bernhard Rausch "rausch.bernhard@gmail.com"  
COPY docker-controller /data/docker-controller  
RUN chmod 755 /data/docker-controller  
  
COPY docker-controller.yml /config/docker-controller.yml  
  
CMD ["/data/docker-controller"]  

