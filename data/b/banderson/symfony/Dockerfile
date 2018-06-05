FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \  
git \  
zip \  
xz-utils \  
curl \  
wget \  
php \  
php-cli \  
php-curl \  
php-gd \  
php-mysql \  
php-json \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php-xml \  
mysql-client \  
apache2 \  
libapache2-mod-php \  
&& apt-get clean  
  
COPY config/php.ini /etc/php/7.0/apache2/php.ini  
  
# Install composer and symfony  
RUN a2enmod rewrite \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer \  
&& wget https://github.com/bander2/twit/releases/download/1.1.0/twit-linux-
amd64 -O /usr/local/bin/twit \  
&& chmod u+x /usr/local/bin/twit \  
&& curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony \  
&& chmod a+x /usr/local/bin/symfony  
  
# Install Bower  
RUN apt-get update && apt-get install -y \  
npm nodejs \  
&& apt-get clean \  
&& npm install -g bower gulp \  
&& ln -s $(which nodejs) /usr/local/bin/node \  
&& echo '{ "allow_root": true }' > /root/.bowerrc  
  
RUN mkdir -p /var/www/symfony  
  
COPY config/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
WORKDIR /var/www/symfony  
  
EXPOSE 80  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

