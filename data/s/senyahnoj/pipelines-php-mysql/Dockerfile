FROM debian:stretch  
MAINTAINER Jon Haynes <jon@senyahnoj.org.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
  
RUN \  
apt-get update &&\  
apt-get -y --no-install-recommends install wget lsb-release ca-certificates
apt-transport-https locales apt-utils gnupg &&\  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&&\  
sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list' &&\  
apt-get update &&\  
echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen &&\  
locale-gen en_GB.UTF-8 &&\  
/usr/sbin/update-locale LANG=en_GB.UTF-8 &&\  
echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections &&\  
echo "mysql-server mysql-server/root_password_again password root" | debconf-
set-selections &&\  
apt-get -y --no-install-recommends install git \  
php7.2-mysql \  
php7.2-cli \  
php7.2-dom \  
php7.2-sqlite3 \  
php7.2-curl \  
php7.2-intl \  
php7.2-json \  
php7.2-gd \  
php7.2-xmlrpc \  
php7.2-zip \  
php-memcached \  
php-gettext \  
php-geoip \  
php-apcu \  
php-imagick \  
php-xdebug \  
imagemagick \  
openssh-client \  
curl \  
software-properties-common \  
gettext \  
zip \  
unzip \  
mysql-server \  
mysql-client \  
apt-transport-https \  
memcached &&\  
curl -sSL https://deb.nodesource.com/setup_8.x | bash - &&\  
apt-get -y --no-install-recommends install nodejs &&\  
apt-get autoclean && apt-get clean && apt-get autoremove  
  
RUN \  
curl -sSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin &&\  
curl -sSL https://phar.phpunit.de/phpunit.phar -o /usr/bin/phpunit && chmod +x
/usr/bin/phpunit &&\  
curl -sSL http://codeception.com/codecept.phar -o /usr/bin/codecept && chmod
+x /usr/bin/codecept &&\  
npm install --no-color --production --global gulp-cli webpack mocha grunt
eslint &&\  
rm -rf /root/.npm /root/.composer /tmp/* /var/lib/apt/lists/*  

