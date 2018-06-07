FROM fluent/fluentd-kubernetes-daemonset:v0.12-alpine-elasticsearch  
# defined at https://github.com/fluent/fluentd-kubernetes-
daemonset/tree/master/docker-image/v0.12/alpine-elasticsearch  
RUN gem install fluent-plugin-record-modifier  
  
# setup forwarding settings for humio  
COPY kubernetes.conf /fluentd/etc/kubernetes.conf  
COPY fluent.conf /fluentd/etc/fluent.conf  
  
# requires envvars specifying: FLUENT_HUMIO_HOST, FLUENT_HUMIO_DATA_SPACE,
FLUENT_HUMIO_INGEST_TOKEN  

