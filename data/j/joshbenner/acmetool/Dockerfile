FROM quay.io/justcontainers/base-alpine:v0.11.1  
ENV ACMETOOL_VERSION=0.0.58 \  
CONFD_VERSION=0.12.0-alpha3 \  
ACME_EMAIL=changeme@example.com \  
ACME_SERVER=https://acme-staging.api.letsencrypt.org/directory \  
ACME_AGREEMENT=changeme \  
CERT_DOMAINS="example.com www.example.com" \  
HAPROXY_ALWAYS_GENERATE=yes  
  
# cron.d keeps acmetool from complaining.  
RUN apk --no-cache add nginx && \  
apk --no-cache add --virtual .download-deps curl tar && \  
cd /usr/local/bin && \  
curl -L
https://github.com/hlandau/acme/releases/download/v$ACMETOOL_VERSION/acmetool-v$ACMETOOL_VERSION-
linux_amd64.tar.gz | tar xz --strip-components=2 acmetool-v$ACMETOOL_VERSION-
linux_amd64/bin/acmetool && \  
apk del .download-deps && \  
mkdir /etc/cron.d  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /usr/local/bin/confd  
  
COPY rootfs /  
  
RUN chmod +x /usr/local/bin/confd /etc/periodic/daily/*  
  
EXPOSE 80  
ENTRYPOINT ["/init"]  

