FROM php:5.6.31-apache  
  
RUN a2enmod rewrite  
  
ADD ./php-ext/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/ioncube_loader_lin_5.6.so  
  
RUN echo "zend_extension=ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/docker-php-ext-ioncube_loader_lin_5.6.ini  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --assume-yes --quiet ca-
certificates curl git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libpq-dev \  
libxml2-dev \  
php-soap \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -Lsf 'https://storage.googleapis.com/golang/go1.8.3.linux-
amd64.tar.gz' | tar -C '/usr/local' -xvzf -  
ENV PATH /usr/local/go/bin:$PATH  
RUN go get github.com/mailhog/mhsendmail  
RUN cp /root/go/bin/mhsendmail /usr/bin/mhsendmail  
  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN pecl install xdebug-2.5.5 \  
&& docker-php-ext-enable xdebug  
  
RUN pecl install rar \  
&& docker-php-ext-enable rar  
  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql  
  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql pgsql pdo_pgsql zip
sockets soap  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  

