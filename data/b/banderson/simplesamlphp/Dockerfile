FROM alpine:latest  
  
MAINTAINER brendan_anderson@hcpss.org  
  
LABEL vendor=Howard\ County\ Public\ School\ System \  
org.hcpss.version="1.0.0" \  
org.hcpss.name="hub_sp"  
  
ENV SAML_VERSION 1.14.4  
COPY templates /srv/templates  
COPY params.yml.dist /params.default.yml  
  
# Get SimpleSAMLPHP.  
RUN set -xe \  
&& buildDeps="wget ca-certificates" \  
&& apk add --no-cache $buildDeps \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& wget
https://simplesamlphp.org/res/downloads/simplesamlphp-${SAML_VERSION}.tar.gz \  
-O /tmp/simplesamlphp-${SAML_VERSION}.tar.gz --no-check-certificate \  
&& tar -zxf /tmp/simplesamlphp-${SAML_VERSION}.tar.gz -C /tmp \  
&& mv /tmp/simplesamlphp-${SAML_VERSION} /srv/simplesaml \  
&& wget https://github.com/bander2/twit/releases/download/1.0.0/twit-linux-
amd64 \  
-O /usr/local/bin/twit --secure-protocol=TLSv1 \  
&& chmod u+x /usr/local/bin/twit \  
&& mkdir /lib64 \  
&& ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \  
&& apk del $buildDeps  
  
WORKDIR /srv/simplesaml  
  
VOLUME ["/srv/simplesaml"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

