FROM fluent/fluentd:v0.12.28-onbuild  
MAINTAINER Patrick Easters <patrick@easte.rs>  
  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
# Set sane defaults  
ENV GELF_PORT 12201  
ENV GELF_PROTOCOL udp  
  
# We need the record-reformer plugin  
USER root  
RUN apk --no-cache --update add sudo build-base ruby-dev && \  
sudo -u fluent gem install fluent-plugin-record-reformer && \  
rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources
-c && \  
apk del sudo build-base ruby-dev && rm -rf /var/cache/apk/*  
  
# Config and gelf plugin are being copied in due to ONBUILD command in
upstream  
# Run fluentd!  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

