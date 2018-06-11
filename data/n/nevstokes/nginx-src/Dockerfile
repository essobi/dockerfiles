FROM alpine:3.6 AS src  
  
COPY github-releases.xsl .  
  
ARG NGINX_VERSION  
ENV INSTALL_VERSION=$NGINX_VERSION  
  
RUN apk --update add \  
ca-certificates \  
gnupg \  
libressl \  
libxslt-dev  
  
RUN if [ -z $NGINX_VERSION ]; then export INSTALL_VERSION=`wget -q
https://github.com/nginx/nginx/releases.atom -O - | xsltproc /github-
releases.xsl - | awk -F/ '{ print $NF; }' | sed -E 's/release-//' | sort -r
-k1,1 -k2,2 -k3,3 | head -1`; fi \  
&& wget -q https://nginx.org/download/nginx-$INSTALL_VERSION.tar.gz -O
nginx.tar.gz \  
&& wget -q https://nginx.org/download/nginx-$INSTALL_VERSION.tar.gz.asc -O
nginx.tar.gz.asc  
  
# Import key  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \  
B0F4253373F8F6F510D42178520A9993A1C052F8  
  
# Verify  
RUN gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz  
  
# Blank slate  
FROM scratch  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
  
COPY \--from=src /nginx.tar.gz .  
  
LABEL maintainer="Nev Stokes <mail@nevstokes.com>" \  
description="Verified source of nginx" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF  

