FROM ubuntu:trusty  
  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# add NGINX official stable repository  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/nginx.list  
  
# add PHP7 unofficial repository
(https://launchpad.net/~ondrej/+archive/ubuntu/php)  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/php.list  
  
# install packages  
RUN apt-get update && \  
apt-get -y --force-yes --no-install-recommends install \  
supervisor \  
curl \  
nginx \  
php7.0-fpm php7.0-cli php7.0-common php7.0-curl php7.0-gd php7.0-intl
php7.0-json php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-opcache
php7.0-soap php7.0-xml php7.0-xmlrpc php7.0-xsl php7.0-zip php7.0-gd  
  
# Install the composer  
RUN curl -sS http://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer  
RUN chmod +x /usr/bin/composer  
  
# configure NGINX as non-daemon  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# configure php-fpm as non-daemon  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
  
# clear apt cache and remove unnecessary packages  
RUN apt-get autoclean && apt-get -y autoremove  
  
#generate htpasswd for nginx domain  
RUN mkdir -p /etc/nginx/htpasswd  
  
# NGINX mountable directories for config and logs  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
# NGINX mountable directory for apps  
VOLUME ["/var/www"]  
  
# copy config file for Supervisor  
COPY config/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
# backup default default config for NGINX  
RUN cp /etc/nginx/sites-available/default /etc/nginx/sites-
available/default.bak  
  
# copy local defualt config file for NGINX  
COPY config/nginx/default /etc/nginx/sites-available/default  
  
# php7.0-fpm will not start if this directory does not exist  
RUN mkdir /run/php  
  
# NGINX ports  
EXPOSE 80 443 8000  
CMD ["/usr/bin/supervisord"]  

