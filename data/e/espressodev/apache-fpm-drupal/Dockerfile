FROM ubuntu:14.04  
MAINTAINER Ian Lintner "ian.lintner@workiva.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV TERM xterm  
  
# Update system  
RUN apt-get update -y && apt-get dist-upgrade -y  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:ondrej/php5-5.6  
RUN add-apt-repository ppa:ondrej/apache2  
RUN add-apt-repository ppa:ondrej/mysql-5.5  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted universe
multiverse" > /etc/apt/sources.list  
RUN apt-get update -y && apt-get dist-upgrade -y  
  
# Basic packages  
RUN apt-get -y install libmysqlclient18 php5 php5-fpm php5-mysql php5-gd
php5-mcrypt php5-curl php5-cli php5-sqlite php5-common php-pear curl php5-json
php5-memcache nano  
RUN apt-get -y install apache2 libapache2-mod-fastcgi supervisor  
  
#RUN php5enmod mcrypt  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Composer and Drush  
RUN /usr/local/bin/composer self-update  
RUN /usr/local/bin/composer global require drush/drush:6.*  
RUN ln -s /root/.composer/vendor/drush/drush/drush /usr/local/bin/drush  
  
VOLUME ["/var/www"]  
VOLUME ["/var/files"]  
  
RUN mkdir -p /var/log/supervisor  
  
ADD conf/apache2/sites-available/default.conf /etc/apache2/sites-
available/default.conf  
RUN a2enmod rewrite proxy proxy_fcgi proxy_http  
RUN a2dissite 000-default  
RUN a2ensite default  
RUN sed -i "s/listen =.*/listen = 127.0.0.1:9000/"
/etc/php5/fpm/pool.d/www.conf  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh && chgrp -Rv www-data /var/files && chown
-R www-data:www-data /var/www  
  
EXPOSE 80  
CMD ["/usr/local/bin/run.sh"]

