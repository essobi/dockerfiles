FROM edusca/docker-nginx-fpm-php5.6  
MAINTAINER Eduardo Scarello <eduardo.scarello@gmail.com>  
  
#Install mongdb driver dependencies for PHP  
RUN apt-get update  
RUN apt-get install -y autoconf g++ make openssl libssl-dev libcurl4-openssl-
dev  
RUN apt-get install -y libcurl4-openssl-dev pkg-config  
RUN apt-get install -y libsasl2-dev  
  
#Install php-dev allowing the use of phpize  
RUN apt-get install -y php5.6-dev  
  
#Crete the directpry for keep the PHP modules  
RUN mkdir /usr/lib/php/5.6/extensions  
  
#install mongo PHP module  
RUN cd /tmp  
RUN curl -O https://pecl.php.net/get/mongodb-1.1.8.tgz  
RUN tar -xzvf mongodb-1.1.8.tgz  
RUN cd mongodb-1.1.8 && phpize && ./configure && make && make install  
RUN mv mongodb-1.1.8/modules/mongodb.so /usr/lib/php/5.6/extensions/mongodb.so  
RUN echo "extension=/usr/lib/php/5.6/extensions/mongodb.so" >>
/etc/php/5.6/cli/php.ini  
  
#install gearman extension  
RUN apt-get install -y libgearman-dev  
RUN cd /tmp  
RUN curl -O https://pecl.php.net/get/gearman-1.1.2.tgz  
RUN tar -xzvf gearman-1.1.2.tgz  
RUN cd gearman-1.1.2 && phpize && ./configure && make && make install  
RUN mv gearman-1.1.2/modules/gearman.so /usr/lib/php/5.6/extensions/gearman.so  
RUN echo "extension=/usr/lib/php/5.6/extensions/gearman.so" >>
/etc/php/5.6/cli/php.ini  

