FROM php:7.2-rc  
  
RUN apt-get update  
  
RUN apt-get install -y \  
libcurl4-openssl-dev \  
sudo \  
git \  
libxslt-dev \  
mercurial \  
subversion \  
zlib1g-dev \  
graphviz \  
zip \  
libicu-dev \  
g++ \  
libpcre3-dev \  
libgd-dev \  
libfreetype6-dev \  
libgmp-dev  
  
RUN apt-get clean  
  
RUN docker-php-ext-install \  
soap \  
gmp \  
dom \  
bcmath \  
zip \  
xsl \  
mbstring \  
gettext \  
curl \  
pdo_mysql \  
json \  
intl \  
opcache \  
mysqli  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \--with-png-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& pecl install ds  
  
RUN echo "extension=ds.so" >> /usr/local/etc/php/php.ini  
  
RUN echo "memory_limit = 512M\n" > /usr/local/etc/php/conf.d/uploads.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

