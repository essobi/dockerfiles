FROM ruby:2.4.1-alpine  
  
RUN echo "@edge http://dl-4.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& BUILD_DEPS=" \  
postgresql-dev \  
libxml2-dev \  
libxslt-dev \  
build-base" \  
&& apk --no-cache add \  
$BUILD_DEPS \  
nodejs@edge \  
nodejs-npm@edge \  
libpq \  
libxml2 \  
libxslt \  
ffmpeg \  
file \  
imagemagick@edge \  
&& npm install -g npm@3 && npm install -g yarn \  
&& rm -rf /tmp/* /var/cache/apk/*  
  

