FROM php:7.2-apache  
LABEL maintainer="Rafael Souza Fijalkowski<rafaelsouzaf@gmail.com>"  
# This Dockerfile was based in Martin Helmich work: https://github.com/martin-
helmich/docker-typo3  
# Install TYPO3  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl git unzip vim wget \  
# Configure PHP  
libxml2-dev libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
zlib1g-dev \  
# Install required 3rd party tools  
graphicsmagick && \  
# Configure extensions  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli soap gd zip opcache && \  
echo 'always_populate_raw_post_data = -1\nmax_execution_time =
240\nmax_input_vars = 1500\nupload_max_filesize = 32M\npost_max_size = 32M' >
/usr/local/etc/php/conf.d/typo3.ini && \  
# Configure Apache as needed  
a2enmod rewrite && \  
apt-get clean && \  
apt-get -y purge \  
libxml2-dev libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* /usr/src/*  
  
WORKDIR /root  
ADD install-typo3.sh .  
VOLUME /var/www/html  
EXPOSE 80  

