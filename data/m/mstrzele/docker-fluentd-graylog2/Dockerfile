FROM fluent/fluentd:latest-onbuild  
MAINTAINER Maciej Strzelecki <maciej.strzelecki@gmail.com>  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
USER root  
  
RUN apk --no-cache add sudo ca-certificates openssl && \  
  
sudo -u fluent gem install gelf && \  
  
cd /fluentd/plugins && \  
wget https://raw.githubusercontent.com/emsearcy/fluent-plugin-
gelf/master/lib/fluent/plugin/out_gelf.rb && \  
  
rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources
-c && \  
apk del sudo ca-certificates openssl && rm -rf /var/cache/apk/*  
  
EXPOSE 24284  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

