FROM php:5.6.30-apache  
MAINTAINER n.dininno@gmail.com  
  
ENV DOWNLOAD_URL http://download.limesurvey.org/latest-stable-
release/limesurvey2.72.3+171020.tar.gz  
#php extensions  
RUN apt-get update && apt-get install -y \  
unixodbc \  
unixodbc-dev \  
freetds-bin \  
freetds-dev \  
tdsodbc \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libldap2-dev \  
zlib1g-dev \  
libc-client-dev \  
libkrb5-dev \  
  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/libsybdb.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a \  
&& docker-php-ext-install pdo pdo_dblib \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install zip \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& rm -rf /var/lib/apt/lists/* \  
#Download and install LimeSurvey  
&& curl -SL "$DOWNLOAD_URL" -o /tmp/lime.tar.gz \  
&& tar xf /tmp/lime.tar.gz limesurvey --strip-components=1 -C /var/www/html \  
&& chown -R www-data:www-data /var/www/html \  
&& rm -f /tmp/lime.tar.gz \  
&& chmod -R 755 /var/www/html/tmp \  
&& chmod -R 755 /var/www/html/upload \  
&& chmod -R 755 /var/www/html/application/config \  
&& chmod -R 755 /var/www/html/plugins \  
&& mkdir -p /var/lib/php5 \  
&& chown www-data:www-data /var/lib/php5  
# add files for freetds  
ADD etc_freetds_freetds.conf /etc/freetds/freetds.conf  
ADD etc_odbc.ini /etc/odbc.ini  
ADD etc_odbcinst.ini /etc/odbcinst.ini  

