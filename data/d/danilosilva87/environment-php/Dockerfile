FROM php:7.1-apache-jessie  
  
LABEL maintainer="danilosilva87@gmail.com"  
  
ENV APPLICATION \  
git  
  
ENV PHP_DEPS \  
libjpeg-dev \  
libpng12-dev \  
libssl-dev \  
libmcrypt-dev \  
lib32z1-dev \  
libxml2-dev \  
libedit-dev \  
libxslt1-dev  
  
ENV EXTENSION \  
zip \  
mcrypt \  
mbstring \  
pdo \  
pdo_mysql \  
xml \  
json \  
opcache \  
phar \  
readline \  
sockets \  
tokenizer \  
xsl \  
gd  
  
ENV APACHE_RUN_USER=app  
ENV APACHE_RUN_GROUP=app  
ENV APACHE_DOCUMENT_ROOT /home/app/public  
  
RUN groupadd --gid 1000 app \  
&& useradd --uid 1000 --gid app -m app  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
$PHP_DEPS \  
$APPLICATION && \  
docker-php-ext-install $EXTENSION && \  
rm -rf /etc/apache2/sites-*/ && \  
chown -R app:app /var/run/apache2 /var/log/apache2 /var/lock/apache2
/var/lib/apache2 && \  
apt-get purge -y --auto-remove && \  
rm -r /var/lib/apt/lists/*  
  
COPY php.ini /usr/local/etc/php/  
COPY ports.conf /etc/apache2/ports.conf  
COPY sites-enabled/*.conf /etc/apache2/sites-enabled/  
  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
RUN a2enmod rewrite ssl && \  
curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
USER app  
  
WORKDIR /home/app  
  
EXPOSE 8080  
CMD ["apache2-foreground"]

