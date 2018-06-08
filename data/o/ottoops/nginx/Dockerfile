FROM ubuntu:14.04  
MAINTAINER Paul Otto <paul@ottoops.com>  
  
RUN \  
env DEBIAN_FRONTEND=noninteractive apt-get update -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update -y && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
WORKDIR /etc/nginx  
  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx"]

