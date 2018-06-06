FROM fluent/fluentd:v1.0.2-onbuild  
  
RUN apk add --update --virtual .build-deps sudo build-base ruby-dev \  
&& sudo gem install fluent-plugin-elasticsearch -v 2.4.1 \--no-document \  
&& sudo gem install fluent-plugin-rewrite-tag-filter --no-document \  
&& sudo gem install fluent-plugin-http-pull --no-document \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* /home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
ENTRYPOINT fluentd -c /fluentd/etc/${FLUENTD_CONF} -p /fluentd/plugins
$FLUENTD_OPT  

