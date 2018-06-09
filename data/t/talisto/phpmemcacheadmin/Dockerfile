FROM php:7.1-alpine  
  
MAINTAINER Talisto <https://github.com/talisto>  
  
RUN apk --update add autoconf g++ make libtool wget tar gzip \  
libmemcached-dev libmemcached libmemcached-libs cyrus-sasl-dev zlib-dev  
RUN pecl install memcached  
RUN docker-php-ext-enable memcached  
  
RUN cd /tmp && \  
wget https://github.com/elijaa/phpmemcachedadmin/archive/1.3.0.tar.gz && \  
tar zxvf 1.3.0.tar.gz && \  
rm 1.3.0.tar.gz  
RUN mkdir -p /var/www  
RUN cp -r /tmp/phpmemcachedadmin-1.3.0/* /var/www  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV MEMCACHE_HOST memcache  
ENV MEMCACHE_PORT 11211  
COPY config.php /var/www/Config/Memcache.php  
  
EXPOSE 9083  
CMD ["php", "-S", "0.0.0.0:9083", "-t", "/var/www"]  

