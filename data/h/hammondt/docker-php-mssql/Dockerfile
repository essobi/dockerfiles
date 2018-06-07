FROM php:7.1-apache  
# Install sqlsrv pre-pre-requisites  
RUN apt-get update \  
&& apt-get install -y -q curl apt-transport-https \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install sqlsrv pre-requisites  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl https://packages.microsoft.com/config/debian/8/prod.list >
/etc/apt/sources.list.d/mssql-release.list \  
&& apt-get update \  
&& apt-get install -y locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& ACCEPT_EULA=Y apt-get install -y msodbcsql \  
&& apt-get install -y unixodbc-dev \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install sqlsrv extensions  
RUN pear config-set php_ini `php --ini | grep "Loaded Configuration" | sed -e
"s|.*:\s*||"` system \  
&& pecl install pdo_sqlsrv \  
&& pecl install sqlsrv \  
&& docker-php-ext-enable sqlsrv pdo_sqlsrv  
  
# Install sSMTP so we can send email  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends ssmtp \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
# FROM Drupal Dockerfile  
# install the PHP extensions we need  
RUN set -ex \  
&& buildDeps=' \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
&& docker-php-ext-install -j "$(nproc)" gd mbstring opcache pdo pdo_mysql zip
\  
&& apt-mark manual \  
libjpeg62-turbo \  
libpq5 \  
&& apt-get purge -y --auto-remove $buildDeps  
  
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
#  
# Configure PHPSMTP  
RUN { \  
echo '[mail function]'; \  
echo 'sendmail_path = "/usr/sbin/ssmtp -t"'; \  
} > /usr/local/etc/php/conf.d/mail.ini  
  
RUN echo '[PHP]\n\  
max_execution_time = 30\n\  
max_input_time = 60\n\  
max_input_vars = 5000\n\  
memory_limit = 512M\n\  
max_post_size = 100M\n\  
file_uploads = On\n\  
upload_max_filesize = 100M\n\  
max_file_uploads = 20\n\  
\n\  
[Date]\n\  
date.timezone = America/New_York\n\  
date.default_latitude = 39.98\n\  
date.default_longitude = -76.94\n'\ >> /usr/local/etc/php/php.ini  
  
RUN { \  
echo 'FromLineOverride=YES'; \  
echo 'mailhub=mail.moo.umd.edu'; \  
echo 'hostname=php-mssql.moo.umd.edu';\  
} > /etc/ssmtp/ssmtp.conf  
#COPY config/apache/vhost.conf /etc/apache2/sites-enabled/00-default.conf  

