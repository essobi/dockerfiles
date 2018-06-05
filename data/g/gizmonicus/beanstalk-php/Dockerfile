FROM php:5.6-apache  
  
# Dependencies  
RUN apt-get -y update \  
&& apt-get -y install \  
automake \  
git \  
libicu-dev \  
libldap2-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libssh2-1-dev \  
libxslt1-dev \  
npm \  
unixODBC-dev \  
uuid-dev \  
vim \  
&& apt-get clean  
  
# Fix PHP config errors with stupid library logic.  
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so  
  
# Fix LDAP extension  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
  
# PHP extensions  
RUN docker-php-ext-install \  
bcmath \  
calendar \  
exif \  
gettext \  
gd \  
ldap \  
mysql \  
mysqli \  
mcrypt \  
pdo \  
pdo_mysql \  
# Skipping these deps since we don't use postgres  
# pdo_pgsql -- not installing  
# pdo_sqlite -- not installing  
# pgsql -- not installing  
shmop \  
soap \  
sockets \  
sysvmsg \  
wddx \  
xmlrpc \  
xsl \  
zip  
  
# Magic from https://github.com/docker-library/php/issues/103  
RUN set -x \  
&& docker-php-source extract odbc \  
&& cd /usr/src/php/ext/odbc \  
&& phpize \  
&& sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure
\  
&& ./configure --with-unixODBC=shared,/usr \  
&& docker-php-ext-install odbc  
  
# PECL extensions  
RUN pecl install \  
igbinary \  
imagick \  
memcached \  
memcache \  
# this stupid package doesn't understand dependencies and thinks we need php 7  
# so we have to specify the version  
oauth-1.2.3 \  
ssh2 \  
uuid  
  
# Add extensions to include dir  
RUN touch /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=igbinary.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=imagick.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=memcache.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=memcached.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=oauth.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=ssh2.so" >> /usr/local/etc/php/conf.d/thirdparty.ini \  
&& echo "extension=uuid.so" >> /usr/local/etc/php/conf.d/thirdparty.ini  
  
# Install composer, this needs to be two steps to ensure we get the latest
version  
ADD http://getcomposer.org/installer /tmp/installer  
RUN php /tmp/installer --install-dir=/usr/local/bin && ln -s
/usr/local/bin/composer.phar /usr/local/bin/composer  
  
RUN find /etc/apache2/ -type f -name \\*.conf | while read FN; do sed -i
's/Listen\\(.*\\)80/Listen\18080/g;s/Listen\\(.*\\)443/Listen\18443/g' "$FN";
done  
  
# Add jenkins users  
RUN groupadd -g 496 jenkins && useradd -g jenkins -u 498 jenkins  
  
# Enable rewrite module  
RUN a2enmod rewrite  
  
# Add our filesystem overlay  
ADD ./root_5 /  
  
# Fix the apache user home directory so it doesn't hang when  
# we change the UID (this forces a chown of the home directory  
# which is mapped to a very large network filesystem).  
RUN mkdir /home/www-data && \  
usermod -d /home/www-data www-data && \  
chown -R www-data:www-data /home/www-data  
  
CMD /run.sh  

