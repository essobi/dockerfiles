FROM php:7.1-apache  
  
# Update apt repo  
RUN apt-get update  
  
# Install PHP extensions  
RUN set -ex \  
&& apt-get install -y libfreetype6-dev libjpeg-dev libpng12-dev libpq-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
--with-freetype-dir=/usr --enable-gd-native-ttf \  
&& docker-php-ext-install gd opcache pdo pdo_pgsql zip  
  
# Install PHP 3rd party extensions  
RUN set -ex \  
&& apt-get install -y libtool autoconf g++ make libmagickwand-dev \  
&& pecl install imagick && docker-php-ext-enable imagick \  
&& pecl install xdebug  
  
# Install composer  
RUN curl -# https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set PHP settings  
RUN { \  
echo 'date.timezone = "UTC"'; \  
echo 'sendmail_path = ""'; \  
echo 'log_errors = 1'; \  
echo 'error_reporting = E_ALL'; \  
echo 'error_log = "/dev/stderr"'; \  
echo 'xdebug.max_nesting_level = 1000'; \  
} | tee $PHP_INI_DIR/conf.d/retreat-guru.ini  
  
# Install Blackfire profiler probe  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Install common tools  
RUN apt-get install -y git zip unzip less vim nano nodejs  
  
# Install JS tools  
RUN set -ex \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g bower  
  
# Clean apt repo cache  
RUN apt-get clean  
  
# Tweak Apache config  
RUN set -ex \  
&& echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf \  
&& a2enconf servername \  
&& a2enmod rewrite expires  
  
# Remove symlinks directing access logs to docker  
RUN rm /var/log/apache2/access.log && \  
rm /var/log/apache2/other_vhosts_access.log  
  
# Setup SSL self-signed certificate and SSL  
COPY etc/ssl/*.key /etc/ssl/private/  
COPY etc/ssl/*.pem /etc/ssl/certs/  
RUN a2enmod ssl && a2ensite default-ssl  
EXPOSE 443  
# Copy scripts  
COPY bin/* /usr/local/bin/  
COPY etc/.bashrc /root/  
COPY etc/.vimrc /root/  
  
# Add non root user  
RUN useradd -m noroot -u 1000 -s /bin/bash -g www-data  
  
# Set default working directory  
WORKDIR /var/www  

