#  
# Drupal Docker PHP-FPM  
#  
  
FROM php:7.1-fpm  
# Install PHP extensions and dependencies  
RUN apt-get update && \  
apt-get install -y zlib1g-dev libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev && \  
docker-php-ext-install zip && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install opcache && \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
apt-get install git-core wget -y && \  
mkdir -p /var/www/web  
# Install xdebug  
RUN pecl install xdebug -y && \  
echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" >
/usr/local/etc/php/conf.d/xdebug.ini && \  
echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo "xdebug.remote_autostart=true" >> /usr/local/etc/php/conf.d/xdebug.ini &&
\  
echo "xdebug.idekey=PHP_STORM" >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo "upload_max_filesize=50M" >> /usr/local/etc/php/conf.d/xdebug.ini  
# Install Composer  
RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
rm dotdeb.gpg && \  
curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/local/bin \--filename=composer && \  
composer global require "hirak/prestissimo:^0.3" \--prefer-dist \--no-progress
\--no-suggest \--optimize-autoloader \--classmap-authoritative && \  
composer clear-cache  
  
# Add drush, git and drupal console to path  
ENV PATH $PATH:/var/www/bin:/usr/lib/git-core  
# Install sendmail & set up sendmail config  
RUN apt-get update && apt-get install -q -y ssmtp mailutils && rm -rf
/var/lib/apt/lists/* && \  
echo "hostname=localhost.localdomain" > /etc/ssmtp/ssmtp.conf && \  
echo "root=admin@localhost.com" >> /etc/ssmtp/ssmtp.conf && \  
echo "mailhub=drupal-mailhog:1025" >> /etc/ssmtp/ssmtp.conf && \  
echo "sendmail_path=sendmail -i -t" >> /usr/local/etc/php/conf.d/php-
sendmail.ini && \  
echo "localhost localhost.localdomain" >> /etc/hosts  
# Add git to path  
ENV PATH="/usr/lib/git-core:${PATH}"  
  
WORKDIR /var/www

