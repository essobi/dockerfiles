FROM alpine:3.5  
LABEL description "Rainloop is a simple, modern & fast web-based client" \  
maintainer="Hardware <contact@meshup.net>"  
  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
ARG GPG_FINGERPRINT="3B79 7ECE 694F 3B7B 70F3 11A4 ED7C 49D9 87DA 4591"  
ENV UID=991 GID=991  
RUN echo "http://php.codecasts.rocks/7.1" >> /etc/apk/repositories &&
BUILD_DEPS=" \  
gnupg \  
openssl \  
wget" \  
&& apk --no-cache -U add \  
${BUILD_DEPS} \  
ca-certificates \  
nginx \  
s6 \  
su-exec \  
php7-fpm \  
php7-curl \  
php7-iconv \  
php7-xml \  
php7-dom \  
php7-openssl \  
php7-json \  
php7-zlib \  
php7-pdo_mysql \  
php7-pdo_sqlite \  
php7-sqlite3 \  
php7-ldap \  
php7-opcache  
  
RUN cd /tmp \  
&& wget -q https://www.rainloop.net/repository/webmail/rainloop-community-
latest.zip \  
&& wget -q https://www.rainloop.net/repository/webmail/rainloop-community-
latest.zip.asc \  
&& wget -q https://www.rainloop.net/repository/RainLoop.asc \  
&& echo "Verifying authenticity of rainloop-community-latest.zip using GPG..."
\  
&& gpg --import RainLoop.asc \  
&& FINGERPRINT="$(LANG=C gpg --verify rainloop-community-latest.zip.asc
rainloop-community-latest.zip 2>&1 \  
| sed -n "s#Primary key fingerprint: \\(.*\\)#\1#p")" \  
&& if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" &&
exit 1; fi \  
&& if [ "${FINGERPRINT}" != "${GPG_FINGERPRINT}" ]; then echo "Warning! Wrong
GPG fingerprint!" && exit 1; fi \  
&& echo "All seems good, now unzipping rainloop-community-latest.zip..." \  
&& mkdir /rainloop && unzip -q /tmp/rainloop-community-latest.zip -d /rainloop
\  
&& find /rainloop -type d -exec chmod 755 {} \; \  
&& find /rainloop -type f -exec chmod 644 {} \; \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /tmp/* /var/cache/apk/* /root/.gnupg  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /rainloop/data  
  
EXPOSE 8888  
CMD ["run.sh"]  

