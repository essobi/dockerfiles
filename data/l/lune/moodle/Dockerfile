FROM php:5.6-apache  
  
ENV DEBCONF_FRONTEND non-interactive  
  
RUN apt-get update && apt-get install -y \  
git \  
imagemagick \  
libapache2-mod-rpaf \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-turbo-progs \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
mysql-client \  
pngquant \  
ssmtp \  
sudo \  
unzip \  
wget \  
zlib1g-dev \  
&& docker-php-ext-install \  
bcmath \  
curl \  
exif \  
intl \  
mbstring \  
mcrypt \  
mysql \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
pgsql \  
soap \  
sockets \  
xmlrpc \  
zip \  
&& apt-get clean && apt-get autoremove -q \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/* \  
&& a2enmod deflate expires headers mime rewrite \  
&& echo "<Directory /var/www/html>\nAllowOverride All\n</Directory>" >
/etc/apache2/conf-enabled/allowoverride.conf \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& echo "sendmail_path = /usr/sbin/ssmtp -t" > /usr/local/etc/php/conf.d/conf-
sendmail.ini \  
&& echo "date.timezone='UTC'\n" > /usr/local/etc/php/conf.d/conf-date.ini  
  
  
COPY ./ /var/www/html/  
  
RUN mv /var/www/html/config-docker.php /var/www/html/config.php \  
&& chown -R www-data:www-data /var/www/html  
  
VOLUME /moodledata  

