FROM nginx  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
RUN set -xe; \  
apt-get update; \  
apt-get install -y certbot; \  
rm -rf /var/cache/apt/*;  
  
VOLUME /etc/letsencrypt  

