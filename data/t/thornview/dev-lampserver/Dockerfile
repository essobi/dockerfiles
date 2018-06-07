FROM php:7.1-apache-jessie  
MAINTAINER Bryce Embry <bryce@thornview.com>  
RUN apt-get update  
  
# Basics  
RUN apt-get install -y vim apt-utils  
  
# MySQL  
# TODO: Change "MyFancyPassword" for a different MySQL password  
RUN echo "mysql-server-5.5 mysql-server/root_password_again password
MyFancyPassword" | debconf-set-selections  
RUN echo "mysql-server-5.5 mysql-server/root_password password
MyFancyPassword" | debconf-set-selections  
RUN apt-get install -y mysql-client mysql-server  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
  
# Add Xdebug  
RUN pecl install xdebug-2.5.0  
RUN docker-php-ext-enable xdebug  
  
RUN sed -i '$ a\xdebug.remote_enable = 1' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN sed -i '$ a\xdebug.remote_connect_back = 0'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '$ a\xdebug.profiler_enable_trigger = 1'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '$ a\xdebug.trace_enable_trigger = 1'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '$ a\xdebug.trace_format = 1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '$ a\xdebug.idekey = "XSTORM"' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#TODO: Replace the IP below with your local IP address so xdebug can
communicate outside Docker  
RUN sed -i '$ a\xdebug.remote_host = 10.151.18.32'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
# Expose ports  
EXPOSE 80 3306  
# Start services  
CMD /etc/init.d/mysql start && /usr/local/bin/apache2-foreground && /bin/bash  
  
# To Build:  
# docker build -t dev-lampserver ./  
# To Run:  
# TODO: replace directory with your own directory  
# docker run -i -t -d --rm --name dev-lampserver -v
C:\Users\embryb\dev\webserver:/var/www/html -p 127.0.0.1:80:80 dev-lampserver  
#  
# -i = keep stdin open, even if not attached  
# -t = allocate a pseudo-TTY  
# -d = run container in background  
# --rm = automatically remove container on exit  
# --name = container name  
# -v = volume to mount (local:docker)  
# -p = public containers ports to host  
# For PHPMyAdmin  
# Download into the mapped directory.  
# On default PHPMyAdmin download, rename `config.sample.inc.php` to
`config.inc.php`  

