FROM ubuntu:trusty  
MAINTAINER Alex Pennington  
  
# Install base packages  
RUN apt-get update && apt-get install -y \  
apache2 \  
apache2-utils \  
build-essential \  
curl \  
libapache2-mod-php5 \  
libnotify-bin \  
netcat \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-xdebug \  
php-apc \  
php-pear \  
wget  
  
RUN rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini && \  
sed -i 's/short_open_tag = Off/short_open_tag = On/' /etc/php5/apache2/php.ini  
  
# Install PHPUnit for unit testing  
RUN wget https://phar.phpunit.de/phpunit-4.8.phar \  
&& chmod +x phpunit-4.8.phar \  
&& mv phpunit-4.8.phar /usr/local/bin/phpunit  
  
# Install NodeJS and NPM  
RUN curl -sL https -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
  
# symlink app folder  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
RUN a2enmod rewrite  
RUN a2enmod proxy  
RUN a2enmod proxy_http  
RUN a2enmod ssl  

