FROM zterry95/docker-php7:7.1-base  
  
RUN apt-get clean -y  
RUN apt-get update  
RUN apt-get install -y unzip  
RUN apt-get install libaio-dev -y  
# Oracle instantclient  
ADD oracle/instantclient-basic-linux.x64-11.2.0.4.0.zip /tmp/instantclient-
basic-linux.x64-11.2.0.4.0.zip  
ADD oracle/instantclient-sdk-linux.x64-11.2.0.4.0.zip /tmp/instantclient-sdk-
linux.x64-11.2.0.4.0.zip  
ADD oracle/instantclient-sqlplus-linux.x64-11.2.0.4.0.zip /tmp/instantclient-
sqlplus-linux.x64-11.2.0.4.0.zip  
  
RUN unzip /tmp/instantclient-basic-linux.x64-11.2.0.4.0.zip -d /usr/local/  
RUN unzip /tmp/instantclient-sdk-linux.x64-11.2.0.4.0.zip -d /usr/local/  
RUN unzip /tmp/instantclient-sqlplus-linux.x64-11.2.0.4.0.zip -d /usr/local/  
RUN ln -s /usr/local/instantclient_11_2 /usr/local/instantclient  
RUN ln -s /usr/local/instantclient/libclntsh.so.11.1
/usr/local/instantclient/libclntsh.so  
RUN ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus  
  
RUN echo 'instantclient,/usr/local/instantclient' | pecl install oci8  
  
ADD php/oci8.ini /usr/local/etc/php/conf.d/oci8.ini  
  
# Install Memcached  
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-
dev/php-memcached/archive/php7.tar.gz" && \  
mkdir -p memcached && \  
tar -C memcached -zxvf /tmp/memcached.tar.gz --strip 1 && \  
( \  
cd memcached && \  
phpize && \  
./configure && \  
make -j$(nproc) && \  
make install \  
) && \  
rm -r memcached && \  
rm /tmp/memcached.tar.gz && \  
docker-php-ext-enable memcached  
  
# Install redis  
RUN pecl install redis -y && docker-php-ext-enable redis  
VOLUME /app/web  
WORKDIR /app/web  

