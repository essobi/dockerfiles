FROM ubuntu:bionic  
  
MAINTAINER "Vitor Carreira" <vitor.carreira@gmail.com>  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
software-properties-common  
  
# Common PHP pages across containers  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
zip \  
unzip \  
php7.2-cli \  
php7.2-mysqlnd \  
php7.2-apcu \  
php7.2-memcached \  
php7.2-imap \  
php7.2-pgsql \  
php7.2-intl \  
php7.2-mbstring \  
php7.2-redis \  
php7.2-mongo \  
php7.2-sqlite \  
php7.2-curl \  
php7.2-json \  
php7.2-ssh2 \  
php7.2-gd \  
php7.2-gmp \  
php7.2-zip \  
php7.2-bcmath \  
php7.2-soap \  
php-pear \  
php7.2-dev make \  
wget \  
git \  
curl && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["php", "-a"]  

