FROM perceptive/docker-php53  
  
RUN apt-get update && apt-get install -y freetds-dev locate  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/libsybdb.so &&
ldconfig -v  
RUN ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a && ldconfig
-v  
  
RUN apt-get update && apt-get install -y \  
curl \  
zlib1g-dev \  
mysql-client \  
&& docker-php-ext-configure sybase_ct --with-sybase-ct=shared,/usr \  
&& docker-php-ext-install pdo_dblib \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mssql \  
&& docker-php-ext-install soap  
  
RUN docker-php-ext-install curl  
  
ADD php.ini /usr/local/etc/php  
RUN a2enmod rewrite  
  
ADD site-optimus.conf /etc/apache2/sites-available  
RUN a2dissite 000-default.conf  
RUN a2ensite site-optimus.conf  
  

