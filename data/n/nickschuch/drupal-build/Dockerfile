# Drupal  
#  
# VERSION 0.0.1  
FROM ubuntu:12.04  
MAINTAINER Nick Schuch (nick@myschuch.com)  
  
##  
# APT.  
##  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
##  
# Base.  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install fail2ban vim git curl
wget pwgen python-setuptools vim-tiny sudo python-software-properties unzip  
  
##  
# Apache.  
##  
RUN add-apt-repository ppa:ondrej/php5  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 php5
libapache2-mod-php5 php5-curl php5-mcrypt php5-mysql php5-gd php-apc php-pear
php5-dev php5-pspell libssl-dev  
  
# This script is used for Supervisord to keep Apache running.  
ADD ./scripts/foreground.sh /etc/apache2/foreground.sh  
RUN rm -rf /var/www/  
RUN chmod 755 /etc/apache2/foreground.sh  
  
# This fixes missing file errors.  
RUN touch /etc/apache2/httpd.conf  
RUN mkdir /etc/apache2/conf.d  
  
# Mods.  
RUN cd /etc/apache2/mods-enabled && ln -s ../mods-available/rewrite.load .  
RUN cd /etc/apache2/mods-enabled && ln -s ../mods-available/headers.load .  
  
# We are removing this because we deal with it in our own custom apache2.conf.  
RUN rm /etc/apache2/mods-enabled/mpm_prefork.conf  
  
# vHost.  
RUN rm -f /etc/apache2/sites-enabled/*  
ADD ./conf/apache2/vhost.conf /etc/apache2/sites-available/drupal.conf  
RUN ln -s /etc/apache2/sites-available/drupal.conf /etc/apache2/sites-
enabled/drupal.conf  
  
##  
# PHP.  
# Required PHP packages.  
##  
ADD ./conf/php/php.ini /etc/php5/apache2/php.ini  
ADD ./conf/php/php.ini /etc/php5/cli/php.ini  
  
# Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
# Drush.  
ADD https://github.com/drush-ops/drush/archive/6.2.0.zip /tmp/drush.zip  
RUN cd /tmp && unzip -d /tmp /tmp/drush.zip  
RUN mv /tmp/drush-6.2.0 /opt/drush  
RUN ln -s /opt/drush/drush /usr/local/bin/drush  
RUN chmod -R 777 /opt/drush/lib  
# Run drush once, so Console_Table is downloaded and installed.  
RUN /usr/local/bin/drush  
  
##  
# SSHD.  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server  
ADD https://github.com/nickschuch.keys /root/.ssh/authorized_keys  
RUN chmod 400 /root/.ssh/authorized_keys  
  
##  
# Supervisord.  
##  
RUN easy_install supervisor  
ADD ./conf/supervisord/supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor/  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
EXPOSE 22 80  
CMD ["/start.sh"]  
  
##  
# Onbuild.  
# These are run on child Docker builds. They build the web application.  
##  
# We upload this entire build pack so we can ship configuration and do things  
# with it in the build.sh on child image builds.  
ADD . /opt/drupal  
  
ONBUILD ADD . /var/www  
ONBUILD RUN chown -R www-data:www-data /var/www  
ONBUILD RUN sh /var/www/build.sh  

