FROM vixns/marathon-lb:long-loglines  
MAINTAINER Stéphane Cottin <stephane.cottin@vixns.com>  
ENV KAFKA_TOPIC=haproxy_logs PORTS=9090  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends curl rsyslog-kafka \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sL
https://github.com/prometheus/haproxy_exporter/releases/download/v0.7.1/haproxy_exporter-0.7.1.linux-
amd64.tar.gz | tar zxf - \  
&& mv haproxy_exporter-0.7.1.linux-amd64/haproxy_exporter
/bin/haproxy_exporter \  
&& rm -rf haproxy_exporter-0.7.1.linux-amd64 \  
&& mkdir -p /var/state/haproxy  
COPY rsyslog /marathon-lb/service/rsyslog  
COPY prometheus_exporter /marathon-lb/service/prometheus_exporter  

