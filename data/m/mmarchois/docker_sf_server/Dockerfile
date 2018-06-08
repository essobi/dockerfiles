FROM php:7.2-apache  
  
ADD bin/docker-* /usr/bin/  
  
ENV GOSU_VERSION 1.10  
# Extensions  
RUN apt-get update && apt-get install -y \  
git \  
ca-certificates \  
libtool \  
libicu-dev \  
openssh-client \  
unzip \  
zlib1g-dev \  
libicu-dev \  
libsodium-dev \  
libjpeg-dev \  
libfreetype6-dev && \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu \  
\--with-png-dir=/usr/lib/x86_64-linux-gnu \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu && \  
docker-php-ext-install \  
bcmath \  
mbstring \  
exif \  
intl \  
zip \  
opcache \  
pdo_mysql \  
gd && \  
echo "date.timezone = Europe/Paris" >> $PHP_INI_DIR/conf.d/app.ini && \  
echo "memory_limit = 342M" >> $PHP_INI_DIR/conf.d/app.ini && \  
echo "date.timezone = Europe/Paris" >> $PHP_INI_DIR/conf.d/app.ini && \  
echo "opcache.max_accelerated_files = 20000" >> $PHP_INI_DIR/conf.d/app.ini &&
\  
echo "realpath_cache_size=4096K" >> $PHP_INI_DIR/conf.d/app.ini && \  
echo "realpath_cache_ttl=600" >> $PHP_INI_DIR/conf.d/app.ini && \  
curl -L -s -o /bin/gosu
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }') && \  
chmod +x /bin/gosu  
  
# APCU ext  
RUN pecl install apcu-5.1.9 \  
&& docker-php-ext-enable apcu  
  
# Install Postgre PDO  
RUN apt-get install -y libpq-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pdo_pgsql pgsql  
  
# Apache conf  
ADD conf/vhost.conf /etc/apache2/sites-available/app.conf  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf \  
&& /bin/bash -c "source /etc/apache2/envvars" \  
&& echo "" > /etc/apache2/sites-available/000-default.conf  
  
# Composer  
RUN curl -k -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN a2enmod \  
rewrite \  
&& a2ensite \  
app.conf  
  
ADD entrypoint.sh /sbin/entrypoint  
  
EXPOSE 80  
WORKDIR /srv  
ENTRYPOINT ["entrypoint"]  

