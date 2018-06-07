FROM janeczku/debian-s6:wheezy-backports  
MAINTAINER Jan Broer <janeczku@yahoo.com>  
  
RUN \  
apt-wrap apt-get update && \  
apt-wrap apt-get install -y \--no-install-recommends wget ca-certificates && \  
  
# Add dotdeb repository  
wget -qO - http://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
sh -c 'echo "deb http://packages.dotdeb.org wheezy all" >>
/etc/apt/sources.list.d/doteb.list' && \  
sh -c 'echo "deb-src http://packages.dotdeb.org wheezy all" >>
/etc/apt/sources.list.d/doteb.list' && \  
apt-wrap apt-get update && \  
  
# Install Nginx  
apt-wrap apt-get install -y nginx-extras && \  
  
# Rename nginx:nginx user/group to www:www, also set uid:gid to 80:80  
groupmod \--gid 80 \--new-name www www-data && \  
usermod \--uid 80 \--home /data/www \--gid 80 \--login www \--shell /bin/bash
\--comment www www-data && \  
  
# Clean-up /etc/nginx/ directory  
rm -rf /etc/nginx/*.d /etc/nginx/*_params && \  
  
# Create dummy SSL certificates  
mkdir -p /etc/nginx/ssl && \  
openssl genrsa -out /etc/nginx/ssl/dummy.key 1024 && \  
openssl req -new -key /etc/nginx/ssl/dummy.key -out /etc/nginx/ssl/dummy.csr
-subj "/C=GB/L=London/O=Company Ltd/CN=docker" && \  
openssl x509 -req -days 3650 -in /etc/nginx/ssl/dummy.csr -signkey
/etc/nginx/ssl/dummy.key -out /etc/nginx/ssl/dummy.crt && \  
openssl dhparam -out /etc/nginx/ssl/dhparam.pem 1024 && \  
  
# Clean up  
apt-clean  
  
COPY rootfs /  
  
ENV GENERATE_DEFAULT_HOST=false  
  
EXPOSE 80 443  
  
VOLUME ["/data"]  

