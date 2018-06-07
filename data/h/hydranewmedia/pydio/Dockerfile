FROM php:7.1-apache  
  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y \  
bzip2 libbz2-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# https://pydio.com/fr/docs/v7-enterprise/pydio-requirements  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install mysqli gd dom exif intl mbstring ldap opcache
pdo_mysql pdo_pgsql pgsql zip bz2  
  
# configure locales  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# wanted pydio settings  
RUN { \  
echo 'output_buffering=Off'; \  
echo 'session.save_path="/tmp"'; \  
echo 'default_charset="utf-8"'; \  
echo 'upload_max_filesize=1G'; \  
echo 'post_max_size=1G'; \  
} > /usr/local/etc/php/conf.d/100-pydio.ini  
  
ENV PYDIO_VERSION 8.0.1  
VOLUME /var/www/html  
WORKDIR /var/www/html/  
  
RUN mkdir /usr/src/pydio && curl -fsSL
"https://download.pydio.com/pub/core/archives/pydio-
core-${PYDIO_VERSION}.tar.gz" | tar xz --strip-components=1 -C /usr/src/pydio  
  
COPY start.sh /usr/bin/start.sh  
CMD ["/usr/bin/start.sh", "apache2-foreground"]  

