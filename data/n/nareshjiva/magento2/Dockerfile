FROM debian:jessie  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# for MYSQL_RANDOM_ROOT_PASSWORD  
pwgen \  
# for mysql_ssl_rsa_setup  
openssl \  
# FATAL ERROR: please install the following Perl modules before executing
/usr/local/mysql/scripts/mysql_install_db:  
# File::Basename  
# File::Copy  
# Sys::Hostname  
# Data::Dumper  
perl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-
build@oss.oracle.com>" imported  
key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list > /dev/null  
  
ENV MYSQL_MAJOR 8.0  
ENV MYSQL_VERSION 8.0.3-rc-1debian8  
  
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list  
  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select
false; \  
} | debconf-set-selections \  
&& apt-get update && apt-get install -y mysql-community-client-
core="${MYSQL_VERSION}" mysql-community-server-core="${MYSQL_VERSION}" && rm
-rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
VOLUME /var/lib/mysql  
# Config files  
COPY config/ /etc/mysql/  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306 80 443 22 2222  
CMD ["mysqld"]  
FROM alexcheng/apache2-php7:7.1.11  
MAINTAINER Fu Cheng <alexcheng1982@gmail.com>  
  
RUN a2enmod rewrite  
  
ENV MAGENTO_VERSION 2.2.2  
RUN rm -rf /var/www/html/* \  
&& apt-get update \  
&& apt-get install -y wget  
  
RUN cd /tmp && curl
https://codeload.github.com/magento/magento2/tar.gz/$MAGENTO_VERSION -o
$MAGENTO_VERSION.tar.gz && tar xvf $MAGENTO_VERSION.tar.gz && mv
magento2-$MAGENTO_VERSION/* magento2-$MAGENTO_VERSION/.htaccess /var/www/html  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev
libfreetype6 libjpeg-turbo8 libjpeg-turbo8-dev libpng12-dev libfreetype6-dev
libicu-dev libxslt1-dev" \  
&& apt-get install -y $requirements \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-install soap \  
&& requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev
libfreetype6-dev libjpeg-turbo8-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove  
  
COPY ./auth.json /var/www/.composer/  
RUN chsh -s /bin/bash www-data  
RUN chown -R www-data:www-data /var/www  
RUN su www-data -c "cd /var/www/html && composer install"  
RUN cd /var/www/html \  
&& find . -type d -exec chmod 770 {} \; \  
&& find . -type f -exec chmod 660 {} \; \  
&& chmod u+x bin/magento  
  
RUN su www-data -c "cd /var/www/html && composer config repositories.magento
composer https://repo.magento.com/"  
  
COPY ./bin/install-magento /usr/local/bin/install-magento  
RUN chmod +x /usr/local/bin/install-magento  
  
COPY ./bin/install-sampledata /usr/local/bin/install-sampledata  
RUN chmod +x /usr/local/bin/install-sampledata  
  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Commented out the next 3 lines, because i don't see no use of this  
WORKDIR /var/www/html  
#VOLUME /var/www/html/var  
#VOLUME /var/www/html/pub  
# Add cron job  
ADD crontab /etc/cron.d/magento2-cron  
RUN chmod 0644 /etc/cron.d/magento2-cron \  
&& crontab -u www-data /etc/cron.d/magento2-cron

