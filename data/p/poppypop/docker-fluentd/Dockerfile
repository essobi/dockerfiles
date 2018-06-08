FROM fluent/fluentd:onbuild  
  
# below RUN includes plugin as examples elasticsearch is not required  
# you may customize including plugins as you wish  
  
RUN apk add --update --virtual .build-deps \  
sudo build-base ruby-dev \  
&& sudo gem install \  
fluent-plugin-elasticsearch \  
fluent-plugin-record-reformer \  
fluent-plugin-xml-parser \  
fluent-plugin-tail-multiline-ex \  
fluent-plugin-parser \  
fluent-plugin-concat \  
fluent-plugin-rewrite-tag-filter \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem

