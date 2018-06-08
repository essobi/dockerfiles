FROM fluent/fluentd:v1.1-onbuild  
USER root  
  
WORKDIR /home/fluent  
RUN apk --no-cache --update add \  
build-base \  
ruby-dev tzdata && \  
gem install fluent-plugin-ping-message fluent-plugin-record-modifier && \  
apk del build-base ruby-dev && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/ && \  
cp /usr/share/zoneinfo/Japan /etc/localtime  
  
RUN mkdir /fluentd/log/apache /fluentd/log/application /fluentd/log/others  

