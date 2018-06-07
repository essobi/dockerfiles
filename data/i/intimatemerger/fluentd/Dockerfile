FROM fluent/fluentd:v0.12.29  
  
USER root  
  
RUN apk add \--no-cache tzdata build-base ruby-dev && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
gem install fluent-plugin-parser:0.6.1 \  
fluent-plugin-rewrite-tag-filter:1.5.5 \  
fluent-plugin-woothee:0.2.1 \  
fluent-plugin-forest:0.3.1 \  
fluent-plugin-s3:0.7.1 \  
fluent-plugin-td:0.10.29 \  
fluent-plugin-bigquery:0.2.16 bigdecimal && \  
apk del tzdata build-base ruby-dev  
  
USER fluent  
  
ONBUILD COPY fluent.conf /fluentd/etc/

