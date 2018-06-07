FROM ubuntu:12.04  
# Install dependencies  
RUN apt-get update -y  
RUN apt-get install -y git curl apache2 php5 php5-cli php-pear php5-dev
php5-gd php5-memcache php5-memcached php5-xsl php5-geoip php-soap php5-imap
php5-curl php5-intl php5-mysql php5-xdebug php-apc libapache2-mod-php5
php5-mcrypt  
RUN apt-get install -y libxml2 autoconf file gcc libc-dev make pkg-config re2c
--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
# Install app  
RUN rm -rf /var/www  
  
# Configure apache  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN a2enmod expires  
RUN chmod 755 /usr/sbin/apache2ctl  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist  
COPY apache2/apache2.conf /etc/apache2/apache2.conf  
RUN mkdir -p /etc/apache2/certs/  
RUN mkdir -p /etc/apache2/vhosts/  
  
EXPOSE 80  
EXPOSE 443

