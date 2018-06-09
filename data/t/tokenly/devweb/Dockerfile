### Dockerfile  
# Tokenly Development Image for web apps  
# PHP5.5 PHP-FPM and NGINX  
FROM ubuntu:16.04  
MAINTAINER Devon Weller <devon@tokenly.com>  
  
# nginx repo  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:nginx/stable  
# RUN apt-get --fix-missing update  
RUN apt-get -y dist-upgrade  
  
# install nginx and PHP packages  
RUN apt-get install -y \  
curl \  
nginx \  
supervisor \  
php7.0-fpm php7.0-cli php7.0-gmp php7.0-curl php7.0-mcrypt php7.0-mysql
php7.0-gd php7.0-mbstring php7.0-xml \  
git git-core \  
apt-transport-https  
  
# install node v6  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN DISTRO=$(lsb_release -c -s) \  
&& echo "deb https://deb.nodesource.com/node_6.x ${DISTRO} main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_6.x ${DISTRO} main" >>
/etc/apt/sources.list.d/nodesource.list  
RUN apt-get update  
RUN apt-get -y install nodejs  
  
# upgrade npm for node  
# RUN npm --version && npm cache -g clean && npm install -g npm && npm
--version  
# add a "/usr/bin/node" fix for nodejs  
# RUN cd /usr/bin/ && ln -s nodejs node  
# clean up apt-get artifacts  
RUN rm -rf /var/lib/apt/lists/*  
  
# Setup config files  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD ./nginx/default /etc/nginx/sites-enabled/default  
ADD ./supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD ./php-fpm/php-fpm.conf /etc/php/7.0/fpm/php-fpm.conf  
  
# add a tokenly user  
RUN useradd -u 1001 -m -d /home/tokenly -s /bin/bash tokenly  
  
# add a php7.0-fpm error log  
RUN mkdir /var/log/php/ && touch /var/log/php/php7.0-fpm-error.log && chown
tokenly:tokenly /var/log/php/php7.0-fpm-error.log  
  
# add start nginx script  
ADD ./nginx/start-nginx.sh /usr/local/bin/start-nginx.sh  
  
# supervisord directories  
RUN mkdir -p /var/run/supervisor/  
RUN chown nobody. /var/run/supervisor/  
RUN mkdir -p /var/log/supervisord  
RUN mkdir -p /var/log/php  
  
# install composer  
RUN cd /usr/local/bin && curl -sS https://getcomposer.org/installer | php  
  
# Default command for container, start supervisor  
CMD ["supervisord", "--nodaemon", "-c", "/etc/supervisor/supervisord.conf"]  
USER root  
  
  
# Expose port 80 of the container  
EXPOSE 80  

