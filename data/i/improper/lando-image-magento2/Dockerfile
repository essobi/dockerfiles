FROM devwithlando/php:7.1-fpm  
  
RUN phpExtDependencies="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev
libfreetype6 libturbojpeg1 libjpeg62-turbo-dev libpng12-dev libfreetype6-dev
libicu-dev libxslt1-dev" \  
&& apt-get update \  
&& apt-get install -y $phpExtDependencies \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-install soap \  
&& noLongerNeeded="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev
libfreetype6-dev libjpeg62-turbo-dev" \  
&& apt-get purge --auto-remove -y $noLongerNeeded  

