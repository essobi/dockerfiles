FROM alpine:3.7  
MAINTAINER Rómulo Rodríguez rodriguezrjrr@gmail.com  
  
# Update system and install php5  
RUN apk upgrade --no-cache \  
&& apk add --no-cache \  
apache2 \  
apache2-utils \  
libressl \  
php5 \  
php5-apache2 \  
php5-apcu \  
php5-bcmath \  
php5-bz2 \  
php5-calendar \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-enchant \  
php5-ftp \  
php5-gd \  
php5-gettext \  
php5-gmp \  
php5-iconv \  
php5-imap \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-mssql \  
php5-mysql \  
php5-odbc \  
php5-opcache \  
php5-openssl \  
php5-pdo \  
php5-pdo_mysql \  
php5-pdo_odbc \  
php5-pdo_pgsql \  
php5-pdo_sqlite \  
php5-pgsql \  
php5-phar \  
php5-posix \  
php5-pspell \  
php5-soap \  
php5-sockets \  
php5-sqlite3 \  
php5-xml \  
php5-xmlreader \  
php5-xmlrpc \  
php5-xsl \  
php5-zip \  
php5-zlib \  
supervisor \  
tzdata  
  
# Get Processmaker CE  
RUN mkdir -p "/opt" \  
&& wget -O "/opt/processmaker-3.2.1-community.tar.gz" \  
"https://superb-
dca2.dl.sourceforge.net/project/processmaker/ProcessMaker/3.2.1/processmaker-3.2.1-community.tar.gz"  
# Apache Port  
EXPOSE 80  
# Insert init script  
COPY docker-entrypoint.sh /bin/  
COPY httpd.conf /etc/apache2  
RUN chmod a+x /bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
  
  
  

