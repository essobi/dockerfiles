FROM php:fpm  
LABEL maintainer="Luiz Benevenuto <luiz@siffra.com.br>"  
  
# Install modules  
RUN buildDeps="libpq-dev libzip-dev libicu-dev xml2 libxml2-dev git curl ssh-
client libmagickwand-dev gnupg2 sudo yarn" && \  
apt-get update && \  
apt-get install -fy $buildDeps \--no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
pecl install imagick && \  
docker-php-ext-install \  
zip \  
gd \  
mbstring \  
tokenizer \  
xml \  
pdo \  
pdo_pgsql \  
pgsql \  
sockets \  
intl \  
pcntl && \  
docker-php-ext-enable imagick  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php --install-dir=/bin --filename=composer  
RUN composer global require deployer/deployer deployer/recipes  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get update && \  
apt-get install -fy nodejs --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
apt autoremove -fy

