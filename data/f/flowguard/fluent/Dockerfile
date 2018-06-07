FROM fluent/fluentd:latest  
  
# below RUN includes plugin as examples elasticsearch is not required  
# you may customize including plugins as you wish  
  
RUN apk add --update krb5-libs && \  
apk add --update --virtual .build-deps libffi-dev \  
sudo build-base ruby-dev && \  
sudo gem install fluent-plugin-kafka \  
fluent-plugin-influxdb \  
fluent-plugin-rewrite-tag-filter \  
fluent-plugin-record-modifier \  
fluent-plugin-juniper-telemetry \  
fluent-plugin-snmp \  
fluent-plugin-elasticsearch \  
bigdecimal \  
zookeeper && \  
sudo gem sources --clear-all && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  

