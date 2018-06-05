FROM phusion/baseimage:0.9.17  
MAINTAINER Adam Engebretson <adam.engebretson@bridgeconx.com>  
# INSPIRED BY github.com/harshjv/docker-php-nginx  
# Default baseimage settings  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add some repositories - staying up to date!  
RUN apt-add-repository ppa:ondrej/php5-5.6 -y \  
&& apt-add-repository ppa:nginx/stable -y  
RUN apt-get update  
  
# Install some CLI goodies  
RUN apt-get install -y --force-yes \  
wget \  
git  
  
# Install Base PHP Packages  
RUN apt-get install -y --force-yes \  
php5-cli \  
php5-dev \  
php-pear \  
php5-mysqlnd \  
php5-pgsql \  
php5-sqlite \  
php5-apcu \  
php5-json \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-gmp \  
php5-imap \  
php5-mcrypt \  
php5-memcached \  
php5-xdebug \  
imagemagick \  
php5-imagick  
  
# Make The MCrypt Extension Available  
RUN sudo php5enmod mcrypt  
  
# Install Composer Package Manager  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# See https://github.com/hirak/prestissimo/issues/45  
# RUN composer global require hirak/prestissimo  
# Misc. PHP CLI Configuration  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php5/cli/php.ini  
RUN sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/cli/php.ini  
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php5/cli/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = America\/Chicago/"
/etc/php5/cli/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/cli/php.ini  
  
# Install Mongo Bindings - PHP Module is Loaded with the File Dump (see below)  
RUN echo "no" > _no  
RUN sudo pecl install mongo < _no  
RUN rm _no  
  
# Install Nginx & PHP-FPM  
RUN apt-get install -y --force-yes \  
nginx \  
php5-fpm  
  
# Tweak Some PHP-FPM Settings  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = America\/Chicago/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/\;session.save_path = .*/session.save_path =
\"\/var\/lib\/php5\/sessions\"/" /etc/php5/fpm/php.ini  
RUN rm /etc/php5/cli/conf.d/20-xdebug.ini  
  
# Configure Nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i "s/# server_names_hash_bucket_size.*/server_names_hash_bucket_size
64;/" /etc/nginx/nginx.conf  
RUN sed -i "s/;request_terminate_timeout.*/request_terminate_timeout = 60/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/worker_processes.*/worker_processes auto;/"
/etc/nginx/nginx.conf  
RUN sed -i "s/# multi_accept.*/multi_accept on;/" /etc/nginx/nginx.conf  
RUN sed -i "s/sendfile on/sendfile off/" /etc/nginx/nginx.conf  
RUN mkdir -p /var/www  
RUN chown www-data:www-data -R /var/www  
  
# Installing NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# == FILE DUMP == #  
ADD files/confd /confd  
ADD files/etc /etc  
ADD files/root /root  
  
# Add nginx service  
RUN mkdir /etc/service/nginx  
ADD build/nginx/run.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
# Add PHP service  
RUN mkdir /etc/service/phpfpm  
ADD build/php/run.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
# Add service  
RUN mkdir /etc/service/confd  
ADD build/confd/run.sh /etc/service/confd/run  
RUN chmod +x /etc/service/confd/run  
  
VOLUME ["/var/www", "/etc/nginx/sites-available", "/etc/nginx/sites-enabled"]  
  
WORKDIR /var/www  
  
EXPOSE 80  

