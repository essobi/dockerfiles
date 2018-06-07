FROM php:7.1.13-fpm  
  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
git \  
vim \  
wget \  
lynx \  
psmisc \  
bzip2 \  
cron \  
supervisor \  
&& apt-get clean  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/; \  
docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
xsl \  
zip \  
opcache \  
soap \  
bcmath  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=1.1.2  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs  
  
# Install MageRun for M2  
RUN cd /usr/local/bin && \  
wget https://files.magerun.net/n98-magerun2.phar && \  
chmod +x ./n98-magerun2.phar  
  
# Install Imagemagic  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libmagickwand-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick  

