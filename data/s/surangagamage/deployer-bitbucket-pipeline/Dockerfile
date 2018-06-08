FROM ubuntu:16.04  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -q -y php7.0 \  
php7.0-fpm \  
imagemagick \  
php-memcached \  
php7.0-soap \  
php7.0-cli \  
php7.0-curl \  
php7.0-dev \  
php7.0-gd \  
php7.0-mcrypt \  
php7.0-zip \  
php7.0-xsl \  
php7.0-odbc \  
php7.0-mbstring \  
php-pear \  
php7.0-intl \  
php7.0-mysql \  
php-imagick \  
openssh-client \  
git \  
python-software-properties  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -q -y nodejs  
  
RUN npm install -g bower  
  
# Composer  
ENV COMPOSER_VERSION 1.3.2  
RUN curl -sSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
# Deployer  
RUN curl -L https://deployer.org/releases/v4.3.0/deployer.phar -o
/usr/local/bin/dep  
  
# Make all binaries executable  
RUN chmod +x /usr/local/bin/*  
  
CMD ["php-fpm7.0"]

