FROM php:5.6-apache  
  
MAINTAINER Emanuel Righetto <e.righetto@athena.eu>  
  
RUN a2enmod rewrite  
  
RUN \  
apt-get update && \  
apt-get -f install -y \  
fontconfig \  
libxrender1 \  
libxext6 \  
libfontconfig1 \  
nano \  
git \  
wget \  
mysql-client \  
ssmtp \  
patch \  
unzip \  
openssh-server \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libxml2-dev \  
libcurl3 \  
libcurl4-gnutls-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install opcache gd mbstring pdo pdo_mysql pdo_pgsql zip
mysqli calendar json curl xml soap  
  
# Install wkhtmltopdf  
RUN cd /root && \  
wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
mv -v wkhtmltox/bin/* /usr/local/bin/  
  
# Install Composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
# Set the permissions  
RUN chmod 0755 /usr/local/bin/*  
  
# See https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} >> /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# Set recommended PHP.ini settings  
RUN { \  
echo ';;;;;;;;;; General ;;;;;;;;;;'; \  
echo 'memory_limit = 128M'; \  
echo 'upload_max_filesize = 64M'; \  
echo 'post_max_size = 64M'; \  
echo 'max_execution_time = 600'; \  
echo 'date.timezone = Europe/Rome'; \  
echo 'error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING'; \  
echo 'session.auto_start = 0'; \  
echo ' '; \  
echo ';;;;;;;;;; Sendmail ;;;;;;;;;;'; \  
echo 'sendmail_path = /usr/sbin/ssmtp -t'; \  
} >> /usr/local/etc/php/conf.d/custom-php-settings.ini  
  
# Force to use mailcatcher  
RUN echo "mailhub=mailcatcher:25\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf  
  
# This will fix problem with php5 session  
RUN mkdir -p /var/lib/php5/sessions  
RUN chown -R www-data:www-data /var/lib/php5/sessions  
RUN chmod -R 775 /var/lib/php5/sessions  
  
# This will fix problem with user permission on OSX  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/html  

