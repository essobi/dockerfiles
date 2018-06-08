FROM php:7.1-fpm-alpine  
MAINTAINER Simon Erhardt <hello@rootlogin.ch>  
  
ARG DOKUWIKI_VERSION=2017-02-19e  
ARG DOKUWIKI_CSUM=09bf175f28d6e7ff2c2e3be60be8c65f  
ARG UID=1512  
ARG GID=1512  
  
ENV INSTALL=0  
  
ADD root /  
  
RUN set -ex \  
  
# Install important stuff  
&& apk add \--update --no-cache \  
alpine-sdk \  
autoconf \  
nginx \  
openssl \  
pcre \  
pcre-dev \  
supervisor \  
tar \  
tini \  
wget \  
  
# Install php plugins  
&& pecl install APCu-5.1.8 \  
&& docker-php-ext-enable apcu \  
  
# Remove dev packages  
&& apk del --no-cache \  
alpine-sdk \  
autoconf \  
pcre-dev \  
  
# Add user for dokuwiki  
&& addgroup -g ${GID} dokuwiki \  
&& adduser -u ${UID} -h /opt/dokuwiki -H -G dokuwiki -s /sbin/nologin -D
dokuwiki \  
&& mkdir -p /opt/dokuwiki \  
  
# Install dokuwiki  
&& wget -q -O /tmp/dokuwiki.tgz
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" \  
&& if [ "$DOKUWIKI_CSUM" != "$(md5sum /tmp/dokuwiki.tgz | awk '{print($1)}')"
]; then echo "Wrong md5sum of downloaded file!"; exit 1; fi \  
&& tar -zxf /tmp/dokuwiki.tgz -C /opt/dokuwiki \--strip-components=1 \  
&& rm /tmp/dokuwiki.tgz \  
&& chmod +x /usr/local/bin/docker-run.sh  
  
VOLUME ["/data"]  
EXPOSE 80  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD /usr/local/bin/docker-run.sh  

