FROM ubuntu:16.04  
MAINTAINER thomaspb  
  
ENV DOLLAR $  
  
ARG ORIGIN  
ARG DOMAIN  
ARG EMAIL  
  
RUN apt update && \  
apt install -y software-properties-common && \  
add-apt-repository ppa:certbot/certbot -y && \  
apt update && \  
apt upgrade -y && \  
apt install -y locales && \  
locale-gen "el_GR.UTF-8" && \  
apt install -y nginx && \  
apt install -y gettext && \  
apt install -y python-certbot-apache && \  
mkdir -p /var/cache/nginx/wowza_cache_temp  
  
ADD run.sh /root/run.sh  
ADD nginx.conf /tmp/nginx.conf  
  
EXPOSE 443  
EXPOSE 80  
RUN chmod +x /root/run.sh  
  
#CMD ["sh", "/root/init.sh"]  

