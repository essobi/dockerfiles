FROM fluent/fluentd:v0.14.23-debian  
  
USER root  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev libffi-dev" \  
&& apt-get update \  
&& apt-get install \  
-y --no-install-recommends \  
$buildDeps \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install \  
fluent-plugin-record-reformer:0.9.1 \  
fluent-plugin-aws-elasticsearch-service:1.0.0 \  
fluent-plugin-kubernetes_metadata_filter:0.32.0 \  
ffi \  
fluent-plugin-systemd:0.3.1 \  
&& gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem sources --clear-all \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
# Copy configuration files  
COPY ./conf/fluent.conf /fluentd/etc/  
COPY ./conf/systemd.conf /fluentd/etc/  
COPY ./conf/kubernetes.conf /fluentd/etc/  
  
# Copy plugins  
COPY plugins /fluentd/plugins/  
  
# Environment variables  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
ENTRYPOINT []  
  
# Run Fluentd  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

