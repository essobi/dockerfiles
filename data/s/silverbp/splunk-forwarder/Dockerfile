FROM fluent/fluentd:latest-onbuild  
MAINTAINER casey@silverblueprints.com  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
USER root  
RUN apk --no-cache --update add sudo build-base ruby-dev && \  
  
sudo gem install docker-api && \  
sudo gem install lru_redux && \  
mkdir /var/log/fluentd && \  
  
rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources
-c && \  
apk del sudo build-base ruby-dev && rm -rf /var/cache/apk/*  
  
EXPOSE 24284  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

