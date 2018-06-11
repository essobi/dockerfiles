FROM fluent/fluentd  
MAINTAINER 77749770@qq.com  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
  
# https://github.com/fluent/fluentd-docker-image  
# cutomize following "gem install fluent-plugin-..." line as you wish  
USER root  
RUN apk --no-cache --update add sudo build-base ruby-dev && \  
sudo -u fluent gem install fluent-plugin-kubernetes_metadata_filter fluent-
plugin-elasticsearch fluent-plugin-elasticsearch-timestamp-check fluent-
plugin-rewrite-tag-filter&& \  
rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources
-c && \  
apk del sudo build-base ruby-dev && rm -rf /var/cache/apk/*  
  
EXPOSE 24284  
COPY fluent.conf /fluentd/etc/  
#USER fluent  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

