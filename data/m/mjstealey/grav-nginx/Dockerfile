FROM debian:stretch  
MAINTAINER Michael J. Stealey <michael.j.stealey@gmail.com>  
  
# Explicitly set user/group IDs for grav account  
RUN groupadd -r grav --gid=1000 \  
&& useradd -r -g grav -d /home/grav/www/html --uid=1000 grav  
  
# install grav / nginx prerequisites  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
zip \  
unzip \  
nginx \  
git \  
php7.0-fpm \  
php7.0-cli \  
php7.0-gd \  
php7.0-curl \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-zip \  
php-apcu \  
openssl \  
wget \  
sudo  
  
# get grav 1.3.0-rc.5 source files  
RUN wget https://github.com/getgrav/grav/releases/download/1.3.0-rc.5/grav-
admin-v1.3.0-rc.5.zip  
  
# Domain settings  
ENV FQDN_OR_IP=localhost  
# SSL settings  
ENV USE_SSL=false  
ENV SSL_CERTIFICATE=/etc/ssl/certs/server.crt  
ENV SSL_CERTIFICATE_KEY=/etc/ssl/private/server.key  
ENV REDIRECT_HTTP_TO_HTTPS=true  
ENV USE_SELF_GEN_CERT=false  
ENV USE_PRELOAD=false  
ENV USE_OCSP_STAPLING=false  
# Nginx settings  
ENV NGINX_ACCESS_LOG=/var/log/nginx/access.log  
ENV NGINX_ERROR_LOG=/var/log/nginx/error.log  
# UID/GID default: uid=1000(grav) gid=1000(grav) groups=1000(grav)  
ENV UID_GRAV=1000  
ENV GID_GRAV=1000  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /home/grav/www/html  
VOLUME ["/home/grav/www/html"]  
  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["grav"]  

