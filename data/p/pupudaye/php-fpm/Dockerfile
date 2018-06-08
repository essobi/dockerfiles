FROM bitnami/php-fpm:5.6  
MAINTAINER Waitfish <lipu8829@qq.com>  
RUN apt-get update  
RUN apt-get -y install gcc  
RUN apt-get -y install g++  
RUN apt-get -y install make  
RUN apt-get -y install m4  
RUN apt-get -y install autoconf  
ADD redis-3.1.4.tgz /opt/bitnami  
WORKDIR /opt/bitnami/redis-3.1.4  
RUN /opt/bitnami/php/bin/phpize  
RUN ./configure --with-php-config=/opt/bitnami/php/bin/php-config  
RUN make  
RUN make install  
  
WORKDIR /app  
ENTRYPOINT ["/app-entrypoint.sh"]  
CMD ["/run.sh"]  

