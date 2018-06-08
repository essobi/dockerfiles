FROM php:7.1-fpm-jessie  
  
ENV SUMMARY="PHP 7 image with standar modules" \  
DESCRIPTION="The image use scripts and configurations compatible \  
with redhat openshift."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="php 7" \  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \  
io.s2i.scripts-url=image:///usr/libexec/s2i \  
com.redhat.component="php" \  
name="oondeo/php" \  
version="7" \  
release="1" \  
maintainer="OONDEO <info@oondeo.es>"  
  
ENV \  
# DEPRECATED: Use above LABEL instead, because this will be removed in future
versions.  
STI_SCRIPTS_URL=image:///usr/libexec/s2i \  
# Path to be used in other layers to place s2i scripts into  
STI_SCRIPTS_PATH=/usr/libexec/s2i  
  
ENV \  
# The $HOME is not set by default, but some applications needs this variable  
HOME=/opt/app-root/src \  
PATH=/opt/app-root/src/bin:/opt/app-root/bin:$STI_SCRIPTS_PATH:$PATH  
  
  
# When bash is started non-interactively, to run a shell script, for example
it  
# looks for this variable and source the content of this file. This will
enable  
# the SCL for all scripts without need to do 'scl enable'.  
ENV BASH_ENV=/opt/app-root/etc/scl_enable \  
ENV=/opt/app-root/etc/scl_enable \  
XDG_DATA_HOME=$HOME/.local/share \  
DEBIAN_FRONTEND=noninteractive \  
LANG=es_ES.UTF-8 LANGUAGE=es_ES.UTF-8 LC_ALL=es_ES.UTF-8 \  
PROMPT_COMMAND=". /opt/app-root/etc/scl_enable"  
# Copy extra files to the image.  
COPY ./root/root/ /  
  
RUN /usr/bin/docker-header  
  
ENTRYPOINT ["/sbin/tini", "-g" ,"--", "container-entrypoint"]  
  
# Directory with the sources is set as the working directory so all STI
scripts  
# can execute relative to this path.  
WORKDIR ${HOME}  
  
RUN apt-get update && apt-get install -y --no-install-recommends git
libbz2-dev libzip-dev \  
libmcrypt-dev libicu-dev libfreetype6-dev libpcre3-dev libxml2-dev libxslt1.1
libxslt1-dev \  
libjpeg62-turbo-dev libpng12-dev libsqlite3-dev libssl-dev libcurl4-openssl-
dev libgmp-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.cache  
  
#included in php: mysqlnd curl  
ENV PHP_EXTENSIONS="soap iconv intl bz2 gmp mysqli mcrypt xsl zip gd pdo
pdo_mysql pdo_sqlite json dom hash bcmath gettext mbstring simplexml"  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install -j$(nproc) ${PHP_EXTENSIONS} \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/etc/php/conf.d/*
/var/log/* /usr/share/doc/* /usr/share/man/* /root/.cache  
  
ENV PHPREDIS_VERSION=3.1.4 APCU_VERSION=5.1.8 XDEBUG_VERSION=2.5.5  
RUN pecl install apcu-$APCU_VERSION xdebug-$XDEBUG_VERSION
redis-${PHPREDIS_VERSION} \  
&& pear install DB MDB2 Mail Mail_Mime Mail_mimeDecode Log HTTP_Request2
XML_RPC2 Date \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/etc/php/conf.d/*
/var/log/* /usr/share/doc/* /usr/share/man/* /root/.cache  
  
# Install php tools (composer / phpunit)  
RUN cd /tmp && \  
curl -sL https://getcomposer.org/composer.phar > composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
curl -sL https://phar.phpunit.de/phpunit.phar > phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PHP_INI_PATH="/opt/app-root/etc/php.ini" \  
PHP_CLI_INI_PATH="/opt/app-root/etc/php-cli.ini" \  
PHP_FPM_PATH="/opt/app-root/etc/php-fpm.conf" \  
PHP_FPMD_PATH="/opt/app-root/etc/php-fpm.d" \  
PHP_LIB_PATH="/opt/app-root/lib/php"  
RUN mkdir -p $PHP_FPMD_PATH $PHP_LIB_PATH  
ENV OPTS=" --fpm-config=$PHP_FPM_PATH -c $PHP_INI_PATH " \  
OPCACHE__ENABLED=0 APC__ENABLED=0 XDEBUG=1 DATE__TIMEZONE=Europe/Madrid  
  
ADD php.ini $PHP_INI_PATH  
ADD php-cli.ini $PHP_CLI_INI_PATH  
ADD php-fpm.d $PHP_FPMD_PATH  
  
# ADD docker.conf /opt/app-root/etc/php-fpm.d/docker.conf  
# ADD zz-docker.conf /opt/app-root/etc/php-fpm.d/zz-docker.conf  
RUN rm -f /usr/local/etc/php/php.ini && ln -s ${PHP_INI_PATH}
/usr/local/etc/php/ \  
&& { \  
echo '[global]'; \  
echo "include=$PHP_FPMD_PATH/*.conf"; \  
} | tee ${PHP_FPM_PATH} \  
&& sed -i '/include_path/d' $PHP_INI_PATH \  
&& echo
"include_path=\".:$HOME/app/include:$HOME/include:$PHP_LIB_PATH:/usr/local/lib/php:/usr/share/php\""
>> /opt/app-root/etc/php.ini  
  
EXPOSE 9000  
CMD [ "$STI_SCRIPTS_PATH/run" ]  
  
ADD s2i/bin $STI_SCRIPTS_PATH  
  
RUN /usr/bin/docker-footer  
  
USER 1001  

