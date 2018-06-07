FROM fluent/fluentd:onbuild  
USER root  
RUN apk add --update --virtual .build-deps \  
build-base ruby-dev \  
  
# cutomize following instruction as you wish  
&& gem install \  
fluent-plugin-elasticsearch \  
fluent-plugin-record-reformer \  
fluent-plugin-concat \  
  
&& gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
WORKDIR /  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

