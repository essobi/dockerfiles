#FROM php:7.1-fpm  
FROM php:7.1.16-fpm-jessie  
  
ENV PATH="${PATH}:/usr/local/bin/"  
RUN apt-get update \  
&& apt-get -y install \  
mercurial \  
git \  
unzip  
  
# Install opcache  
RUN docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install opcache  
  
# Install bcmath  
RUN docker-php-ext-install bcmath  
  
# Install bz2  
RUN apt-get install -y libbz2-dev \  
&& docker-php-ext-install bz2  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Install zip  
RUN apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
# Install mbstring  
RUN docker-php-ext-install mbstring  
  
# Install mcrypt  
RUN apt-get install -y libmcrypt-dev \  
&& docker-php-ext-install mcrypt  
  
# Install phpredis  
#RUN git clone -b php7 https://github.com/phpredis/phpredis.git
/usr/src/php/ext/redis \  
# && docker-php-ext-install redis  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
# Install PDO  
RUN apt-get update \  
&& apt-get install -y libpq-dev sqlite3 libsqlite3-dev \  
&& docker-php-ext-install pdo_pgsql pdo_mysql pdo_sqlite  
  
# Install XSL  
RUN apt-get install -y libxslt-dev \  
&& docker-php-ext-install xsl  
  
# Install xmlrpc  
RUN docker-php-ext-install xmlrpc  
  
# Install ftp  
RUN docker-php-ext-install ftp  
  
# Install intl  
RUN apt-get install -y libicu-dev \  
&& docker-php-ext-install intl  
  
# Install Xdebug  
ADD php.ini /usr/local/etc/php/php.ini  
RUN curl -fsSL 'https://xdebug.org/files/xdebug-2.6.0.tgz' -o xdebug.tar.gz \  
&& mkdir -p xdebug \  
&& tar -xf xdebug.tar.gz -C xdebug --strip-components=1 \  
&& rm xdebug.tar.gz \  
&& ( \  
cd xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -r xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set timezone  
RUN rm /etc/localtime && \  
ln -s /usr/share/zoneinfo/Europe/Vilnius /etc/localtime  
  
# Install wkhtmltopdf and wkhtmltoimage dependencies  
RUN apt-get install -y libxrender1 libfontconfig1  
  
# Expose XDebug remote agent connection  
EXPOSE 9000  
WORKDIR /var/www/  

