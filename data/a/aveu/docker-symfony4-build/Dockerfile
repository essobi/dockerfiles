FROM php:7.1  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
lftp \  
zip \  
unzip \  
nodejs \  
apt-transport-https \  
yarn \  
zlib1g-dev \  
&& docker-php-ext-install pdo_mysql zip  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

