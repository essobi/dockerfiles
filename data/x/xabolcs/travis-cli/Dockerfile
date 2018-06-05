# https://github.com/travis-ci/travis.rb#installation  
FROM ruby:2-alpine  
  
RUN set -ex; \  
apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
; \  
gem install travis ; \  
apk del .build-deps; \  
apk update ; \  
apk add git  
  
# Location where travis config stored  
ENV TRAVIS_CONFIG_PATH /travis  
VOLUME /travis  
  
# Generally the current working dir will be used as the repo volume  
VOLUME /repo  
WORKDIR /repo  
  
ENTRYPOINT ["travis"]  

