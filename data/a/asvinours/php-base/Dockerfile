FROM php:5.6-fpm  
  
# Get repository and install wget and vim  
RUN apt-get update && apt-get install --no-install-recommends -y \  
curl \  
wget \  
vim \  
git \  
unzip \  
gettext \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libicu-dev \  
libcurl4-openssl-dev \  
g++ \  
unixodbc-dev \  
libxml2-dev \  
libaio-dev \  
libmemcached-dev \  
freetds-dev \  
mediainfo \  
libpq-dev \  
locales \  
ssh  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& git clone https://github.com/phpredis/phpredis /usr/src/php/ext/redis \  
&& cd /usr/src/php/ext/redis && git checkout 3.1.1 \  
&& docker-php-ext-configure redis \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsq \  
&& docker-php-ext-install -j4 \  
iconv \  
mbstring \  
intl \  
mcrypt \  
shmop \  
gd \  
mysqli \  
pdo_mysql \  
zip \  
redis \  
pcntl \  
simplexml \  
curl \  
json \  
fileinfo \  
bcmath \  
opcache \  
pdo_pgsql \  
pgsql \  
gettext \  
&& pear install Crypt_HMAC2  
  
COPY locale.gen /etc/locale.gen  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN locale-gen  
  
COPY php.ini /usr/local/etc/php/  
  
CMD ["/bin/true"]  

