FROM php:7-apache  
WORKDIR /var/www/  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https && \  
apt-get install -y libcurl4-gnutls-dev libxml2-dev libbz2-dev zlib1g-dev
libssl-dev libtidy-dev libxslt1-dev libmagic-dev libexif-dev file
libssh2-1-dev git curl wget unzip libjpeg62-turbo-dev libpng-dev
libfreetype6-dev sendmail && \  
apt-get clean && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install zip && \  
docker-php-ext-install curl dom bcmath xmlwriter xsl zip bcmath calendar ctype
&& \  
docker-php-ext-install exif && \  
a2enmod rewrite  
  
RUN cd /tmp && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
rm -rf /tmp/./*  
  
RUN rm -rf html && \  
git clone https://github.com/getgrav/grav.git html && \  
cd html && \  
composer -n --no-ansi install && \  
bin/grav install && \  
bin/gpm install -n -q -y admin && \  
chown -R www-data .  
  
  
ENV PATH="/var/www/html/bin:$HOME/.composer/vendor/bin:${PATH}"  
VOLUME /var/www/html/logs #for performance reason  
VOLUME /var/www/html/cache #for performance reason  
  
VOLUME /var/www/html/user #user data  
  
WORKDIR /var/www/html  

