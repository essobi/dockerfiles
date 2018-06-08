FROM php:7.1-fpm  
  
MAINTAINER "Marc Geurts <geurtsmarc@hotmail.com>"  
RUN apt-get update \  
&& apt-get install -y \  
libpq-dev \  
libzip-dev \  
nano \  
zip \  
unzip \  
vim \  
wget \  
curl \  
git \  
mysql-client \  
moreutils \  
dnsutils \  
zlib1g-dev \  
libicu-dev \  
libmemcached-dev \  
g++ \  
libc-client-dev \  
ssh \  
libkrb5-dev --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Run docker-php-ext-install for available extensions  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-install pdo pdo_mysql opcache zip bcmath intl  
  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap  
  
# Install xdebug  
RUN pecl install -o -f redis  
RUN pecl install xdebug  
RUN docker-php-ext-enable redis xdebug \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back = 1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.idekey = \"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.remote_port = 9001" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& \  
rm -rf /tmp/pear  
  
# Copy php.ini  
COPY php-custom.ini /usr/local/etc/php/conf.d/php-custom.ini  
  
# Set your timezone here  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
RUN "date"  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get autoremove -y  
  
# Set enviroments  
ENV MYSQL_ROOT_USER=root  
ENV MYSQL_ROOT_PASSWORD=propertywindow  
  
# Set rights  
RUN useradd -ms /bin/bash vagrant  
CMD php-fpm -F  
USER vagrant  
  
# Add Symfony alias  
RUN echo 'alias sf="php app/console"' >> ~/.bashrc  
RUN echo 'alias ll="ls -lah"' >> ~/.bashrc  
#RUN echo " StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
WORKDIR /app  

