FROM php:7.0.12-fpm  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm  
  
# prepare node  
RUN apt-get update && \  
apt-get install -y apt-transport-https && \  
curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key
add - && \  
echo "deb https://deb.nodesource.com/node_6.x jessie main" | tee
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb-src https://deb.nodesource.com/node_6.x jessie main" | tee -a
/etc/apt/sources.list.d/nodesource.list  
  
# install php & node  
RUN apt-get update && \  
apt-get install -y nodejs \  
rsyslog \  
zlib1g-dev \  
libpng-dev \  
libjpeg-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev && \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/freetype2 \  
\--with-png-dir=/usr/include \  
\--with-jpeg-dir=/usr/include && \  
docker-php-ext-install pdo \  
pdo_mysql \  
mysqli \  
zip \  
gd \  
curl \  
sockets \  
json && \  
docker-php-ext-enable pdo \  
pdo_mysql \  
gd \  
curl \  
json \  
zip \  
mysqli  
  
# configure php  
RUN echo "log_errors = On" >> /usr/local/etc/php/php.ini && \  
echo "display_startup_errors = On" >> /usr/local/etc/php/php.ini && \  
echo "display_errors = On" >> /usr/local/etc/php/php.ini && \  
echo "error_reporting = -1" >> /usr/local/etc/php/php.ini && \  
echo "upload_max_filesize = 100M" >> /usr/local/etc/php/php.ini && \  
echo "post_max_size = 100M" >> /usr/local/etc/php/php.ini && \  
echo "date.timezone = America/Los_Angeles" >> /usr/local/etc/php/php.ini && \  
echo "catch_workers_output = yes" >> /usr/local/etc/php-fpm.conf  
  
# install composer & npm@3 & yarn  
RUN echo "$(curl -sS https://composer.github.io/installer.sig) -" > composer-
setup.php.sig && \  
curl -sS https://getcomposer.org/installer | tee composer-setup.php |
sha384sum -c composer-setup.php.sig && \  
curl -L https://www.npmjs.org/install.sh | sh && \  
php composer-setup.php -- --install-dir=/usr/local/bin --filename=composer &&
\  
npm install yarn  
  
VOLUME ["/var/www"]  
WORKDIR /var/www  
  
CMD php-fpm  
  
EXPOSE 9000  

