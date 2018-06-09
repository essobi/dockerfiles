FROM alpine:3.3  
MAINTAINER James Pamplin <james@jamespamplin.com>  
  
ENV TRAVIS_VERSION 1.8.2  
# Install travis cli and ruby dependencies  
# Also installs dev dependencies (build_deps) for compiling ruby-ffi  
# which are removed after install  
RUN apk add --no-cache ruby ruby-io-console ruby-json git && \  
apk add --no-cache --virtual build_deps \  
build-base ruby-dev libc-dev libffi-dev linux-headers && \  
gem install travis -v ${TRAVIS_VERSION} \--no-rdoc --no-ri && \  
apk del build_deps  
  
# Default travis config directory: ~/.travis  
VOLUME /root/.travis  
  
# Mount your project to /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/usr/bin/travis"]  

