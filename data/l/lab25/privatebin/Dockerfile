FROM php:7.2-apache-stretch  
  
ARG PRIVATEBIN_VERSION=1.1.1  
ARG TINI_VERSION=0.16.1  
ARG
TINI_URL=https://github.com/krallin/tini/releases/download/v${TINI_VERSION}  
ARG
PRIVATEBIN_URL=https://github.com/PrivateBin/PrivateBin/archive/${PRIVATEBIN_VERSION}.tar.gz  
ARG
PRIVATEBIN_ASC_URL=https://github.com/PrivateBin/PrivateBin/releases/download/${PRIVATEBIN_VERSION}/PrivateBin-${PRIVATEBIN_VERSION}.tar.gz.asc  
  
COPY trustedkeys-tini.gpg .  
RUN curl -LOO "${TINI_URL}/{tini-amd64,tini-amd64.asc}" && \  
gpgv --keyring `pwd`/trustedkeys-tini.gpg tini-amd64.asc tini-amd64 && \  
mv tini-amd64 /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini && \  
rm tini-amd64.asc trustedkeys-tini.gpg && \  
rm -rf /root/.gnupg  
  
# Install PHP extensions  
RUN set -xe; \  
apt-get update; \  
savedAptMark="$(apt-mark showmanual)"; \  
apt-get install -y --no-install-recommends \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libpq-dev \  
curl \  
; \  
docker-php-ext-configure gd --with-freetype-dir=/usr --with-jpeg-dir=/usr
--with-png-dir=/usr; \  
docker-php-ext-install -j$(nproc) gd pdo_pgsql opcache; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
RUN { \  
echo 'opcache.enable=1'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.save_comments=1'; \  
echo 'opcache.revalidate_freq=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini;  
  
RUN a2enmod rewrite  
  
COPY trustedkeys-privatebin.gpg .  
RUN set -xe; \  
cd /var/www/html/; \  
curl -o privatebin.tar.gz -L $PRIVATEBIN_URL; \  
curl -o privatebin.tar.gz.asc -L $PRIVATEBIN_ASC_URL; \  
gpgv --keyring `pwd`/trustedkeys-privatebin.gpg privatebin.tar.gz.asc
privatebin.tar.gz && \  
tar xf privatebin.tar.gz --strip 1; \  
mv .htaccess.disabled .htaccess; \  
rm privatebin.tar.gz privatebin.tar.gz.asc trustedkeys-privatebin.gpg  
  
RUN set -xe; \  
mv cfg/conf.sample.php cfg/conf.php; \  
sed -i 's/limit = 10/limit = 0/' cfg/conf.php; \  
sed -i 's/fileupload = false/fileupload = true/' cfg/conf.php; \  
sed -i 's/burnafterreadingselected = false/burnafterreadingselected = true/'
cfg/conf.php; \  
sed -i 's/default = "1week"/default = "1hour"/' cfg/conf.php; \  
sed -i 's/class = Filesystem/class = Database/' cfg/conf.php; \  
perl -i.orig -0pe 's/\\[model_options\\]\ndir = PATH
"data"/[model_options]\n;dir = PATH "data"/' cfg/conf.php; \  
rm cfg/conf.php.orig  
  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["tini", "--", "entrypoint.sh"]  
CMD ["apache2-foreground"]  

