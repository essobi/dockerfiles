FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y curl openssl  
RUN curl http://uk1.php.net/distributions/php-5.6.30.tar.gz -o
/usr/src/php-5.6.30.tar.gz && \  
cd /usr/src && \  
tar -zxvf php-5.6.30.tar.gz  
RUN apt-get update && apt-get install -y build-essential libxml2-dev
libcurl4-openssl-dev sendmail  
  
WORKDIR /usr/src/php-5.6.30  
  
COPY ["config.nice", "config.nice"]  
  
RUN ./config.nice && make install  
  
RUN apt-get update && apt-get install -y git mysql-client-5.5  
  
RUN apt-get remove -y build-essential libxml2-dev libcurl4-openssl-dev && rm
-rf /var/lib/apt/lists/*  
  
RUN cd /usr/bin && ln -s /usr/local/php-5.6.30/bin/php .  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www  
  
CMD ["/usr/local/php-5.6.30/sbin/php-fpm", "-F"]  

