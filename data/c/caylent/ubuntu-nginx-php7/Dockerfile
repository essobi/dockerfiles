FROM ubuntu:14.04  
MAINTAINER Stefan Thorpe <stefan@caylent.com>  
  
ENV NGINX_SITE_HOME /usr/share/nginx/html  
ENV NGINX_PATH /etc/nginx  
ENV NGINX_SITE_CONF_PATH /etc/nginx/conf.d  
  
#Install Packages  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y language-pack-en-base
software-properties-common &&\  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \  
echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list && \  
echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list.d/nginx.list && \  
apt-key adv --fetch-keys "http://nginx.org/keys/nginx_signing.key" && \  
apt-get update -y && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
supervisor \  
php7.0 \  
php7.0-fpm php7.0-common\  
php7.0-curl php7.0-mbstring php7.0-xml php7.0-mysql php7.0-dev\  
git \  
nginx \  
libyaml-dev && \  
pecl install yaml-2.0.0 && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ${NGINX_SITE_HOME}/* && \  
mkdir /run/php && \  
echo "extension=yaml.so" >> /etc/php/7.0/fpm/php.ini && \  
echo "extension=yaml.so" >> /etc/php/7.0/cli/php.ini  
  
#Setup Services to start  
  
COPY supervisord.conf /etc/supervisor/conf.d/  
COPY default.conf ${NGINX_SITE_CONF_PATH}/  
COPY nginx.conf ${NGINX_PATH}  
COPY php-fpm.conf /etc/php/7.0/fpm/  
  
# forward request and error logs to docker log collector  
# This might not be needed if logs are ported to /dev/std... in virtualhost  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
CMD ["/usr/bin/supervisord"]  

