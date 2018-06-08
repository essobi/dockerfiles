FROM golang:1.6.3-alpine  
  
RUN apk add --no-cache ca-certificates  
  
ENV APPENGINE_VERSION=1.9.46  
ENV HOME=/root  
ENV SDK=https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-${APPENGINE_VERSION}.zip \  
PACKAGES="curl unzip git python alpine-sdk" \  
PATH=${HOME}/go_appengine:${PATH} \  
GOROOT=/usr/local/go  
  
RUN apk add --update \--no-cache ${PACKAGES} && \  
curl -fo /tmp/gae.zip ${SDK} && unzip -q /tmp/gae.zip -d /tmp/ && mv
/tmp/go_appengine ${HOME}/go_appengine && \  
rm /tmp/gae.zip  
RUN curl -s https://glide.sh/get | sh  

