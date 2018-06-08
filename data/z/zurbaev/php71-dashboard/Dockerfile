FROM phusion/baseimage:latest  
  
MAINTAINER Timur Zurbaev <zurbaev@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update && \  
apt-get install -y --force-yes \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-json \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-sqlite \  
php7.1-sqlite3 \  
php7.1-zip \  
php7.1-bcmath \  
php7.1-memcached \  
php7.1-gd \  
php7.1-dev \  
pkg-config \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
libsqlite3-dev \  
sqlite3 \  
git \  
curl \  
nano \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -s http://getcomposer.org/installer | php && \  
chmod a+x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
RUN curl -O -L https://phar.phpunit.de/phpunit.phar && \  
chmod a+x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
RUN curl -O -L http://get.sensiolabs.org/php-cs-fixer.phar && \  
chmod a+x php-cs-fixer.phar && \  
mv php-cs-fixer.phar /usr/local/bin/php-cs-fixer  

