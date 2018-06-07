FROM fluent/fluentd  
MAINTAINER Minwoo Lee <ermaker@gmail.com>  
  
USER root  
RUN set -ex && \  
apk \--no-cache --update add --virtual .deps \  
build-base \  
git \  
ruby-dev \  
sudo && \  
sudo -u fluent gem install \  
bson_ext \  
fluent-plugin-bufferize \  
fluent-plugin-color-stripper \  
fluent-plugin-docker-format \  
fluent-plugin-elasticsearch \  
fluent-plugin-mongo \  
fluent-plugin-out-http \  
fluent-plugin-parser \  
fluent-plugin-record-reformer \  
fluent-plugin-rewrite-tag-filter \  
fluent-plugin-secure-forward \  
fluent-plugin-slack && \  
sudo -u fluent git clone \  
https://github.com/ermaker/fluent-plugin-color-stripper \  
-b apply_fluentd_0_14 && \  
cd fluent-plugin-color-stripper && \  
sudo -u fluent gem build fluent-plugin-color-stripper.gemspec && \  
sudo -u fluent gem install fluent-plugin-color-stripper-0.0.3.gem && \  
cd .. && \  
sudo -u fluent rm -rf fluent-plugin-color-stripper && \  
apk del .deps  
USER fluent  

