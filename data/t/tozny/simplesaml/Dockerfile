# Dockerfile written by Eric Mann <eric@tozny.com>  
#  
# Copyright (c) 2017 Tozny, LLC  
FROM php:7.1-alpine  
  
MAINTAINER Eric Mann <eric@tozny.com>  
  
COPY templates /srv/templates  
COPY params.yml.dist /params.default.yml  
  
ENV SSP_VERSION 1.14.11  
ENV SSP_HASH 4899cae8e66967ad9fbf8dd0efe605b3a7c0f7a7c2c7a09e61470d623ca3a878  
  
RUN set -x \  
&& apk add --no-cache openssl  
  
RUN set -x \  
&& buildDeps="ca-certificates wget" \  
&& apk add --no-cache $buildDeps && update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& wget
https://github.com/simplesamlphp/simplesamlphp/releases/download/v$SSP_VERSION/simplesamlphp-$SSP_VERSION.tar.gz
-O /tmp/simplesamlphp-$SSP_VERSION.tar.gz \  
&& echo "$SSP_HASH /tmp/simplesamlphp-$SSP_VERSION.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/simplesamlphp-$SSP_VERSION.tar.gz -C /tmp \  
&& mv /tmp/simplesamlphp-$SSP_VERSION /srv/simplesaml \  
&& rm /tmp/simplesamlphp-$SSP_VERSION.tar.gz \  
&& apk del $buildDeps  
  
ENV TWIT_VERSION 1.1.0  
RUN set -x \  
&& buildDeps="ca-certificates wget" \  
&& apk add --no-cache $buildDeps && update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& wget https://github.com/bander2/twit/releases/download/$TWIT_VERSION/twit-
linux-amd64 \  
-O /usr/local/bin/twit --secure-protocol=TLSv1 \  
&& chmod u+x /usr/local/bin/twit \  
&& mkdir /lib64 \  
&& ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \  
&& apk del $buildDeps  
  
ENV TOZNYAUTH_VERSION 1.0.0  
RUN set -x \  
&& buildDeps="ca-certificates wget" \  
&& apk add --no-cache $buildDeps && update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& wget https://github.com/tozny/simplesamlphp-toznyauth-
external/releases/download/$TOZNYAUTH_VERSION/toznyauth.tgz -O
/tmp/toznyauth.tgz \  
&& tar -xzf /tmp/toznyauth.tgz -C /tmp \  
&& mv /tmp/toznyauth /srv/simplesaml/modules/toznyauth \  
&& touch /srv/simplesaml/modules/toznyauth/enable \  
&& chown -R root:root /srv/simplesaml/modules/toznyauth \  
&& rm /tmp/toznyauth.tgz \  
&& apk del $buildDeps  
  
WORKDIR /srv/simplesaml  
  
VOLUME ["/srv/simplesaml"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

