FROM fluent/fluentd:v0.14.25-debian  
USER root  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& sudo gem install gelf --no-document \  
&& sudo gem install fluent-plugin-kubernetes_metadata_filter --no-document \  
&& sudo gem install fluent-plugin-record-modifier --no-document \  
&& sudo gem install fluent-plugin-elasticsearch --no-document \  
&& sudo gem install fluent-plugin-s3 -v 1.0.0 \--no-document \  
&& sudo gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
COPY plugins /fluentd/plugins/  
# Overwrite default entrypoint to run with root user  
ENTRYPOINT []  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

