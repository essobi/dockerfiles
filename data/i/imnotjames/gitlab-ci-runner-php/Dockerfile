FROM ubuntu:17.04  
MAINTAINER James Ward <james@notjam.es>  
  
ENV HOME "/root"  
ENV PATH
"~/.yarn/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
ENV COMPOSER_HOME /root/composer  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Update the installation  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Set the Locale  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
  
# Add ondrej/php PPA  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update  
  
# PHP Installation  
RUN apt-get remove -y --purge php5 php5-common  
  
RUN apt-get install -y \  
php7.0-common \  
php7.0-cli \  
php7.0-fpm \  
php7.0-dev \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-readline \  
php7.0-mcrypt \  
php7.0-zip \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-curl \  
php7.0-json \  
php7.0-sqlite3 \  
php7.0-tokenizer \  
php7.0-imap \  
php-msgpack \  
php-xdebug \  
php7.0-gd  
  
RUN apt-get install build-essential php-pear php7.0-dev  
  
# Install other PHP extensions  
RUN apt-get install -y libzookeeper-mt2 libzookeeper-mt-dev  
RUN pecl install zookeeper-0.4.0  
RUN echo "extension=zookeeper.so" >> `php --ini | grep "Loaded Configuration"
| sed -e "s|.*:\s*||"`  
  
RUN apt-get install -y libssl-dev pkg-config  
RUN pecl install mongodb-1.2.9  
RUN echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" |
sed -e "s|.*:\s*||"`  
  
# Install composer  
VOLUME /root/composer  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer selfupdate  
RUN composer global require hirak/prestissimo --prefer-dist --no-interaction  
  
# mozjpeg-bin requires libpng12  
RUN curl -o /tmp/libpng12.deb
http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb  
RUN dpkg --install /tmp/libpng12.deb  
RUN rm /tmp/libpng12.deb  
  
# Dependency for some nodejs packages?  
RUN apt-get install -y nasm  
  
# NodeJS installation  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# Install some build packages  
RUN npm install -g gulp  
RUN npm install -g grunt  
RUN npm install -g webpack  
  
# YARN  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  

