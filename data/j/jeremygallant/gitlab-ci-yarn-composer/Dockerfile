FROM ubuntu:16.04  
RUN export LC_ALL=C.UTF-8  
RUN DEBIAN_FRONTEND=noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ARG COMPOSER_VERSION=1.5.2  
ENV COMPOSER_HOME /composer  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN apt-get update  
RUN apt-get install -y \  
autoconf \  
autogen \  
language-pack-en-base \  
wget \  
curl \  
rsync \  
ssh \  
openssh-client \  
git \  
build-essential \  
apt-utils \  
software-properties-common \  
python-software-properties \  
nasm \  
libjpeg-dev \  
libpng-dev  
  
RUN wget -q -O /tmp/libpng12.deb
http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
\  
&& dpkg -i /tmp/libpng12.deb \  
&& rm /tmp/libpng12.deb  
  
# PHP  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && apt-get update &&
apt-get install -y php7.1  
RUN apt-get install -y \  
php7.1-curl \  
php7.1-gd \  
php7.1-dev \  
php7.1-xml \  
php7.1-bcmath \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-zip \  
php7.1-sqlite \  
php7.1-soap \  
php7.1-json \  
php7.1-intl \  
php7.1-imap \  
php-xdebug \  
php-memcached  
RUN command -v php  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer --version=${COMPOSER_VERSION}  
  
# PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
RUN command -v phpunit  
  
# Node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh  
RUN bash nodesource_setup.sh  
RUN apt-get install nodejs -y  
RUN command -v node  
RUN command -v npm  
  
# Yarn  
RUN npm install yarn -g  
  
# Newman  
ENV NEWMAN_VERSION 3.9.3  
RUN npm install -g newman@${NEWMAN_VERSION};  
  
# Other  
RUN mkdir ~/.ssh

