FROM fluent/fluentd:latest-onbuild  
MAINTAINER Minwoo Lee <ermaker@gmail.com>  
  
USER root  
RUN apk --no-cache --update add \  
build-base \  
ruby-dev && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
USER fluent  
  
RUN gem install \  
bson_ext \  
fluent-plugin-color-stripper \  
fluent-plugin-mongo \  
fluent-plugin-parser \  
fluent-plugin-record-reformer \  
fluent-plugin-rewrite-tag-filter  
  
# install fixed-version plugin  
USER root  
RUN apk --no-cache --update add git && \  
rm -rf /var/cache/apk/*  
USER fluent  
  
RUN git clone https://github.com/ermaker/fluent-plugin-color-stripper \  
-b strip_dangling_colors && \  
cd fluent-plugin-color-stripper && \  
gem build fluent-plugin-color-stripper.gemspec && \  
gem install fluent-plugin-color-stripper-0.0.3.gem && \  
cd .. && \  
rm -rf fluent-plugin-color-stripper  
  
RUN mkdir -p /fluentd/buffer  
VOLUME /fluentd/buffer  
EXPOSE 9880  

