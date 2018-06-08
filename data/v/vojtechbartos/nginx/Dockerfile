FROM nginx:1.9.7  
MAINTAINER Vojta Bartos <hi@vojtech.me>  
  
RUN \  
apt-get update && \  
apt-get install -y python && \  
mkdir -p /etc/nginx/sites-enabled/  
  
ADD configs/nginx.conf /etc/nginx/nginx.conf  
ADD configs/templates/ /etc/nginx/templates/  
ADD scripts/ /etc/nginx/scripts/  
  
ENTRYPOINT python /etc/nginx/scripts/generate_sites.py && nginx  

