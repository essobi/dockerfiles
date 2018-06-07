FROM alpine:latest  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
TERM="xterm" \  
PGDATA=/var/lib/postgresql/data  
  
COPY entrypoint.sh /entrypoint.sh  
COPY doctrine.sh /usr/bin/doctrine  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --update add \  
git \  
curl \  
postgresql \  
php7 \  
php7-curl \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-openssl \  
php7-pdo \  
php7-pdo_pgsql \  
php7-phar \  
php7-xml \  
php7-zip \  
php7-zlib \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /usr/bin/php7 /usr/bin/php \  
&& curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& chmod +x /usr/local/bin/gosu \  
&& curl -L -o /usr/bin/doctrine-migrations
https://github.com/doctrine/migrations/releases/download/1.4.1/doctrine-
migrations.phar \  
&& chmod a+x /usr/bin/doctrine-migrations \  
&& doctrine-migrations --version \  
&& chmod a+x /entrypoint.sh \  
&& chmod a+x /usr/bin/doctrine \  
&& mkdir /migrations  
  
COPY php.ini /etc/php7/conf.d/50-setting.ini  
COPY config /config  
  
VOLUME /var/lib/postgresql/data  
  
EXPOSE 5432  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["postgres"]  

