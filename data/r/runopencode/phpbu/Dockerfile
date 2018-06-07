FROM php:7.1.1  
  
#####################################################################################  
# #  
# Setup PHP & Extensions #  
# #  
#####################################################################################  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
xz-utils \  
wget \  
zip \  
git \  
autoconf \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt-dev \  
libbz2-dev \  
make \  
unzip \  
bzip2 \  
libicu-dev \  
mysql-client  
  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl intl && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-install opcache && \  
docker-php-ext-install mbstring pdo pdo_mysql zip  
  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
#####################################################################################  
# #  
# Setup PHPBU #  
# #  
#####################################################################################  
  
WORKDIR /tmp  
  
RUN curl -o /tmp/phpbu.phar https://phar.phpbu.de/phpbu.phar  
  
RUN mv /tmp/phpbu.phar /usr/local/bin/phpbu.phar && \  
ln -s /usr/local/bin/phpbu.phar /usr/local/bin/phpbu && \  
chmod +x /usr/local/bin/phpbu  
  
  
####################################################################################  
# #  
# Setup workspace dir #  
# #  
####################################################################################  
  
RUN rm -r /tmp/* && \  
cd / && \  
mkdir /workspace && \  
cd /workspace  
  
WORKDIR /workspace

