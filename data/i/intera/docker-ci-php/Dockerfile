FROM ubuntu:16.04  
  
COPY install_composer.sh /tmp/install_composer.sh  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
php-apcu \  
php-cli \  
php-curl \  
php-gd \  
php-igbinary \  
php-intl \  
php-json \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-pgsql \  
php-soap \  
php-sqlite3 \  
php-xdebug \  
php-xml \  
php-zip \  
imagemagick \  
language-pack-de \  
wget \  
git \  
  
&& bash /tmp/install_composer.sh \  
&& mv composer.phar /usr/local/bin/ \  
  
&& apt-get --purge autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

