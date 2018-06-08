FROM fluent/fluentd:v0.14-onbuild  
MAINTAINER devops@leonisand.co  
  
USER root  
  
RUN apk add --no-cache --update --virtual .build-deps \  
build-base ruby-dev \  
&& echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache --update \  
percona-toolkit@testing mariadb-dev sudo \  
# cutomize following instruction as you wish  
&& sudo gem install \  
fluent-plugin-rds-slowlog \  
fluent-plugin-mysql_explain \  
fluent-plugin-sql_fingerprint \  
fluent-plugin-slack \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* /home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
COPY ./fluent.conf /fluentd/etc/slowlog-monitor.conf  
ENV FLUENTD_CONF="slowlog-monitor.conf"  

