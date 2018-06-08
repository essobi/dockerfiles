FROM alpine:3.1  
  
ENV FLUENTD_VERSION 0.12.16  
  
RUN apk add --update ca-certificates tar ruby ruby-json ruby-irb ruby-dev \  
musl-dev make gcc g++ libgcc libstdc++ && \  
gem install --no-document jemalloc --wrappers && \  
gem install --no-document fluentd -v $FLUENTD_VERSION && \  
fluent-gem install --no-document fluent-plugin-kubernetes_metadata_filter
fluent-plugin-elasticsearch && \  
mkdir /etc/fluent && \  
apk del tar ruby-dev musl-dev make gcc g++ libgcc libstdc++ && \  
rm -rf /tmp/* \  
/var/cache/apk/* \  
/root/.gem \  
/usr/lib/ruby/gems/*/cache/* \  
/usr/lib/ruby/gems/*/extensions/x86_64-linux/*/*/gem_make.out \  
/usr/lib/ruby/gems/*/extensions/x86_64-linux/*/*/mkmf.log \  
/usr/lib/ruby/gems/*/gems/*/ext/* \  
/usr/lib/ruby/gems/*/gems/*/spec \  
/usr/lib/ruby/gems/*/gems/*/test \  
/usr/lib/ruby/gems/*/gems/*/tests \  
/usr/lib/ruby/gems/*/gems/yajl-ruby-*/benchmark  
# ulimit -n 65536  
  
COPY fluent.conf /etc/fluent/fluent.conf  
  
ENV ES_HOSTS elasticsearch-logging.default.svc.cluster.local:9200  
  
CMD [ "/usr/bin/je", "/usr/bin/fluentd", "--no-supervisor" ]

