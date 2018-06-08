FROM php:7-fpm  
MAINTAINER pythias <pythias@gmail.com>  
  
# nginx  
RUN apt-get update && apt-get install -y nginx  
RUN mkdir -p /var/log/www  
RUN mkdir -p /var/log/nginx  
RUN mkdir -p /var/data  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/vhost.conf /etc/nginx/conf.d/vhost.conf  
  
# supervisor  
RUN apt-get install -y supervisor wget unzip  
RUN mkdir -p /var/log/supervisor  
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# redis  
RUN wget http://download.redis.io/releases/redis-3.2.1.tar.gz -O
/home/redis-3.2.1.tar.gz  
RUN cd /home && tar xzf redis-3.2.1.tar.gz && cd redis-3.2.1 && make && make
install  
RUN rm -f /home/redis-3.2.1.tar.gz  
COPY conf/redis.conf /etc/redis.conf  
  
# redis ext  
RUN wget https://pecl.php.net/get/redis-3.0.0.tgz -O /home/redis-3.0.0.tgz  
RUN pecl install /home/redis-3.0.0.tgz  
RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
RUN rm -f /home/redis-3.0.0.tgz  
  
# yaf ext  
RUN wget https://pecl.php.net/get/yaf-3.0.3.tgz -O /home/yaf-3.0.3.tgz  
RUN pecl install /home/yaf-3.0.3.tgz  
RUN echo "extension=yaf.so" > /usr/local/etc/php/conf.d/yaf.ini  
RUN rm -f /home/yaf-3.0.3.tgz  
  
# pcntl ext  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install sockets  
  
# composer  
RUN wget https://getcomposer.org/download/1.2.0/composer.phar -O
/usr/local/bin/composer  
RUN chmod 755 /usr/local/bin/composer  
  
# htdocs  
RUN wget https://codeload.github.com/pythias/mock.server/zip/master -O
/home/mock.server-master.zip  
RUN unzip /home/mock.server-master.zip -d /home && rm -f /home/mock.server-
master.zip && cp -r /home/mock.server-master/* /var/www/html/  
#RUN git clone https://github.com/pythias/mock.server /var/www/html/  
RUN cd /var/www/html/ && composer install --no-plugins --no-scripts &&
composer update --no-plugins --no-scripts  
  
# daemons  
COPY daemons.sh /usr/local/bin/daemons.sh  
RUN chmod 755 /usr/local/bin/daemons.sh  
  
EXPOSE 9000 6379 80  
WORKDIR /var/www/html/  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

