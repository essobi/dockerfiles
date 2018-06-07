# Use phusion/baseimage as base image.  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.10.1  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install packages for Laravel and front-end build process  
ENV DOCKER_USER_ID 501  
ENV DOCKER_USER_GID 20  
ENV BOOT2DOCKER_ID 1000  
ENV BOOT2DOCKER_GID 50  
# Tweaks to give Apache/PHP write permissions to the app  
RUN usermod -u ${BOOT2DOCKER_ID} www-data && \  
usermod -G staff www-data && \  
useradd -r mysql && \  
usermod -G staff mysql  
  
RUN groupmod -g $(($BOOT2DOCKER_GID \+ 10000)) $(getent group $BOOT2DOCKER_GID
| cut -d: -f1)  
RUN groupmod -g ${BOOT2DOCKER_GID} staff  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN add-apt-repository -y ppa:ondrej/php && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install ca-certificates nodejs npm supervisor wget git apache2 php-
xdebug libapache2-mod-php5.6 php5.6 pwgen php5.6-apc php5.6-mcrypt php5.6-gd
php5.6-xml php5.6-mbstring php5.6-curl php5.6-dev php5.6-sybase freetds-common
libsybdb5 php5.6-gettext zip unzip php5.6-zip jq openssh-client && \  
npm install -g --silent n \  
gulp-cli \  
bower \  
yarn && \  
n stable && \  
yarn global add node-sass && \  
ln -sf /usr/local/n/versions/node/8.2.1/bin/node /usr/bin/node && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
echo "[global]" > /etc/freetds/freetds.conf && \  
echo "tds version = 8.0" >> /etc/freetds/freetds.conf && \  
echo "text size = 20971520" >> /etc/freetds/freetds.conf && \  
echo "client charset = UTF-8" >> /etc/freetds/freetds.conf  
  
# Update CLI PHP to use 5.6  
RUN ln -sfn /usr/bin/php5.6 /etc/alternatives/php  
  
# Set PHP timezones to Australia/Sydney  
RUN sed -i "s/;date.timezone =/date.timezone = Australia\/Sydney/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i "s/;date.timezone =/date.timezone = Australia\/Sydney/g"
/etc/php/5.6/cli/php.ini  
  
# Add composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
# We need Phpunit 5.7 for this to work  
RUN php -r "copy('https://phar.phpunit.de/phpunit-5.7.phar', 'phpunit');" && \  
mv phpunit /usr/local/bin  
  
# Set Executable Bit for Phpunit  
RUN chmod +x /usr/local/bin/phpunit  
  
# Rewrite enable  
RUN a2enmod rewrite  
  
# Configure /app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for the app  
VOLUME [ "/app" ]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

