FROM php:apache  
RUN apt-get update \  
&& apt-get -y install bash git ssh libmcrypt-dev openssl libsodium-dev libgmp-
dev libgmp3-dev \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install -j$(nproc) mcrypt gmp \  
&& pecl install libsodium \  
&& docker-php-ext-enable libsodium \  
&& git clone https://github.com/VostroNet/looking-glass.git \--branch master
--single-branch /var/www/html/ \  
&& apt-get purge -y \--auto-remove git \  
&& mkdir -p /var/log/ \  
&& touch /var/log/looking-glass.log \  
&& chown www-data /var/log/looking-glass.log  
  
  
#bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap interbase intl json ldap mbstring mcrypt mysqli
oci8 odbc opcache pcntl pdo  
# pdo_dblib pdo_firebird pdo_mysql pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql
phar posix pspell readline recode reflection session shmop simplexml snmp soap
sockets spl standard sysvmsg  
# sysvsem sysv  
#shm tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zip  

