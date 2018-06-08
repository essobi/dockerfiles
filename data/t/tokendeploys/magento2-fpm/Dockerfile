FROM php:7.0-fpm  
  
MAINTAINER Steve Desmet <steve.desmet@tokendeploys.com>  
  
ENV MAGE_ROOT /var/www/magento  
  
RUN set -xe \  
&& mageBuildDeps=" \  
libicu-dev \  
libpng12-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libxslt1-dev \  
libmcrypt-dev \  
" \  
&& apt-get update && apt-get install -y $mageBuildDeps openssh-client git
ssmtp --no-install-recommends && rm -rf /var/lib/apt/lists/* \  
\  
&& docker-php-ext-install \  
bcmath \  
intl \  
mbstring \  
mcrypt \  
pdo \  
pdo_mysql \  
soap \  
xsl \  
zip \  
opcache \  
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install gd \  
\  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
\  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer selfupdate \  
\  
&& curl -o n98-magerun2 http://files.magerun.net/n98-magerun2.phar \  
&& chmod +x n98-magerun2 \  
&& mv n98-magerun2 /usr/local/bin/ \  
&& n98-magerun2 selfupdate \  
\  
&& echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf \  
&& echo 'sendmail_path = "/usr/sbin/sendmail -i -t"' >
/usr/local/etc/php/conf.d/mail.ini \  
\  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $PHPIZE_DEPS \  
&& apt-get purge -y $mageBuildDeps  
  
WORKDIR $MAGE_ROOT  
  
COPY scripts/* /usr/local/bin/  
  
RUN set -ex \  
&& cd /usr/local/etc \  
&& { \  
echo 'memory_limit = 512M'; \  
} | tee php/conf.d/magento.ini  
  

