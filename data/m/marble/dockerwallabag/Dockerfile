# Hacked from someone else's wallabag image to add postgres support and update
to 1.9.1  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.16  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update System  
RUN apt-get update && apt-get dist-upgrade -y  
  
# Install locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen cs_CZ.UTF-8  
RUN locale-gen de_DE.UTF-8  
RUN locale-gen es_ES.UTF-8  
RUN locale-gen fr_FR.UTF-8  
RUN locale-gen it_IT.UTF-8  
RUN locale-gen pl_PL.UTF-8  
RUN locale-gen pt_BR.UTF-8  
RUN locale-gen ru_RU.UTF-8  
RUN locale-gen sl_SI.UTF-8  
RUN locale-gen uk_UA.UTF-8  
  
# Install wallabag prereqs  
RUN add-apt-repository ppa:nginx/stable \  
&& apt-get update \  
&& apt-get install -y nginx php5-cli php5-common \  
php5-curl php5-pgsql php5-fpm php5-gd php5-json php5-tidy wget \  
unzip gettext php5-mcrypt  
  
# Configure php-fpm  
RUN echo "cgi.fix_pathinfo = 0" >> /etc/php5/fpm/php.ini  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
COPY conf/www.conf /etc/php5/fpm/pool.d/www.conf  
  
RUN mkdir /etc/service/php5-fpm  
COPY conf/php5-fpm.sh /etc/service/php5-fpm/run  
  
RUN mkdir /etc/service/nginx  
COPY conf/nginx.sh /etc/service/nginx/run  
  
# Wallabag version  
ENV WALLABAG_VERSION 1.9.1  
# Extract wallabag code  
ADD https://github.com/wallabag/wallabag/archive/$WALLABAG_VERSION.zip
/tmp/wallabag-$WALLABAG_VERSION.zip  
  
RUN mkdir -p /var/www  
RUN cd /var/www \  
&& unzip -q /tmp/wallabag-$WALLABAG_VERSION.zip \  
&& mv wallabag-$WALLABAG_VERSION wallabag \  
&& cd wallabag \  
&& curl -s http://getcomposer.org/installer | php \  
&& php composer.phar install \  
&& mkdir write \  
&& mv assets cache write \  
&& sed -i "s#require_once INCLUDES . '/poche/config.inc.php'#require_once ROOT
. '/write/config.inc.php'#" inc/poche/global.inc.php \  
&& sed -i "s#inc/poche/config.inc.php#write/config.inc.php#" install/index.php  
  
COPY conf/99_change_wallabag_config_salt.sh
/etc/my_init.d/99_change_wallabag_config_salt.sh  
  
COPY conf/config.inc.php /var/www/wallabag/write/config.inc.php  
  
RUN rm -f /tmp/wallabag-$WALLABAG_VERSION.zip  
  
RUN chown -R www-data:www-data /var/www/wallabag  
RUN chmod 755 -R /var/www/wallabag  
  
# Configure nginx to serve wallabag app  
COPY conf/nginx-wallabag /etc/nginx/sites-available/default  
  
EXPOSE 80  
# Expose volumes  
WORKDIR /  
  
VOLUME /wallabag/write  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

