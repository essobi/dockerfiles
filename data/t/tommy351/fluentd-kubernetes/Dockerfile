FROM fluent/fluentd:v0.12-onbuild  
  
RUN apk add \--update \--no-cache \--virtual .build-deps sudo build-base ruby-
dev && \  
sudo gem install fluent-plugin-kubernetes_metadata_filter && \  
sudo gem install fluent-plugin-elasticsearch -v '~> 1.0' && \  
sudo gem sources \--clear-all && \  
apk del .build-deps && \  
rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  

