FROM centos:6  
MAINTAINER Carlos Vaz carlosjvaz@gmail.com  
  
# Update centos6  
RUN yum update -y  
  
# Add the ngix and PHP dependent repository  
ADD nginx.repo /etc/yum.repos.d/nginx.repo  
  
# Installing nginx  
RUN yum -y install nginx  
  
# Install php  
RUN yum -y --enablerepo=remi,remi-php53 install php php-fpm php-gd php-ldap \  
php-imap php-sqlite php-pgsql php-pear php-mysql php-mcrypt \  
php-xcache php-xml php-xmlrpc php-mbstring nkf html2text \  
php-cli php-mcrypt php-soap php-process php-devel  
  
# Install xdebug  
RUN yum -y install gcc  
RUN pecl install xdebug-2.2.7  
  
# Adding the configuration file of the nginx  
ADD conf.d/default.conf /etc/nginx/conf.d/default.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# suport ssl  
RUN mkdir /etc/nginx/ssl/  
ADD ssl/server.crt /etc/nginx/ssl/server.crt  
ADD ssl/server.key /etc/nginx/ssl/server.key  
  
# php settings  
RUN echo 'date.timezone="America/Sao_Paulo"' > /etc/php.d/timezone.ini  
RUN echo 'short_open_tag = On' > /etc/php.d/shortopentags.ini  
RUN sed -i 's/post_max_size = 8M/post_max_size = 64M/g' /etc/php.ini  
RUN sed -i 's/memory_limit = 128M/memory_limit = 256M/g' /etc/php.ini  
RUN sed -i 's/listen = 127.0.0.1:9000/listen = 9001/g' /etc/php-fpm.d/www.conf  
RUN sed -i '/^listen.allowed_clients/ s/^/;/' /etc/php-fpm.d/www.conf  
RUN echo "zend_extension = /usr/lib64/php/modules/xdebug.so" >
/etc/php.d/xdebug.ini  
RUN echo "xdebug.remote_port=9000" >> /etc/php.d/xdebug.ini  
RUN echo "xdebug.remote_enable=on" >> /etc/php.d/xdebug.ini  
RUN echo "xdebug.remote_autostart=off" >> /etc/php.d/xdebug.ini  
RUN echo "xdebug.remote_connect_back = 1" >> /etc/php.d/xdebug.ini  
RUN echo "xdebug.remote_log=/var/log/xdebug.log" >> /etc/php.d/xdebug.ini  
  
# Install other utilites  
RUN yum -y install zip  
  
# Clean up YUM when done.  
RUN yum clean -y all  
  
# Install phpunit  
RUN yum -y install wget  
RUN wget -O phpunit.phar https://phar.phpunit.de/phpunit-old.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
# shared folders  
VOLUME ["/var/www/html"]  
  
# nginx  
EXPOSE 80 443  
CMD service php-fpm start && nginx  

