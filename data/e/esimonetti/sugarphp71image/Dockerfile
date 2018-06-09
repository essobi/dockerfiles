FROM debian:9.2  
MAINTAINER enrico.simonetti@gmail.com  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
curl \  
apt-transport-https \  
lsb-release \  
ca-certificates  
RUN curl -sS https://packages.sury.org/php/apt.gpg -o
/etc/apt/trusted.gpg.d/php.gpg  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
apache2 \  
php7.1-curl \  
php7.1-gd \  
php7.1-bcmath \  
php7.1-mbstring \  
php7.1-imap \  
php7.1-zip \  
php7.1-ldap \  
php7.1 \  
php7.1-dev \  
php7.1-mcrypt \  
php7.1-redis \  
php7.1-mysql \  
php7.1-xml \  
php7.1-xdebug \  
php7.1-tideways \  
php7.1-gmp \  
&& update-alternatives --set php /usr/bin/php7.1  
RUN apt-get purge -y \  
php7.2-cli \  
php7.2-common \  
php7.2-json \  
php7.2-opcache \  
php7.2-phpdbg \  
php7.2-readline \  
&& apt-get autoclean && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*  

