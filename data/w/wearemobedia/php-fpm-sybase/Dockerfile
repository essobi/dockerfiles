FROM wearemobedia/php-fpm:5.6-1.2.0  
  
RUN apt-get update && apt-get install -y freetds-common freetds-bin freetds-
dev unixodbc \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/libsybdb.so  
# install the PHP extensions we need  
RUN docker-php-ext-configure sybase_ct --with-sybase-ct=/usr \  
&& docker-php-ext-install -j "$(nproc)" sybase_ct pdo_dblib  

