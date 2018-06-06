FROM php:5.6.24-apache  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y install build-essential apache2-utils  
  
# install ODBC connector  
COPY odbc/odbc-sqlserver-1.9.0-linux-x86-64-ul64.tar /var/www/odbc-
sqlserver-1.9.0-linux-x86-64-ul64.tar  
RUN cd /var/www/ && tar -xf /var/www/odbc-
sqlserver-1.9.0-linux-x86-64-ul64.tar  
  
RUN apt-get -qqy update \  
&& apt-get install -y libpng12-dev libjpeg-dev \  
&& apt-get -y install re2c libmcrypt-dev \  
&& apt-get -y install zlib1g-dev \  
&& apt-get -y install libssl-dev libc-client2007e-dev libkrb5-dev \  
&& apt-get -y install libcurl4-gnutls-dev \  
&& apt-get -y install libxml2-dev libxslt-dev \  
&& apt-get -y install libssl-dev \  
&& apt-get -y install libcurl4-openssl-dev  
  
RUN docker-php-ext-install bcmath \  
&& docker-php-ext-configure gd \--with-jpeg-dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip  
  
## install redis - note temporarily excluding because install via PECL require
PHP >= v7  
#RUN pecl install redis  
#RUN docker-php-ext-enable redis  
# install xhprof  
RUN pecl install xhprof-beta  
RUN docker-php-ext-enable xhprof  
  
# enable base apache modules  
RUN a2enmod access_compat actions alias allowmethods auth_basic auth_digest
authn_anon authn_core authn_dbd authn_dbm authn_file authn_socache authz_core
authz_dbd authz_dbm authz_groupfile authz_host authz_owner authz_user
autoindex cache cache_disk data dbd deflate dir dump_io echo env expires
ext_filter filter headers include info log_debug mime_magic mime negotiation
remoteip reqtimeout request rewrite setenvif slotmem_plain slotmem_shm
socache_dbm socache_memcache socache_shmcb status substitute suexec unique_id
userdir vhost_alias  
  
# enable dav modules  
RUN a2enmod dav dav_fs dav_lock  
  
# enable lua module  
RUN a2enmod lua  
  
# enable mpm module  
#RUN a2enmod mpm_event  
# enable modules required for proxy  
RUN a2enmod proxy proxy_html proxy_http xml2enc lbmethod_bybusyness
lbmethod_byrequests lbmethod_bytraffic lbmethod_heartbeat proxy_ajp
proxy_balancer proxy_connect proxy_express proxy_fcgi proxy_fdpass proxy_ftp
proxy_scgi  
  
# enable ssl module  
RUN a2enmod ssl  
  
# enable systemd module  
#RUN a2enmod systemd  
RUN service apache2 restart  
  
EXPOSE 80  
EXPOSE 443  
  
VOLUME ["/var/www/html"]

