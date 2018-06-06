FROM ubuntu:16.04  
RUN apt-get -y update && apt-get install -y curl openssh-client expect  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN builderDeps=" \  
git-ftp \  
sshpass \  
php \  
php-mbstring \  
php-gd \  
php-zip \  
php-xml \  
php-cli \  
php-curl \  
nodejs \  
build-essential \  
" \  
&& apt-get install -y $builderDeps \--no-install-recommends  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN adduser --disabled-password --gecos '' builder  
USER builder  
WORKDIR /home/builder  
RUN mkdir ~/.npm-global  
RUN npm config set prefix '~/.npm-global'  
RUN export PATH=~/.npm-global/bin:$PATH  
RUN npm install -g webpack  
RUN composer global require "phpunit/phpunit=5.5.*"

