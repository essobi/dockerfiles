FROM alpine:3.5  
  
ARG JEKYLL_VERSION=3.4.3  
ARG HTMLPROOFER_VERSION=3.6.0  
  
RUN apk add --no-cache --virtual .build-dependencies \  
build-base \  
libffi-dev \  
libxml2-dev \  
readline-dev \  
ruby-dev \  
yaml-dev \  
zlib-dev \  
&& \  
apk add --no-cache \  
curl \  
openssh \  
rsync \  
ruby \  
ruby-json \  
&& \  
gem install --no-document \  
jekyll:${JEKYLL_VERSION} \  
html-proofer:${HTMLPROOFER_VERSION} \  
&& \  
apk del .build-dependencies

