FROM ubuntu:xenial  
MAINTAINER rapid.recon@birchwood.ca  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update && apt-get install -y locales && locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LANGUAGE=en_US:en \  
LC_ALL=${OS_LOCALE}  
  
ENV PHP_CONF_DIR=/etc/php/7.1 \  
PHP_DATA_DIR=/var/lib/php  
  
RUN \  
apt-get update && \  
apt-get install -y curl bzip2 software-properties-common python-software-
properties build-essential libfontconfig1 libfontconfig1-dev libfreetype6
libfreetype6-dev chrpath libssl-dev libxft-dev && \  
add-apt-repository -y ppa:ondrej/php && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y git nodejs php7.1-cli php7.1-fpm php7.1-common php7.1-curl
php7.1-gd php7.1-mysql php7.1-sqlite3 php7.1-soap php7.1-xml php7.1-zip
php7.1-gettext php7.1-mbstring php7.1-mcrypt php7.1-intl php7.1-imap
imagemagick php-imagick graphicsmagick && \  
curl -sS https://getcomposer.org/installer | php -- --version=1.4.1 --install-
dir=/usr/local/bin --filename=composer \  
cd / && \  
/usr/local/bin/composer self-update && \  
apt-get autoremove -y  
RUN apt-get -y install python3-setuptools python3-pip  
RUN pip3 install --upgrade pip  
RUN pip3 install boto3  
RUN apt-get -y install zip  

