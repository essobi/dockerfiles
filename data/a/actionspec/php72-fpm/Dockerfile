FROM phpdockerio/php72-fpm:latest  
  
  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php-memcached php7.2-mysql
php7.2-pgsql php-redis php-xdebug php7.2-bcmath php7.2-bz2 php7.2-dba
php7.2-enchant php7.2-gd php-igbinary php-imagick php7.2-imap php7.2-interbase
php7.2-intl php-mongodb php-msgpack php7.2-odbc php7.2-phpdbg php7.2-pspell
php-raphf php7.2-recode php7.2-soap php7.2-sybase php-tideways php7.2-tidy
php7.2-xmlrpc php7.2-xsl php-yaml php-zmq \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  

