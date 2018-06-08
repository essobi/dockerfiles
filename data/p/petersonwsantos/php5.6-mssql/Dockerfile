FROM php:5.6-apache  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
zlib1g-dev \  
freetds-dev \  
freetds-bin \  
freetds-common \  
libdbd-freetds \  
libsybdb5 \  
libqt4-sql-tds \  
libqt5sql5-tds \  
libqxmlrpc-dev \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/libsybdb.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a \  
&& docker-php-ext-install mssql \  
&& docker-php-ext-configure mssql \  
&& chmod 755 /var/www/html -R \  
&& chown www-data:www-data /var/www/html  
COPY conf/php.ini /usr/local/etc/php/  
COPY conf.d/ /usr/local/etc/php/conf.d/  

