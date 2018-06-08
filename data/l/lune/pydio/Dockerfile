FROM php:7-apache  
  
ENV PYDIO_VERSION 8.0.2  
  
RUN apt-get update && apt-get install -y \  
fontconfig-config \  
fonts-dejavu-core \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libgd-tools \  
libmagick++-dev \  
libjpeg-turbo-progs \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libmagickwand-6-headers \  
libpng-dev \  
libpq-dev \  
libxml2-dev \  
mysql-client \  
pngquant \  
ssmtp \  
sudo \  
unzip \  
wget \  
zlib1g-dev \  
&& apt-get clean && apt-get autoremove -q \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/*  
  
RUN pecl install \  
APCu-5.1.8 \  
imagick-3.4.3  
  
RUN docker-php-ext-install \  
exif \  
intl \  
gd \  
json \  
mbstring \  
mysqli \  
pgsql \  
opcache \  
xml \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
--with-freetype-dir=/usr/include/ \  
&& docker-php-ext-enable \  
apcu \  
imagick  
  
RUN { \  
echo 'output_buffering=Off'; \  
echo 'upload_max_filesize=2G'; \  
echo 'post_max_size=2G'; \  
echo 'memory_limit=512M'; \  
echo 'session.save_path=/var/run/pydio'; \  
echo 'cgi.fix_pathinfo=0'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/pydio.ini  
  
RUN mkdir -p /var/run/pydio /var/lib/pydio /etc/pydio \  
&& chown www-data:www-data /var/run/pydio \  
&& chown www-data:www-data /var/lib/pydio \  
&& chown www-data:www-data /etc/pydio  
  
RUN curl -fsSL -o pydio-core.tar.gz
https://download.pydio.com/pub/core/archives/pydio-
core-${PYDIO_VERSION}.tar.gz \  
&& tar -xzf pydio-core.tar.gz -C /usr/share \  
&& mv /usr/share/pydio-core-${PYDIO_VERSION} /usr/share/pydio \  
&& mv /usr/share/pydio/data /var/lib/pydio/data \  
&& mv /usr/share/pydio/conf /etc/pydio/conf \  
&& chown -R www-data:www-data /var/lib/pydio/data \  
&& sed -i -e 's!.*define("AJXP_CONF_PATH".*!define("AJXP_CONF_PATH",
"/etc/pydio/conf");!g' /usr/share/pydio/base.conf.php \  
&& sed -i -e 's!.*define("AJXP_DATA_PATH".*!define("AJXP_DATA_PATH",
"/var/lib/pydio/data");!g' /etc/pydio/conf/bootstrap_context.php  
  
VOLUME /var/run/pydio  
VOLUME /var/lib/pydio  
  
COPY httpd.conf /etc/pydio/httpd.conf  
RUN ln -s /etc/pydio/httpd.conf /etc/apache2/sites-available/pydio.conf \  
&& a2enmod expires headers mime rewrite \  
&& a2dissite 000-default \  
&& a2ensite pydio  

