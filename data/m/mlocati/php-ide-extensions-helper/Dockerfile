FROM php:7.2-cli  
  
ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-
installer/master/install-php-extensions /usr/local/bin/  
  
# Install all extensions listed by docker-php-ext-install (listed with `docker
run -ti --rm php:7.2-cli docker-php-ext-install`), except:  
# Already installed extensions:  
# ctype  
# curl  
# dom  
# fileinfo  
# filter  
# ftp  
# hash  
# iconv  
# json  
# mbstring  
# pdo  
# pdo_sqlite  
# phar  
# posix  
# readline  
# reflection  
# session  
# simplexml  
# sodium  
# spl  
# standard  
# tokenizer  
# xml  
# xmlreader  
# xmlwriter  
# Depending on Oracle Instant Client, which requires an Oracle account:  
# oci8  
# pdo_oci  
RUN chmod uga+x /usr/local/bin/install-php-extensions && sync && install-php-
extensions \  
# Core extensions  
bcmath \  
bz2 \  
calendar \  
dba \  
enchant \  
exif \  
gd \  
gettext \  
gmp \  
imap \  
interbase \  
intl \  
ldap \  
mcrypt \  
mysqli \  
odbc \  
opcache \  
pcntl \  
pdo_dblib \  
pdo_firebird \  
pdo_mysql \  
pdo_odbc \  
pdo_pgsql \  
pgsql \  
pspell \  
recode \  
shmop \  
snmp \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
tidy \  
wddx \  
xmlrpc \  
xsl \  
zend_test \  
zip \  
# PECL extensions  
apcu \  
imagick \  
memcached \  
pdo_sqlsrv \  
redis \  
sqlsrv \  
ssh2 \  
timezonedb \  
uuid \  
xdebug \  
yaml \  
# Extensions from source  
cmark \  
&& true  

