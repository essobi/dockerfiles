FROM debian  
MAINTAINER William McGann <contact@WilliamMcGann.com>  
  
COPY . /  
  
RUN apt-get update && apt-get -y install sabnzbdplus && apt-get -y clean  
  
VOLUME /data  
  
CMD ["sabnzbdplus", "--config-file", "/data/sabnzbd.ini", "-s", "0.0.0.0:80"]  

