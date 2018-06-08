FROM php:5.6-fpm  
  
RUN apt-get -y update && \  
apt-get -y install \  
nginx-full \  
libxml2-dev \  
zlib1g-dev \  
libpspell-dev \  
supervisor && \  
docker-php-ext-install \  
dom \  
json \  
xml \  
mbstring \  
session \  
sockets \  
pdo \  
pdo_mysql \  
iconv \  
fileinfo \  
zip \  
pspell && \  
pear install \  
mail_mime \  
net_smtp \  
net_idna2-beta \  
auth_sasl \  
net_sieve \  
crypt_gpg && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -SL
https://github.com/roundcube/roundcubemail/releases/download/1.2.2/roundcubemail-1.2.2-complete.tar.gz
| tar xvz --strip-components=1 && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
chown -R www-data:www-data /var/www/html  
  
COPY etc/ /etc/  
COPY usr/ /usr/  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

