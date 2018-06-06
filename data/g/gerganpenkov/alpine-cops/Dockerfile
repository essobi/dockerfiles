FROM alpine:3.6  
MAINTAINER Gergan Penkov <gergan at google.com>  
  
RUN apk update &&\  
apk upgrade &&\  
apk add --no-cache --update git apache2 php7-apache2 curl php7-cli php7-curl
php7-json php7-xml php7-wddx php7-xmlreader php7-dom php7-xsl php7-phar
php7-openssl php7-pdo php7-pdo_sqlite php7-gd php7-intl php7-zlib php7-zip
php7-mbstring php7-iconv && \  
curl -sS https://getcomposer.org/installer | /usr/bin/php -- --install-
dir=/usr/bin --filename=composer && \  
rm -rf /var/www/localhost/htdocs && \  
git clone -b master https://github.com/seblucas/cops.git
/var/www/localhost/htdocs && \  
composer global require "fxp/composer-asset-plugin:~1.1" && \  
cd /var/www/localhost/htdocs && \  
composer install --no-dev --optimize-autoloader && \  
sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \  
sed -i 's/Group apache/Group www-data/g' /etc/apache2/httpd.conf && \  
mkdir /books && \  
mkdir /run/apache2/ && \  
chown -R apache:www-data /run/apache2 && \  
chown -R apache:www-data /var/www/localhost/htdocs && \  
rm -rf /var/cache/apk/*  
  
ADD files/config_local.php /var/www/localhost/htdocs/config_local.php  
  
EXPOSE 80  
# Expose volumes  
VOLUME ["/books"]  
  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]  

