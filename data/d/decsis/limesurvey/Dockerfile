FROM php:7.1.2-apache  
  
ENV DOWNLOAD_URL https://www.limesurvey.org/stable-
release?download=2014:limesurvey2641%20170310targz  
  
RUN apt-get update  
  
# Install Postgre PDO  
RUN apt-get install -y libpq-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pdo pdo_pgsql pgsql \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libldap2-dev \  
zlib1g-dev \  
libc-client-dev \  
libkrb5-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
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
&& mkdir -p /var/lib/php5 \  
&& chown www-data:www-data /var/lib/php5  
  
VOLUME /var/www/html/upload  
VOLUME /var/www/html/application/config

