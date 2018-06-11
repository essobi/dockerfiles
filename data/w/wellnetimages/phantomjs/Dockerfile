FROM php:7.0.7-fpm  
  
# Install extensions.  
RUN apt-get update && apt-get install --no-install-recommends --force-yes -y \  
fontconfig \  
bzip2 \  
unzip \  
libcurl3 \  
libcurl4-gnutls-dev \  
libxml2-dev \  
wget \  
&& docker-php-ext-install mbstring json curl xml \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/local  
  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar -xvf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& mv phantomjs-2.1.1-linux-x86_64 phantomjs  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN composer require behat/mink:~1.6  
RUN composer require jcalderonzumba/gastonjs:^1.1@dev  
RUN composer require jcalderonzumba/mink-phantomjs-driver:~0.3.1  
  
CMD ["/usr/local/phantomjs/bin/phantomjs", "--ssl-protocol=any", "--ignore-
ssl-errors=true", "./vendor/jcalderonzumba/gastonjs/src/Client/main.js",
"8510", "1024", "768"]  

