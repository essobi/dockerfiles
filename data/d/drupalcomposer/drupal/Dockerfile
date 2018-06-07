FROM drupal:8-fpm-alpine  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
# Install remainder of packages.  
RUN apk --update add --no-cache \  
bash \  
git \  
gzip \  
mysql-client \  
patch \  
postgresql-client \  
ssmtp \  
zlib-dev  
  
COPY conf/ssmtp.conf /etc/ssmtp/ssmtp.conf  
RUN echo "hostname=drupal-composer.org" >> /etc/ssmtp/ssmtp.conf  
RUN echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/usr/local/etc/php/conf.d/mail.ini  
  
COPY php.ini /usr/local/etc/php/php.ini  
  
# Install extensions  
RUN docker-php-ext-configure zip \  
\--with-zlib-dir=/usr && \  
docker-php-ext-install zip && \  
docker-php-ext-install bcmath  

