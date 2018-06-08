FROM ruby:2.4.2-alpine3.4  
MAINTAINER goya "rudd@adobe.com"  
  
ENV BUILD_PACKAGES="curl ca-certificates ruby-dev build-base" \  
DEV_PACKAGES="zlib-dev libxml2-dev libxslt-dev tzdata yaml-dev mysql-dev
openssl" \  
RUBY_PACKAGES="ruby ruby-io-console nodejs ruby-json yaml git tree unzip zip
sqlite-dev" \  
RAILS_ENV="production" \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  
  
RUN apk --update --upgrade add $BUILD_PACKAGES $RUBY_PACKAGES $DEV_PACKAGES &&
\  
wget http://github.com/git-lfs/git-lfs/releases/download/v2.2.1/git-lfs-linux-
amd64-2.2.1.tar.gz && \  
tar xvf git-lfs-linux-amd64-2.2.1.tar.gz && \  
cp git-lfs-2.2.1/git-lfs /usr/local/bin && \  
rm -rf git-lfs* && \  
addgroup -g 1000 www && adduser -u 1000 -G www -S -s /bin/sh -D www && \  
su -l www -c 'git lfs install'

