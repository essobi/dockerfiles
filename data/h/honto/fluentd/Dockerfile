FROM fluent/fluentd:v0.14-latest  
MAINTAINER Tsukasa Tamaru <tsukasa.tamaru@2dfacto.co.jp>  
  
RUN apk add --update --virtual .build-deps \  
build-base ruby-dev sudo \  
&& sudo gem install \  
fluent-plugin-forest \  
fluent-plugin-typecast \  
fluent-plugin-record-reformer \  
fluent-plugin-tail-ex \  
fluent-plugin-parser \  
bson_ext \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
EXPOSE 24284  
EXPOSE 24224  

