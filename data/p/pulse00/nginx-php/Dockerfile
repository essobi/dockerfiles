#  
# Nginx Dockerfile  
#  
# https://github.com/dockerfile/nginx  
#  
# Pull base image.  
FROM stackbrew/ubuntu:13.10  
# Setup repositories  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
# Install nginx  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Install PHP  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes php5-fpm
php5-cli php5-dev php-pear php5-mysqlnd php5-json php5-mcrypt php5-gd
php5-sqlite php5-curl php5-intl php5-xdebug php5-memcache php5-imagick  
  
# Patch php.ini  
RUN echo "xdebug.max_nesting_level = 400" >> /etc/php5/fpm/php.ini  
RUN echo "xdebug.max_nesting_level = 400" >> /etc/php5/cli/php.ini  
  
# Attach volumes. I'm not 100% we really need this yet ;)  
VOLUME /etc/nginx/sites-enabled  
VOLUME /var/log/nginx  
VOLUME /var/www  
  
# Set working directory.  
WORKDIR /etc/nginx  
  
# Expose ports.  
EXPOSE 80  
# add the startup script  
ADD ./startup.sh /opt/startup.sh  
  
# Define default command.  
CMD ["/bin/bash", "/opt/startup.sh"]  

