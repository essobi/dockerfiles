FROM composer  
  
RUN apk --no-cache add freetype freetype-dev libpng libpng-dev libjpeg-turbo
libjpeg-turbo-dev icu icu-dev libxml2 libxml2-dev openssl-dev pcre-dev imap-
dev libedit-dev $PHPIZE_DEPS  
  
# bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap interbase intl json ldap mbstring mysqli oci8 odbc
opcache pcntl pdo pdo_dblib pdo_firebird pdo_mysql pdo_oci pdo_odbc pdo_pgsql
pdo_sqlite pgsql phar posix pspell readline recode reflection session shmop
simplexml snmp soap sockets sodium spl standard sysvmsg sysvsem sysvshm tidy
tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zend_test zip  
RUN docker-php-ext-install gd intl json mbstring soap readline  
  
RUN pecl install mongodb apcu  

