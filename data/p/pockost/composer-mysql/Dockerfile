FROM pockost/composer  
RUN docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd \  
&& docker-php-ext-install pdo_mysql mysqli  
  
RUN echo "memory_limit = 2048M" > /usr/local/etc/php/conf.d/memory.ini  
  

