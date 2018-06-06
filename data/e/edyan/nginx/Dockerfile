FROM debian:stretch-slim  
MAINTAINER Emmanuel Dyan <emmanueldyan@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Installation  
RUN apt update && \  
apt upgrade -y && \  
# Packages  
apt install -y --no-install-recommends nginx && \  
# Clean  
apt autoremove -y && \  
apt autoclean && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* /usr/share/man/* /usr/share/doc/* /var/cache/*
/var/log/*  
  
# Configuration  
COPY vhost.conf /etc/nginx/sites-available/default  
  
RUN mv /var/www/html/* /var/www/ && rm -rf /var/www/html  
RUN mkdir /var/log/nginx  
RUN chmod 755 /var/log/nginx  
  
ENV NGINX_UID 33  
ENV NGINX_GID 33  
EXPOSE 80  
COPY run.sh /run.sh  
RUN chmod u+x /run.sh  
  
CMD ["/run.sh"]  

