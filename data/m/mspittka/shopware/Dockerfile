FROM ubuntu:xenial  
  
MAINTAINER Marco Spittka <marco.spittka@rhiem.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apache2 \  
apache2-utils \  
php-apcu \  
php-cli \  
php-curl \  
php-gd \  
php-mcrypt \  
php-zip \  
phpmyadmin \  
unzip \  
bzip2 \  
git \  
curl \  
ant \  
php-xdebug\  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Configure Apache  
# COPY files/apache-shopware.conf /etc/apache2/sites-
available/000-default.conf  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& sed --in-place "s/^upload_max_filesize.*$/upload_max_filesize = 10M/"
/etc/php/7.0/apache2/php.ini \  
&& sed --in-place "s/^display_errors.*$/display_errors = On/"
/etc/php/7.0/apache2/php.ini \  
&& sed --in-place "s/^memory_limit.*$/memory_limit = 256M/"
/etc/php/7.0/apache2/php.ini \  
&& phpenmod mcrypt  
  
# Install Shopware  
# COPY files/install_5.1.6_04ec396ac8d2fa8c1e088bc2bd2c8132ab56c270.zip
/tmp/shopware.zip  
# ADD
http://releases.s3.shopware.com.s3.amazonaws.com/install_5.2.4_b1a52d04c9c8cd60205c181eb7d51aa5a516bff0.zip
/tmp/shopware.zip  
# Install ioncube  
# COPY files/ioncube_loaders_lin_x86-64.tar.bz2
/tmp/ioncube_loaders_lin_x86-64.tar.bz2  
ADD
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
/tmp/  
RUN tar xvzfC /tmp/ioncube_loaders_lin_x86-64.tar.gz /tmp/ \  
&& rm /tmp/ioncube_loaders_lin_x86-64.tar.gz \  
&& mkdir -p /usr/local/ioncube \  
&& cp /tmp/ioncube/ioncube_loader_lin_7.0.so /usr/local/ioncube \  
&& rm -rf /tmp/ioncube \  
&& echo "zend_extension = /usr/local/ioncube/ioncube_loader_lin_7.0.so" >
/etc/php/7.0/apache2/conf.d/00-ioncube.ini \  
&& echo "zend_extension = /usr/local/ioncube/ioncube_loader_lin_7.0.so" >
/etc/php/7.0/cli/conf.d/00-ioncube.ini \  
&& echo "xdebug.remote_enable = 1" >> /etc/php/7.0/apache2/php.ini \  
&& echo "xdebug.remote_connect_back = 1" >> /etc/php/7.0/apache2/php.ini \  
&& echo "xdebug.remote_port = 9000" >> /etc/php/7.0/apache2/php.ini  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80 443 9000  

