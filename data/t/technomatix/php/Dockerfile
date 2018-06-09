FROM php:5.6-cli  
  
ENV TZ=UTC  
ENV COMPOSER_HOME=/home/composer/.composer  
ENV COMPOSER_ALLOW_SUPERUSER=1  
  
RUN set -xe && \  
apt-get -qq update && \  
  
# Configure timezone  
ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone
&& \  
  
# Install php extensions  
  
## GD http://php.net/manual/en/book.image.php  
apt-get -qq install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev && \  
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
  
## MySQL Functions http://php.net/manual/en/ref.pdo-mysql.php  
docker-php-ext-install -j$(nproc) pdo_mysql && \  
  
## BCMath Arbitrary Precision Mathematics http://php.net/manual/en/book.bc.php  
docker-php-ext-install -j$(nproc) bcmath && \  
  
## Zip http://php.net/manual/en/book.zip.php  
apt-get -qq install -y zlib1g-dev && \  
docker-php-ext-install -j$(nproc) zip && \  
  
## XML-RPC http://php.net/manual/en/book.xmlrpc.php  
apt-get -qq install -y libxml2-dev && \  
docker-php-ext-install -j$(nproc) xmlrpc && \  
  
## XSL http://php.net/manual/en/book.xsl.php  
apt-get -qq install -y libxslt-dev && \  
docker-php-ext-install -j$(nproc) xsl && \  
  
## Intl http://php.net/manual/en/book.intl.php  
apt-get -qq install -y libicu-dev && \  
docker-php-ext-install -j$(nproc) intl && \  
  
## Mcrypt http://php.net/manual/en/book.mcrypt.php  
apt-get -qq install -y libmcrypt-dev && \  
docker-php-ext-install -j$(nproc) mcrypt && \  
  
# Configure PHP  
echo "date.timezone = "${TZ} >> /usr/local/etc/php/php.ini && \  
  
# Tools  
apt-get -qq install -y git && \  
apt-get -qq install -y mysql-client && \  
  
# Install Composer  
curl -sS https://getcomposer.org/installer | php \-- \  
\--filename=composer \  
\--install-dir=/usr/local/bin && \  
  
# Clean  
composer clearcache && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH="/home/composer/.composer/vendor/bin:${PATH}"  
  
COPY etc/entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["entrypoint.sh"]  
  
WORKDIR /project  
  
CMD ["php", "-a"]  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/Technomatix/docker-php.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="Technomatix team <team@tmx-learning.com>" \  
org.label-schema.name="docker-php" \  
org.label-schema.description="PHP stack for development and work" \  
org.label-schema.url="https://github.com/Technomatix/docker-php"  

