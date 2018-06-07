FROM php:fpm  
  
RUN apt-get update  
  
# Install Git  
RUN apt-get install -y git  
  
# Install Postgre PDO  
RUN apt-get install -y libpq-dev  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql  
  
#Install curl  
RUN apt-get install -y curl libcurl3 libcurl3-dev  
  
#Install International Components for Unicode  
RUN apt-get install -y libicu-dev  
  
#ssl libs  
RUN apt-get install -y libc-client-dev libkrb5-dev  
  
#lib for gd  
RUN apt-get install -y libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libxpm-dev \  
libvpx-dev  
  
#mail support  
RUN apt-get install -y exim4  
  
#Configure imap  
RUN docker-php-ext-configure imap --with-imap-ssl --with-kerberos  
  
# Configure GD package for JPEG support  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-vpx-dir=/usr/lib/x86_64-linux-gnu/  
  
#gettext  
RUN apt-get install -y gettext locales locales-all  
  
#install docker php extention  
RUN docker-php-ext-install \  
mysqli \  
pdo \  
pdo_pgsql \  
pgsql \  
intl \  
exif \  
pcntl \  
gettext \  
imap \  
ftp \  
gd \  
json \  
curl \  
iconv \  
mbstring \  
calendar  
  
#add sendmail to php  
RUN echo "sendmail_path=sendmail -i -t" >> /usr/local/etc/php/conf.d/php-
sendmail.ini  
  
#add mcrypt  
RUN apt-get install -y libmcrypt-dev \  
&& docker-php-ext-install mcrypt  
  
#add zip  
RUN apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
# Install Xdebug  
#RUN curl -fsSL 'https://xdebug.org/files/xdebug-2.4.0.tgz' -o xdebug.tar.gz \  
# && mkdir -p xdebug \  
# && tar -xf xdebug.tar.gz -C xdebug --strip-components=1 \  
# && rm xdebug.tar.gz \  
# && ( \  
# cd xdebug \  
# && phpize \  
# && ./configure --enable-xdebug \  
# && make -j$(nproc) \  
# && make install \  
# ) \  
# && rm -r xdebug \  
# && docker-php-ext-enable xdebug  
#cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#new entrypoint  
COPY entrypoint.sh /usr/local/bin/  
  
RUN chmod 777 /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

