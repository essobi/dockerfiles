FROM alpine:3.6  
ENV UID=991 GID=991  
RUN apk --no-cache -U add nginx s6 su-exec ca-certificates openssl php7-fpm \  
php7-curl php7-iconv php7-xml php7-dom php7-openssl php7-json \  
php7-zlib php7-pdo_mysql php7-pdo_sqlite php7-sqlite3 php7-ldap \  
php7-opcache  
  
RUN wget -q "https://www.rainloop.net/repository/webmail/rainloop-community-
latest.zip" -O /tmp/rainloop.zip  
  
RUN cd /tmp \  
&& mkdir /rainloop \  
&& unzip -q /tmp/rainloop.zip -d /rainloop \  
&& find /rainloop -type d -exec chmod 755 {} \; \  
&& find /rainloop -type f -exec chmod 644 {} \;  
  
RUN rm -rf /tmp/* /var/cache/apk/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /rainloop/data  
  
EXPOSE 8888  
CMD ["run.sh"]

