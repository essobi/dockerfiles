FROM php:5.6.7  
# Buildpack  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
openssh-client \  
bzip2 \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# PHP  
  
RUN apt-get update && \  
\  
apt-get install -y --no-install-recommends \  
libldap2-dev \  
libldb-dev \  
libmcrypt-dev \  
libsodium-dev \  
zlib1g-dev  
  
RUN docker-php-ext-install \  
zip \  
mbstring \  
pdo_mysql && \  
\  
pecl install \  
libsodium-1.0.6 \  
xdebug && \  
\  
echo "zend_extension=xdebug.so" > "$(php-config
--prefix)/etc/php/conf.d/xdebug.ini" && \  
echo "extension=libsodium.so" > "$(php-config
--prefix)/etc/php/conf.d/libsodium.ini"  
  
RUN docker-php-ext-configure \  
ldap --with-libdir="lib/x86_64-linux-gnu" && \  
\  
docker-php-ext-install \  
mcrypt \  
ldap  
  
# Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
\  
php composer-setup.php --install-dir="/usr/local/bin" \--filename="composer"
&& \  
\  
rm composer-setup.php  

