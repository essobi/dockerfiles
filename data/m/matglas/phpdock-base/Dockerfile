# Image is based on https://registry.hub.docker.com/u/phusion/baseimage/  
# and the php contains the Dockerfile.  
FROM phusion/baseimage:0.9.16  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Inspired by Tutum Apache PHP.  
#  
# https://registry.hub.docker.com/u/tutum/apache-php/dockerfile/  
#  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set timezone and locale.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# PHP Packages.  
RUN apt-get update && apt-get -y install \  
php5 php5-fpm php5-gd php5-ldap \  
php5-sqlite php5-pgsql php-pear php5-mysql php5-curl \  
php5-mcrypt php5-xmlrpc php5-intl php5-xdebug \  
build-essential curl mysql-client  
  
##  
# Now all our stuff.  
##  
# Preinstall some things that don't change.  
RUN apt-get update -q \  
&& apt-get install -y apt-utils \  
&& apt-get -y install \  
git \  
unzip \  
nano \  
&& apt-get clean  
  
# Install composer related packages.  
ENV PATH $PATH:$HOME/.composer/vendor/bin  
RUN cd $HOME \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer config --global cache-dir /cache/composer  
  
# Install drush.  
ENV DRUSH_VERSION 8.0.0-rc1  
RUN composer global require drush/drush:$DRUSH_VERSION \--prefer-source \  
&& drush cc drush  
  
# Exporting current path to make tools available when using nsenter.  
RUN echo "export PATH=$PATH" >> $HOME/.bashrc \  
&& echo "export TERM=xterm" >> $HOME/.bashrc  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

