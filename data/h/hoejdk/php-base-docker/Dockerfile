# Compose from php 7 apache  
FROM php:7.0-apache  
COPY config/php.ini /usr/local/etc/php/  
  
# Update and install nano editor  
RUN apt-get update && apt-get install -y nano curl unzip python ghostscript
imagemagick libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev
imagemagick libmagickwand-dev  
RUN pecl install imagick  
RUN echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
RUN curl
"https://www.pdflib.com/binaries/PDFlib/911/PDFlib-9.1.1-Linux-x86_64-php.tar.gz"
-o "PDFlib-9.1.1-Linux-x86_64-php.tar.gz"  
RUN tar -zxf PDFlib-9.1.1-Linux-x86_64-php.tar.gz  
RUN cp PDFlib-9.1.1-Linux-x86_64-php/bind/php/php-700/php_pdflib.so
/usr/local/lib/php/extensions/no-debug-non-zts-20151012  
RUN echo 'extension=php_pdflib.so' >/usr/local/etc/php/conf.d/docker-php-ext-
php_pdflib.ini  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN aws configure set default.region eu-west-1  
  
# Install required php modules  
#RUN docker-php-ext-install -j$(nproc) iconv mcrypt  
#RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-
jpeg-dir=/usr/include/  
#RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install pdo pdo_mysql soap  
RUN a2enmod rewrite  
  
# Search and replace  
RUN sed -i 's/html/html\/public/g' /etc/apache2/sites-
available/000-default.conf

