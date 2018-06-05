FROM debian:jessie  
  
MAINTAINER "Braydee Johnson" <braydee@braydeejohnson.com>  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y nginx  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/laravel /etc/nginx/sites-available/laravel  
RUN ln -s /etc/nginx/sites-available/laravel /etc/nginx/sites-enabled/laravel
&& \  
rm /etc/nginx/sites-enabled/default  
  
RUN mkdir -p /data && \  
mkdir -p /logs  
VOLUME ["/data"]  
VOLUME ["/data/logs"]  
  
# PORTS  
EXPOSE 80  
EXPOSE 443  
  
WORKDIR /opt/bin  
CMD service nginx start

