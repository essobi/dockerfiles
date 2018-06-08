FROM ruby:2.3-alpine  
MAINTAINER Vinson Zou <vinsoncou@gmail.com>  
  
ENV BUILD_PACKAGES="curl-dev ruby-dev build-base bash" \  
DEV_PACKAGES="zlib-dev libxml2-dev libxslt-dev tzdata yaml-dev mysql-dev"  
# Update and install base packages and nokogiri gem that requires a native
compilation  
RUN apk update && \  
apk upgrade && \  
apk add --update\  
$BUILD_PACKAGES \  
$DEV_PACKAGES && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /app  

