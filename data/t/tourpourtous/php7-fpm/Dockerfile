FROM debian:jessie  
  
MAINTAINER Ernesto Baez <ernesto@tourpourtous.com>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV XDEBUG_ENABLED 0  
RUN apt-get update && apt-get install -y wget apt-utils\  
&& echo "deb http://cdn.content-network.net/mirror/dotdeb/ jessie all" >>
/etc/apt/sources.list \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg \  
&& apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpcre3 libpcre3-dev librecode0 libsqlite3-0 libxml2 php7.0-mbstring\  
php7.0-fpm php7.0 php7.0-gd php7.0-cgi php7.0-dbg php7.0-xdebug \  
sqlite php7.0-sqlite3 imagemagick php7.0-imagick php7.0-imap \  
php7.0-curl php7.0-mcrypt php7.0-xml php7.0-odbc php7.0-pgsql git \  
php7.0-json php7.0-zip php7.0-mysql php7.0-bz2 php7.0-dev php7.0-intl  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY etc/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN chmod ug+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm7.0", "-c", "/etc/php/7.0/fpm", "--fpm-config",
"/etc/php/7.0/fpm/php-fpm.conf", "-F"]  

