FROM ubuntu  
MAINTAINER Christian Lück <christian@lueck.tv>  
  
RUN apt-get update && apt-get install -y unzip php5-cli  
  
ADD https://github.com/clue/php-redis-server/archive/master.zip /php-redis-
server.zip  
RUN unzip php-redis-server.zip && mv php-redis-server-master php-redis-server  
WORKDIR php-redis-server  
  
ADD https://getcomposer.org/composer.phar /php-redis-server/composer.phar  
RUN php composer.phar install  
  
USER nobody  
EXPOSE 6379  
CMD php bin/redis-server.php  

