ARG BASE_IMAGE=php:7.0  
FROM ${BASE_IMAGE}  
MAINTAINER Kang Ki Tae <kt.kang@ridi.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN docker-php-source extract \  
# Install common  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget software-properties-common openssh-client git mysql-client zlib1g-dev
libmcrypt-dev libldap2-dev \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap zip mysqli pdo pdo_mysql \  
# Install mysql  
&& apt-get install mysql-server -y \  
&& sed -i 's/127\\.0\\.0\\.1/0\\.0\\.0\\.0/g' /etc/mysql/my.cnf \  
&& sed -i '/max_connections/a max_connections = 3000' /etc/mysql/my.cnf \  
# Install xdebug php extention  
&& pecl config-set preferred_state beta \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear \  
&& pecl config-set preferred_state stable \  
# Install node && bower  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install nodejs -y \  
&& npm install -g bower \  
  
# Install composer  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer \  
# Install newman (Postman test runner)  
&& npm install newman --global \  
# Clean  
&& apt-get autoclean -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \  
&& docker-php-source delete  

