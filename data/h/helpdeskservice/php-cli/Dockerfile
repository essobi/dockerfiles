FROM php:7.2.3-fpm-alpine  
  
RUN apk add --update --no-cache c-client curl bash \  
gettext-libs gmp icu-libs libbz2 libgd libintl \  
libldap libmcrypt libsasl libxslt \  
openssh-client rsync tidyhtml-libs wget &&\  
apk add --no-cache --virtual build-dependencies \  
autoconf bzip2-dev g++ gcc gettext-dev gmp-dev \  
icu-dev imap-dev libffi-dev libjpeg-turbo-dev \  
libmcrypt-dev libpng-dev libxml2-dev libxslt-dev \  
make openldap-dev pcre-dev tidyhtml-dev &&\  
docker-php-ext-install -j4 bcmath bz2 calendar exif \  
gd gettext gmp imap intl ldap mysqli opcache\  
pcntl pdo_mysql shmop soap sockets sysvmsg sysvsem sysvshm \  
tidy wddx xmlrpc xsl zip &&\  
yes | pecl install igbinary mcrypt-1.0.1 mongodb oauth redis xdebug &&\  
docker-php-ext-enable igbinary mcrypt mongodb oauth redis &&\  
pear channel-discover pear.phing.info && pear install phing/phing &&\  
apk del build-dependencies  
  
COPY configs/ /  
  
EXPOSE 9000  
  
CMD ["php-fpm"]

