FROM ubuntu:16.04  
# Image based on lliccien/docker-symfony-drupal  
MAINTAINER Eduardo Pinuaga <eduardo.pinuaga-linares@elementsystems.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Add repository PPA php 7.1  
RUN apt-get update && \  
apt-get install -y python-software-properties && \  
apt-get install -y software-properties-common && \  
apt-get install -y build-essential  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y language-pack-en-base &&\  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:ondrej/php  
  
# Update the package repository and Install base packages  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes nano wget curl sqlite3 git && \  
apt-get install --yes apache2 supervisor && \  
apt-get install --yes \  
libapache2-mod-php7.1 \  
php7.1-bcmath \  
php7.1-bz2 \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-dba \  
php7.1-gd \  
php7.1-gmp \  
php7.1-imap \  
php7.1-intl \  
php7.1-json \  
php7.1-ldap \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-odbc \  
php7.1-pgsql \  
php7.1-recode \  
php7.1-snmp \  
php7.1-soap \  
php7.1-sqlite \  
php7.1-tidy \  
php7.1-xdebug \  
php7.1-xml \  
php7.1-xmlrpc \  
php7.1-xsl \  
php7.1-zip && \  
apt-get install -y php-gnupg php-imagick php-mongodb php-fxsl php-
uploadprogress  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Install Drush  
RUN wget http://files.drush.org/drush.phar && chmod +x drush.phar && mv
drush.phar /usr/local/bin/drush  
  
# Install Drupal-Console  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar && mv
drupal.phar /usr/local/bin/drupal && chmod +x /usr/local/bin/drupal  
  
# Install Symfony Installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && chmod
a+x /usr/local/bin/symfony  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs  
  
# install libxrender1 for wkhtmltopdf  
RUN apt-get update && apt-get install libxrender1 --yes  
  
# Cleaning  
RUN apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# config Xdebug  
RUN sed -i '$ a\xdebug.var_display_max_depth=4' /etc/php/7.1/mods-
available/xdebug.ini && \  
sed -i '$ a\xdebug.max_nesting_level=500' /etc/php/7.1/mods-
available/xdebug.ini && \  
sed -i '$ a\xdebug.var_display_max_data=-1' /etc/php/7.1/mods-
available/xdebug.ini && \  
sed -i '$ a\xdebug.remote_enable=1' /etc/php/7.1/mods-available/xdebug.ini &&
\  
sed -i '$ a\xdebug.remote_port="9000"' /etc/php/7.1/mods-available/xdebug.ini  
  
# Confugure php.ini apache  
RUN sed -ri 's/^max_execution_time\s*=\s*30/max_execution_time = 3600/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^;date.timezone\s*=/date.timezone = UTC/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^memory_limit\s*=\s*128M/memory_limit = 1024M/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^post_max_size\s*=\s*8M/post_max_size = 2048M/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 2048M/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^;opcache.enable=0/opcache.enable=1/g' /etc/php/7.1/apache2/php.ini
&& \  
sed -ri 's/^;opcache.enable_cli=0/opcache.enable_cli=1/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^;opcache.memory_consumption=64/opcache.memory_consumption=128/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri
's/^;opcache.interned_strings_buffer=4/opcache.interned_strings_buffer=8/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri
's/^;opcache.max_accelerated_files=2000/opcache.max_accelerated_files=4000/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^;opcache.revalidate_freq=2/opcache.revalidate_freq=2/g'
/etc/php/7.1/apache2/php.ini && \  
sed -ri 's/^;opcache.fast_shutdown=0/opcache.fast_shutdown=1/g'
/etc/php/7.1/apache2/php.ini && \  
echo 'extension=uploadprogress.so' >> /etc/php/7.1/apache2/php.ini  
  
# Confugure php.ini php Cli  
RUN sed -ri 's/^max_execution_time\s*=\s*30/max_execution_time = 3600/g'
/etc/php/7.1/cli/php.ini && \  
sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.1/cli/php.ini && \  
sed -ri 's/^;date.timezone\s*=/date.timezone = UTC/g' /etc/php/7.1/cli/php.ini
&& \  
sed -ri 's/^memory_limit\s*=\s*128M/memory_limit = 1024M/g'
/etc/php/7.1/cli/php.ini && \  
sed -ri 's/^post_max_size\s*=\s*8M/post_max_size = 2048M/g'
/etc/php/7.1/cli/php.ini && \  
sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 2048M/g'
/etc/php/7.1/cli/php.ini  
  
# Config apache RUN a2enmod rewrite  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && a2enmod
rewrite php7.1  
  
# Copy configuration files  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Delete and create directories  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html /var/log/supervisor && chown -R www-data:www-
data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html
/var/log/supervisor  
  
# Override Enabled ENV Variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
WORKDIR /var/www/html  
  
RUN usermod -u 1000 www-data  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

