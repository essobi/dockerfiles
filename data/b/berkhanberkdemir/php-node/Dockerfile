FROM php:7.1-cli  
  
RUN apt-get update -yqq -q=2 \  
&& apt-get install -yqq -q=2 \  
libicu-dev \  
libxml2-dev \  
libxslt-dev \  
libmcrypt-dev \  
zlib1g-dev \  
libcurl3-dev \  
make g++ libssl-dev wget python  
  
RUN wget --quiet "https://nodejs.org/dist/v8.9.4/node-v8.9.4.tar.gz" \  
&& tar -xvf "node-v8.9.4.tar.gz" \  
&& cd node-v8.9.4 \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install -j$(nproc) \  
&& node -v \  
&& npm -v  
  
# `curl, dom, pdo, posix, simplexml` already loaded  
  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-install -j$(nproc) \  
intl \  
xmlrpc \  
xsl \  
pdo_mysql \  
mcrypt \  
zip \  
&& docker-php-ext-enable opcache \  
&& curl -sS "https://getcomposer.org/installer" | php -- --install-
dir=/usr/local/bin --filename=composer  

