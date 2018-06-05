FROM ubuntu:14.04.2  
ENV DEBIAN_FRONTEND=noninteractive  
  
ADD build/etc/apt/apt.conf.d/90-AlwaysYes /etc/apt/apt.conf.d/90-AlwaysYes  
  
RUN apt-get update  
RUN apt-get install software-properties-common  
RUN add-apt-repository ppa:ondrej/php5-5.6  
  
RUN apt-get update  
RUN apt-get install curl  
RUN apt-get install wget  
RUN apt-get install git  
RUN apt-get install wget  
RUN apt-get install vim  
RUN apt-get install make  
RUN apt-get install nginx  
RUN apt-get install php5-fpm  
RUN apt-get install php5-cli  
RUN apt-get install php5-sqlite  
RUN apt-get install php5-gd  
RUN apt-get install php5-mysql  
RUN apt-get install php5-memcache  
RUN apt-get install mariadb-client  
RUN apt-get install supervisor  
  
RUN mkdir -p /usr/local/bin  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin  
RUN mv /usr/local/bin/composer.phar /usr/local/bin/composer  
  
RUN composer global require drush/drush:~7.0.0  
  
# Setup the symlink  
RUN ln -sf /root/.composer/vendor/bin/drush.php /usr/local/bin/drush  
  
ADD build/etc/nginx/sites-available/default /etc/nginx/sites-available/default  
ADD build/etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf  
ADD build/etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD build/etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
RUN sed -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' -i
/etc/php5/fpm/php.ini  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf  
RUN sed -e 's/;listen\\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf  
RUN sed -e 's/;listen\\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
WORKDIR /app  
  
CMD ["/usr/bin/supervisord", "-n"]  

