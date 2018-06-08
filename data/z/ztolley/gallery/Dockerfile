FROM ubuntu:trusty  
MAINTAINER Zac Tolley <zac@thetolleys.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git curl apache2 libapache2-mod-php5 php5-curl
mysql-server php5-mysql pwgen php-apc php5-mcrypt php5-imagick && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Add image configuration and scripts  
ADD docker/start-apache2.sh /start-apache2.sh  
ADD docker/start-mysqld.sh /start-mysqld.sh  
ADD docker/run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD docker/my.cnf /etc/mysql/conf.d/my.cnf  
ADD docker/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-
apache2.conf  
ADD docker/supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-
mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL utils  
ADD docker/create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD docker/createdb.sh /createdb.sh  
RUN chmod 755 /*.sh  
  
# config to enable .htaccess  
ADD docker/apache_symfony /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# load the app into /app folder and link into apache  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD . /app  
RUN mkdir /app/web/uploads | true  
RUN mkdir /app/app/cache | true  
RUN mkdir /app/app/logs | true  
  
RUN chmod a+rw /app/app/logs  
RUN chmod a+rw /app/app/cache  
RUN chmod a+rw /app/web/uploads  
  
RUN rm -f /app/app/config/parameters.yml  
RUN rm -rf /app/app/cache/*  
RUN rm -rf /app/app/logs/*  
  
WORKDIR /app  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer install --prefer-dist  
  
# Install bower and get bower dependencies  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g bower  
RUN npm install -g browserify  
run npm install -g watchify  
  
# Assets  
RUN bower install --allow-root  
  
#Enviornment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/app/web/uploads" ]  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

