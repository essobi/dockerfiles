FROM phusion/baseimage:latest  
  
MAINTAINER Eric <ericstone.dev@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Upgrade OS  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Tools  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
git \  
curl  
  
# PHP  
RUN add-apt-repository ppa:ondrej/php5-5.6 && \  
apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
php-pear \  
php5-cli \  
php5-common \  
php5-curl \  
php5-dev \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-imap \  
php5-intl \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-memcached \  
php5-mysql \  
php5-pgsql \  
php5-mongo \  
php5-redis \  
php5-sqlite \  
php5-tidy \  
php5-xdebug  
# php5-xhprof  
RUN service php5-fpm stop  
  
# MySQL Client  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
mysql-client  
  
# NGINX  
RUN DEBIAN_FRONTEND="noninteractive" && \  
apt-get remove --purge --yes nginx && \  
apt-get install --yes \  
nginx-extras \  
ssl-cert \  
&& \  
mkdir /var/cache/nginx  
RUN service nginx stop  
  
# SSH (for remote drush)  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install --yes openssh-server  
RUN dpkg-reconfigure openssh-server  
  
# Drush, console  
RUN cd /usr/local/bin/ && \  
curl http://files.drush.org/drush.phar -L -o drush && \  
chmod +x drush  
COPY ./conf/drush/drush-remote.sh /usr/local/bin/drush-remote  
RUN chmod +x /usr/local/bin/drush-remote  
RUN cd /usr/local/bin/ && \  
curl https://drupalconsole.com/installer -L -o drupal && \  
chmod +x drupal  
  
# PHP CLI config  
COPY ./conf/php5/cli/php.ini /etc/php5/cli/php.ini  
  
# PHP-FPM config  
COPY ./conf/php5/fpm/php.ini-development /etc/php5/fpm/php.ini  
COPY ./conf/php5/fpm/php-fpm.conf-development /etc/php5/fpm/php-fpm.conf  
RUN rm -rf /etc/php5/fpm/pool.d/*  
COPY ./conf/php5/fpm/pool.d /etc/php5/fpm/pool.d  
RUN mkdir -p /var/log/php5-fpm && \  
chown www-data:www-data /var/log/php5-fpm  
  
# Prevent php warnings  
RUN sed -ir 's@^#@//@' /etc/php5/mods-available/*  
RUN php5enmod \  
mcrypt \  
xdebug  
# xhprof  
# Nginx config  
# use drupal7 configuration  
# see https://github.com/ericstone57/drupal-with-nginx  
COPY ./drupal-with-nginx /etc/nginx  
# customized configuration  
COPY ./conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./conf/nginx/upstream_phpcgi_tcp.conf /etc/nginx/upstream_phpcgi_tcp.conf  
COPY ./conf/nginx/apps/drupal/drupal--development.conf
/etc/nginx/apps/drupal/drupal.conf  
COPY ./conf/nginx/htpasswd-users /etc/nginx/.htpasswd-users  
RUN rm -rf /etc/nginx/sites-enabled/*  
COPY ./conf/nginx/sites-enabled /etc/nginx/sites-enabled  
  
# SSH config  
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak  
COPY ./conf/ssh/sshd_config /etc/ssh/sshd_config  
RUN rm -f /etc/service/sshd/down  
  
# Directories  
RUN mkdir -p /var/www/html && \  
chgrp www-data /var/www/html && \  
chmod 755 /var/www/html  
  
# Use baseimage-docker's init system.  
ADD init/ /etc/my_init.d/  
RUN chmod -v +x /etc/my_init.d/*.sh  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/www/html  
  
EXPOSE 80 443 22  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]

