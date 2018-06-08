FROM golang:1.7-alpine  
MAINTAINER Zadkiel Aharonian <aslafy_z@epitech.eu>  
  
ENV APPENGINE_VERSION=1.9.48  
ENV SDK=https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-${APPENGINE_VERSION}.zip \  
PACKAGES="curl unzip" \  
PATH=/google_appengine:${PATH} \  
GOROOT=/usr/local/go  
  
RUN apk add \--update \--no-cache gcc musl-dev git python ${PACKAGES} && \  
curl -fo /tmp/gae.zip ${SDK} && unzip -q /tmp/gae.zip -d /tmp/ && mv
/tmp/go_appengine /google_appengine && \  
apk del ${PACKAGES} \--no-cache && rm -rf /tmp/* /var/cache/apk/*  

