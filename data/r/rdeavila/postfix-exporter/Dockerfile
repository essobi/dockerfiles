FROM ruby:2.3-alpine  
  
ARG GEM_VERSION="> 0"  
RUN apk update \  
&& apk add build-base \  
&& gem install postfix-exporter -v "$GEM_VERSION" \  
&& apk del build-base \  
&& rm -f /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bundle/bin/postfix-exporter"]  

