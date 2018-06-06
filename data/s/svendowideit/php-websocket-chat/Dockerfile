FROM svendowideit/php:5-sockets  
MAINTAINER Sven Dowideit <SvenDowideit@home.org.au>  
  
RUN apt-get update \  
&& apt-get install -y vim git \  
&& rm -r /var/lib/apt/lists/*  
  
WORKDIR /var/www/html/  
  
# process the composer.json  
COPY composer.json /var/www/html/  
  
# pre-reqs for predis/predis-async  
#RUN apt-get update \  
# && apt-get install -y libhiredis-dev \  
# && rm -r /var/lib/apt/lists/*  
#RUN cd /tmp && git clone https://github.com/nrk/phpiredis.git \  
# && cd phpiredis \  
# && phpize && ./configure --enable-phpiredis \  
# && make && make install  
RUN composer install  
  
COPY . /var/www/html/  
  
#CMD ["/var/www/html/start.sh"]  
CMD ["php", "server.php"]  

