# Container Base  
FROM php:7.0-apache  
  
ENV http_proxy ${HTTP_PROXY}  
ENV https_proxy ${HTTP_PROXY}  
ENV NR_ENABLED=false  
ENV NR_APP_NAME=""  
ENV NR_LICENSE_KEY=""  
COPY configs/ports.conf /etc/apache2/ports.conf  
COPY apache-run.sh /usr/bin/apache-run  
  
RUN chmod a+x /usr/bin/apache-run  
  
# Install libs  
RUN apt-get update && apt-get install -y wget vim supervisor zip
libfreetype6-dev libjpeg62-turbo-dev \  
libmcrypt-dev libpng-dev libssl-dev libaio1 git libcurl4-openssl-dev libxslt-
dev \  
libldap2-dev libicu-dev libc-client-dev libkrb5-dev libsqlite3-dev libedit-dev  
  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure hash \--with-mhash \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install -j$(nproc) iconv bcmath mcrypt \  
gd pdo_mysql calendar curl exif ftp gettext \  
hash xsl ldap intl imap pdo_sqlite mbstring \  
mcrypt pcntl readline shmop soap sockets wddx zip  
  
# Install ssh2  
RUN wget https://www.libssh2.org/download/libssh2-1.7.0.tar.gz && wget
https://pecl.php.net/get/ssh2-1.1.2.tgz \  
&& tar vxzf libssh2-1.7.0.tar.gz && tar vxzf ssh2-1.1.2.tgz \  
&& cd libssh2-1.7.0 && ./configure \  
&& make && make install \  
&& cd ../ssh2-1.1.2 && phpize && ./configure --with-ssh2 \  
&& make && make install \  
&& echo "extension=ssh2.so" >> /usr/local/etc/php/conf.d/ssh2.ini  
  
# Install oci8  
RUN mkdir -p /opt/oci8 \  
&& cd /opt/oci8 \  
&& wget https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-basic-
linux.x64-12.1.0.2.0.zip \  
&& wget https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-sdk-
linux.x64-12.1.0.2.0.zip \  
&& unzip instantclient-sdk-linux.x64-12.1.0.2.0.zip \  
&& unzip instantclient-basic-linux.x64-12.1.0.2.0.zip \  
&& cd instantclient_12_1/ \  
&& ln -s libclntsh.so.12.1 libclntsh.so \  
&& ln -s libocci.so.12.1 libocci.so \  
&& cd /tmp \  
&& wget https://pecl.php.net/get/oci8-2.1.7.tgz \  
&& tar xzf oci8-2.1.7.tgz \  
&& cd oci8-2.1.7 \  
&& phpize \  
&& ./configure --with-oci8=shared,instantclient,/opt/oci8/instantclient_12_1/
\  
&& make \  
&& make install \  
&& echo "extension=/tmp/oci8-2.1.7/modules/oci8.so" >>
/usr/local/etc/php/conf.d/oci8.ini  
  
# Install redis  
RUN pecl install redis \  
&& echo "extension=redis.so" >> /usr/local/etc/php/conf.d/redis.ini  
  
RUN echo "---> Adding Support for NewRelic" && \  
mkdir /tmp/newrelic /scripts/ && \  
cd /tmp/newrelic && \  
wget -r -l1 -nd -A"linux.tar.gz"
https://download.newrelic.com/php_agent/release/ && \  
gzip -dc newrelic*.tar.gz | tar xf - && \  
cd newrelic-php5* && \  
rm -f /usr/local/lib/php/extensions/no-debug-non-zts-20151012/newrelic.so && \  
cp ./agent/x64/newrelic-20151012.so /usr/local/lib/php/extensions/no-debug-
non-zts-20151012/newrelic.so && \  
cp ./daemon/newrelic-daemon.x64 /usr/bin/newrelic-daemon && \  
cp ./scripts/newrelic.ini.template /scripts/newrelic.ini && \  
mkdir /var/log/newrelic  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
# Install XDebug  
RUN pecl install xdebug  
  
# Run composer install  
CMD /usr/bin/apache-run  
  
EXPOSE 8080  

