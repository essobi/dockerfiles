FROM phusion/baseimage:latest  
  
MAINTAINER Matt Alford <malford@nsgdv.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
# Add the "PHP 7" ppa  
RUN add-apt-repository -y \  
ppa:ondrej/php  
  
# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT  
RUN apt-get update && apt-get install -y --force-yes \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-gmp \  
php7.1-json \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-zip \  
php7.1-memcached \  
php7.1-gd \  
php7.1-xdebug \  
php-dev \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
git \  
curl \  
node-gyp \  
python2.7 \  
gcc \  
nano  
  
# Clean up, to free some space  
RUN apt-get clean  
  
# Add bin folder of composer to PATH.  
RUN echo "export PATH=${PATH}:/var/www/app/vendor/bin" >> ~/.bashrc  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Source the bash  
RUN . ~/.bashrc  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/app  

