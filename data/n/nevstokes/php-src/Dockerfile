FROM alpine:3.6 AS src  
  
COPY version.xsl .  
  
RUN apk update && apk add \  
ca-certificates \  
libressl \  
libxslt-dev  
  
RUN wget -q https://secure.php.net/releases/feed.php -O - | xsltproc
version.xsl - > versioninfo  
  
FROM scratch  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
  
COPY \--from=src /versioninfo .  
  
LABEL maintainer="Nev Stokes <mail@nevstokes.com>" \  
description="PHP release versions and hashes" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF  

