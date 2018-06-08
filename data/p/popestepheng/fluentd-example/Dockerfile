FROM fluent/fluentd:v0.12-onbuild  
MAINTAINER Kevin Kaland <kevin@projectricochet.com>  
  
RUN apk add --update --virtual .build-deps \  
sudo build-base ruby-dev \  
&& sudo gem install \  
fluent-plugin-secure-forward \  
fluent-plugin-elasticsearch \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
EXPOSE 24284 5170  

