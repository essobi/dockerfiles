FROM ruby:2.2.5-alpine  
  
LABEL com.tomasbasham.maintainer "Tomas Basham <me@tomasbasham.co.uk>" \  
com.tomasbasham.version "1.8.8" \  
com.tomasbasham.description "Travis CI Command Line Interface & Ruby Library"  
  
ENV VERSION 1.8.8  
# Install travis  
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \  
&& apk add --no-cache git \  
&& gem install travis -v ${VERSION} \--no-rdoc --no-ri \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["travis"]  
CMD ["help"]  

