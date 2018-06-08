FROM fluent/fluentd-kubernetes-daemonset:v0.12-debian-cloudwatch  
  
RUN gem install fluent-plugin-detect-exceptions  
  
ENV STACK_TRACE_FLUSH_INTERVAL=1  
COPY kubernetes.conf /fluentd/etc/  
  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

