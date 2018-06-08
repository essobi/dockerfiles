FROM fluent/fluentd:v0.14-onbuild  
MAINTAINER devops@leonisand.co  
  
ENV PGSQL_PLUGIN_COMMIT 3e40b48948c970389c35725aa2fe5f36c814796c  
ENV PGSQL_FINGERPRINT_COMMIT 66d264c6a551b4aedfe91ed41e2b34911267911f  
  
USER root  
  
RUN apk add \--no-cache \--update \--virtual .build-deps \  
build-base ruby-dev git \  
&& echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add \--no-cache \--update \  
mariadb-dev sudo \  
  
# cutomize following instruction as you wish  
&& sudo gem install \  
fluent-plugin-slack \  
# Install github.com/hirakiuc/fluent-plugin-rds-pgsql-slow-query-log.git  
&& sudo git clone https://github.com/hirakiuc/fluent-plugin-rds-pgsql-slow-
query-log.git /tmp/fluent-plugin-pgsql-slow-query-log \  
&& sudo sh -c 'cd /tmp/fluent-plugin-pgsql-slow-query-log && git checkout
$PGSQL_PLUGIN_COMMIT && gem build fluent-plugin-rds-pgsql-slow-query-
log.gemspec && gem install ./fluent-plugin-rds-pgsql-slow-query-log*.gem' \  
# Install github.com/hirakiuc/fluent-plugin-pgsql_fingerprint.git  
&& sudo git clone https://github.com/hirakiuc/fluent-plugin-
pgsql_fingerprint.git /tmp/fluent-plugin-pgsql_fingerprint \  
&& sudo sh -c 'cd /tmp/fluent-plugin-pgsql_fingerprint && git checkout
$PGSQL_FINGERPRINT_COMMIT && gem build fluent-plugin-pgsql_fingerprint.gemspec
&& gem install ./fluent-plugin-pgsql_fingerprint*.gem' \  
# Cleanup  
&& sudo gem sources \--clear-all \  
&& apk del .build-deps \  
&& rm -rf /usr/lib/ruby/gems/*/cache/*.gem \  
&& rm -rf /tmp/fluent-plugin-pgsql-slow-query-log \  
&& rm -rf /tmp/fluent-plugin-pgsql_fingerprint \  
&& mkdir -p /var/fluent/pos_files  
  
COPY ./fluent.conf /fluentd/etc/slowlog-monitor.conf  
ENV FLUENTD_CONF="slowlog-monitor.conf"  

