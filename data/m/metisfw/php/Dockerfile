FROM php:5.4-cli  
  
RUN curl \--silent --location https://deb.nodesource.com/setup_0.12 | bash -  
  
RUN apt-get update  
  
RUN buildDeps=" \  
libfreetype6-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libcurl4-gnutls-dev \  
libpq-dev \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& docker-php-ext-configure gd \--enable-gd-native-ttf --with-jpeg-
dir=/usr/lib/x86_64-linux-gnu --with-png-dir=/usr/lib/x86_64-linux-gnu --with-
freetype-dir=/usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap \--with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install tokenizer \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install calendar \  
&& docker-php-ext-install fileinfo \  
&& docker-php-ext-install json \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install bcmath \  
&& apt-get purge -y \--auto-remove $buildDeps \  
&& cd /usr/src/php \  
&& make clean  
  
RUN apt-get install -y git nodejs ssh mysql-client libfreetype6
libjpeg62-turbo libmcrypt4 libpng12-0 libpq5 sendmail imagemagick \--no-
install-recommends && rm -rf /var/lib/apt/lists/*  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
  
RUN curl -sS https://getcomposer.org/installer | php \-- --install-
dir=/usr/local/bin --filename=composer  

