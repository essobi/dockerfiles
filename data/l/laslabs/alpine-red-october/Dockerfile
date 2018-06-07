FROM golang:alpine  
MAINTAINER Dave Lasley <dave@laslabs.com>  
  
ENV RO_CERTPASSWD="password" \  
RO_COMMONNAME="localhost" \  
RO_DATA="/var/lib/redoctober/data"  
  
ENV RO_CERTS="${RO_DATA}/server.crt" \  
RO_KEYS="${RO_DATA}/server.pem"  
  
RUN addgroup -S redoctober \  
&& adduser -S -g redoctober redoctober \  
# Add community for runit  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
# Install build dependencies  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
gcc \  
git \  
libtool \  
# Install required applicatons  
&& apk add --no-cache \  
runit \  
openssl \  
# Install Red October  
&& git clone --depth=1 "https://github.com/cloudflare/redoctober.git"
"$GOPATH/src/github.com/cloudflare/redoctober" \  
&& go install github.com/cloudflare/redoctober \  
# Remove dependencies  
&& apk del .build-deps  
  
# Setup Environment  
  
VOLUME ["/var/lib/redoctober/data"]  
  
ENTRYPOINT ["/go/src/github.com/cloudflare/redoctober/scripts/docker-
entrypoint.sh"]  
  
CMD ["redoctober", \  
"-addr=0.0.0.0:8080", \  
"-vaultpath=/var/lib/redoctober/data/diskrecord.json", \  
"-certs=/var/lib/redoctober/data/server.crt", \  
"-keys=/var/lib/redoctober/data/server.pem", \  
"-metrics-host=0.0.0.0", \  
"-metrics-port=8081"]  
  
# Metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Red October - Alpine" \  
org.label-schema.description="Provides a Docker image for Red October on
Alpine Linux." \  
org.label-schema.url="https://laslabs.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/LasLabs/docker-alpine-red-
october" \  
org.label-schema.vendor="LasLabs Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

