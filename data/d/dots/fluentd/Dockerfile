FROM fluent/fluentd:latest-onbuild  
WORKDIR /home/fluent  
  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
USER root  
RUN apk add --no-cache --virtual .fluent-deps \  
sudo \  
build-base \  
ruby-dev \  
&& sudo -u fluent gem install \  
fluent-plugin-concat \  
fluent-plugin-elasticsearch \  
fluent-plugin-grep \  
fluent-plugin-multiline-parser \  
&& rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem \  
&& sudo -u fluent gem sources -c \  
&& apk del .fluent-deps  
  
EXPOSE 24284  
USER fluent  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

