FROM fluent/fluentd:v0.12.34-onbuild  
  
USER root  
  
RUN apk add --update --virtual .build-deps \  
sudo build-base ruby-dev \  
&& sudo -u fluent gem install \  
fluent-plugin-elasticsearch \  
fluent-plugin-secure-forward \  
&& sudo -u fluent gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
USER fluent

