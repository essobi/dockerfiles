FROM ubuntu:16.04  
  
MAINTAINER Nguyen Huu Kim <kimnguyen.ict@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common locales  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y php5.6 \--force-yes  
  
RUN apt-get install -y --force-yes \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-dev \  
php5.6-gd \  
php5.6-gmp \  
php5.6-json \  
php5.6-ldap \  
php5.6-mysql \  
php5.6-odbc \  
php5.6-opcache \  
php5.6-pgsql \  
php5.6-pspell \  
php5.6-readline \  
php5.6-recode \  
php5.6-snmp \  
php5.6-sqlite3 \  
php5.6-tidy \  
php5.6-xml \  
php5.6-xmlrpc \  
php5.6-bcmath \  
php5.6-bz2 \  
php5.6-enchant \  
php5.6-fpm \  
php5.6-imap \  
php5.6-interbase \  
php5.6-intl \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-phpdbg \  
php5.6-soap \  
php5.6-sybase \  
php5.6-xsl \  
php5.6-zip \  
php5.6-dba \  
libmcrypt-dev \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
sqlite3 \  
libsqlite3-dev \  
git \  
curl \  
vim \  
nano \  
net-tools \  
pkg-config \  
iputils-ping  
  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN echo "export
PATH=${PATH}:/var/www/workspace/vendor/bin:/root/.composer/vendor/bin" >>
~/.bashrc  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g yarn gulp-cli  
  
WORKDIR /var/www/workspace  

