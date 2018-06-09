FROM ubuntu:16.04  
MAINTAINER Luiz Felipe F M Costa <luiz@thenets.org>  
  
ENV USER_HOME=/home/easyphp/  
ENV APP=/home/easyphp/html/  
  
USER root  
  
# Upgrade system  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y  
  
# =====================================  
# Install PHP core  
# =====================================  
# Install PHP  
RUN apt-get update && \  
apt-get install -y php php-mysql && \  
apt-get autoclean  
  
# Create easyphp user  
RUN groupadd -r -g 1000 easyphp && \  
useradd -mr -c "easyphp" -d $USER_HOME -g 1000 -u 1000 easyphp  
  
# Create app dir and set permissions  
RUN mkdir -p $APP && chown -R 1000.1000 $USER_HOME  
  
# Change to easyphp user  
USER easyphp  
  
# Create hello world file  
RUN echo "<?php echo 'Hello from PHP. You did\'t set a volume for your
application.'; ?>" > $APP/index.php  
  
# =====================================  
# Install Apache  
# =====================================  
USER root  
RUN apt-get update && \  
apt-get install -y apache2 libapache2-mod-php php-mcrypt php-cli php-curl  
ADD httpd.conf /home/easyphp/httpd.conf  
RUN a2enmod rewrite && \  
adduser easyphp www-data && \  
chown 1000.1000 /home/easyphp/httpd.conf && \  
rm /etc/apache2/sites-available/000-default.conf && \  
ln -s /home/easyphp/httpd.conf /etc/apache2/sites-available/000-default.conf
&& \  
echo '' > /etc/apache2/ports.conf && \  
chmod 777 -R /var/log/apache2/ /var/lock/apache2/  
  
# DEBUG tools  
USER root  
RUN apt-get update && \  
apt-get install -y git curl wget nano htop && \  
apt-get autoclean  
  
# =====================================  
# Install PHP and Composer  
# =====================================  
USER root  
RUN apt-get update && \  
apt-get install -y zip unzip php7.0-zip && \  
apt-get autoclean && \  
ln -s $APP/../composer.phar /usr/local/bin/composer  
USER easyphp  
RUN cd $APP/.. && \  
wget
https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer
-O - -q | php -- --quiet && \  
composer require "laravel/lumen-installer"  
  
# Add easyphp to www-data group  
USER root  
RUN usermod -aG www-data easyphp  
  
# Add index.php file  
ADD ./index.php $APP/index.php  
RUN chown -R 1000.1000 $APP/.. && chmod -R 770 $APP/..  
  
# Config and volume  
USER root  
WORKDIR $APP  
ADD ./entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  
EXPOSE 80  
VOLUME [$APP]

