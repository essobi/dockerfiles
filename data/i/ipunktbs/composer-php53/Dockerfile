FROM tomsowerby/php-5.3:cli  
RUN apt-get update && apt-get -y install zlib1g-dev unzip libmcrypt-dev \  
libmysqlclient-dev \  
&& pecl install zip \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-enable zip  

