FROM ruby:2.4.1-alpine  
  
RUN apk --no-cache add --virtual .build-deps make gcc libc-dev git libffi-dev
\  
&& apk add --no-cache git ca-certificates \  
&& gem install travis -v 1.8.8 --no-rdoc --no-ri \  
&& gem install websocket-native --no-rdoc --no-ri \  
&& apk del --purge .build-deps  
  
VOLUME /project  
VOLUME /travis  
  
ENV TRAVIS_CONFIG_PATH=/travis  
WORKDIR /project  
  
ENTRYPOINT ["/usr/local/bundle/bin/travis"]  

