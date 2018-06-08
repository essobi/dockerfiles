FROM debian:jessie  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update && apt-get upgrade -y  
  
# install basic utilities  
RUN apt-get install -y gettext git sudo netcat  
  
# install php-fpm  
RUN apt-get install -y php5-fpm php5-cli php5-curl php5-intl php5-mysql
php5-apcu php5-mcrypt  
  
RUN apt-get clean  
  
# setup php-fpm  
COPY www.conf /etc/php5/fpm/pool.d/www.conf.tpl  
  
ENV PHP_FPM_ROOT_DIR=/var/app/current  
ENV PHP_FPM_USER=www-data  
ENV PHP_FPM_GROUP=www-data  
ENV APP_UTILS_DIR=/opt/app-utils  
  
# prepare app  
RUN mkdir -p /var/app/current  
WORKDIR /var/app/current  
  
RUN mkdir -p ${APP_UTILS_DIR}  
  
# install composer  
RUN mkdir -p /opt/composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/opt/composer/composer.phar  
COPY composer /usr/local/bin/composer  
RUN chmod 0755 /usr/local/bin/composer  
  
# add bootstrap  
COPY docker-entrypoint /usr/local/bin/docker-entrypoint  
RUN chmod 755 /usr/local/bin/docker-entrypoint  
  
# add hook run script  
COPY run-hooks /usr/local/bin/run-hooks  
RUN chmod 755 /usr/local/bin/run-hooks  
  
# add console  
COPY console /usr/local/bin/console  
RUN chmod 755 /usr/local/bin/console  
  
EXPOSE 9000  
CMD ["/usr/local/bin/docker-entrypoint"]  

