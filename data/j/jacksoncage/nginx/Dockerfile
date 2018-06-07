# Nginx container  
#  
# docker run -rm -i -d \  
# -p 80 \  
# -e NGINX_SERVER_NAME=jacksoncage.se \  
# -v /etc/localtime:/etc/localtime \  
# jacksoncage/nginx  
FROM debian:jessie  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2015-12-11  
# Install applications  
RUN apt-get update -qq && \  
apt-get upgrade -yqq && \  
apt-get -yqq install wget curl nginx && \  
ln -s /etc/nginx/sites-available/001-docker /etc/nginx/sites-
enabled/001-docker  
  
# Clean image  
RUN apt-get -yqq clean && \  
apt-get -yqq purge && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
COPY 001-docker /etc/nginx/sites-available/  
  
ENV NGINX_RUN_USER www-data  
ENV NGINX_RUN_GROUP www-data  
ENV NGINX_LOG_DIR /var/log/nginx  
ENV NGINX_BACKEND_IP 172.17.42.1  
ENV NGINX_BACKEND_PORT 80  
ENV NGINX_SERVER_NAME localhost  
  
EXPOSE 80 443  
COPY start.sh /start.sh  
CMD ["/start.sh"]  

