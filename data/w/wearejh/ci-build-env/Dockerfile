FROM php:7.0-cli-alpine  
MAINTAINER Michael Woodward <michael@wearejh.com>  
  
RUN apk --update add \  
curl \  
git \  
knock \  
openssh \  
mysql-client \  
patch \  
rsync \  
libpng \  
libpng-dev \  
g++ \  
icu \  
icu-dev \  
libmcrypt-dev \  
libxslt-dev \  
libstdc++ \  
libgcc  
  
RUN docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
xsl \  
zip \  
soap \  
bcmath \  
mysqli \  
opcache \  
pcntl  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer global require wearejh/m2-deploy-recipe:dev-master  
  
RUN apk add nodejs  
RUN npm install -g yarn m2-builder@1  
  
RUN mkdir -p /root/build  
WORKDIR /root/build  
  
ENV PATH=/root/.composer/vendor/bin:$PATH  
  
RUN mkdir $HOME/.ssh  
COPY ./config/php.ini /usr/local/etc/php/conf.d/php-custom.ini  

