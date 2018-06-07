FROM ubuntu:xenial  
  
MAINTAINER Achim Rosenhagen <a.rosenhagen@ffuenf.de>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ant \  
curl \  
git \  
openssl \  
libfreetype6-dev \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
libxml2-dev \  
mysql-client \  
openjdk-8-jdk \  
wget \  
zlib1g-dev \  
php-common \  
php-dev \  
php-pear \  
php-pecl-http \  
php-imap \  
php-intl \  
php-json \  
php-mysql \  
php-opcache \  
php-oauth \  
php-pspell \  
php-ldap \  
php-xml \  
php-soap \  
php-mbstring \  
php-apcu \  
php-cli \  
php-curl \  
php-gd \  
php-mcrypt \  
php-zip \  
unzip \  
bzip2 \  
apache2 \  
apache2-utils \  
libapache2-mod-php \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN mkdir /tmp/ioncube && \  
mkdir -p /usr/local/ioncube && \  
cd /tmp/ioncube && \  
wget -q
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
-O /tmp/ioncube/ioncube_loaders_lin_x86-64.tar.gz && \  
tar xvf /tmp/ioncube/ioncube_loaders_lin_x86-64.tar.gz && \  
cd `php -i | grep extension_dir | cut -d' ' -f 5` && \  
cp /tmp/ioncube/ioncube/ioncube_loader_lin_7.0.so
/usr/local/ioncube/ioncube_loader_lin_7.0.so && \  
echo zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.0.so >
/etc/php/7.0/apache2/conf.d/00-ioncube.ini && \  
echo zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.0.so >
/etc/php/7.0/cli/conf.d/00-ioncube.ini && \  
rm -rf /tmp/ioncube/  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY files/apache-shopware.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& sed --in-place "s/^upload_max_filesize.*$/upload_max_filesize = 20M/"
/etc/php/7.0/apache2/php.ini \  
&& sed --in-place "s/^memory_limit.*$/memory_limit = 512M/"
/etc/php/7.0/apache2/php.ini \  
&& sed --in-place "s/^allow_url_fopen.*$/allow_url_fopen = On/"
/etc/php/7.0/apache2/php.ini \  
&& phpenmod mcrypt  
  
COPY files/config.php.tmpl /config.php.tmpl  
  
VOLUME ["/var/www/html"]  
  
COPY files/substitute-env-vars.sh /bin/substitute-env-vars.sh  
RUN chmod +x /bin/substitute-env-vars.sh  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80

