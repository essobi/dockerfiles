  
FROM php:5.6-cli  
  
#update repo  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
libmagickwand-dev \  
imagemagick \  
wget \  
curl \  
git \  
jq \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install pcntl \  
&& pecl install imagick \  
&& pecl install xdebug \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-enable pcntl \  
&& curl https://sdk.cloud.google.com | bash  
  
RUN apt-get install -y \  
libpq-dev \  
postgresql-client  
  
RUN docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_mysql  
  
RUN docker-php-ext-install pgsql pdo_pgsql  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/  
  
env PATH /root/google-cloud-sdk/bin:$PATH  
  
#Download dependencies  
# Set memory limit  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
# Set environmental variables  
ENV COMPOSER_HOME /root/composer  
  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /root/google-cloud-sdk/bin/gcloud components update kubectl  
  
RUN docker-php-ext-install \  
zip \  
bz2 \  
mbstring \  
pdo_mysql \  
bcmath  
  
CMD ["php"]  

