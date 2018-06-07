FROM evild/alpine-php:7.0.8  
ARG DOKUWIKI_VERSION=2016-06-26a  
ARG MD5_CHECKSUM=9b9ad79421a1bdad9c133e859140f3f2  
  
RUN apk add --no-cache --virtual .build-deps \  
autoconf gcc libc-dev make \  
libpng-dev libjpeg-turbo-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd opcache \  
&& find /usr/local/lib/php/extensions -name '*.a' -delete \  
&& find /usr/local/lib/php/extensions -name '*.so' -exec strip --strip-all
'{}' \; \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive \  
/usr/local/lib/php/extensions \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .phpext-rundeps $runDeps \  
&& apk del .build-deps  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
VOLUME /var/www/html  
  
RUN curl -o dokuwiki-$DOKUWIKI_VERSION.tgz -SL
http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz \  
&& echo "$MD5_CHECKSUM dokuwiki-$DOKUWIKI_VERSION.tgz" | md5sum -c - \  
&& tar xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" -C /usr/src/ \  
&& rm dokuwiki-$DOKUWIKI_VERSION.tgz \  
&& mv /usr/src/dokuwiki-$DOKUWIKI_VERSION /usr/src/dokuwiki \  
&& chown -R www-data:www-data /usr/src/dokuwiki  
  
ADD root /  

