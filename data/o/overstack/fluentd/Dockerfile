FROM alpine:3.2  
MAINTAINER SHS  
  
ENV FLUENTD_VERSION 0.12.12  
RUN apk update && \  
apk upgrade && \  
apk add build-base ruby-dev jemalloc-dev && \  
rm /var/cache/apk/* && \  
echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc" && \  
gem install fluentd && \  
gem install fluent-plugin-elasticsearch && \  
ulimit -n 65536 && \  
rm -rf /tmp/* && \  
rm -rf /usr/share/ri/*  
  
COPY fluent.conf /etc/fluent/  
  
ENV JEMALLOC_PATH /usr/lib/libjemalloc.so  
  
EXPOSE 24224  
CMD sed -i "s/<hostname>/$ELASTICSEARCH_PORT_9200_TCP_ADDR/"
/etc/fluent/fluent.conf && fluentd -c /etc/fluent/fluent.conf  

