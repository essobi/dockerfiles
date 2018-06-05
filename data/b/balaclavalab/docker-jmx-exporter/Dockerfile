FROM openjdk:8-jre-alpine  
  
ENV JMX_EXPORTER=0.1.0 CONFD=0.14.0  
RUN apk add wget --no-cache \  
&& mkdir -p /opt/jmx_prometheus_httpserver \  
&& wget
http://central.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/${JMX_EXPORTER}/jmx_prometheus_httpserver-${JMX_EXPORTER}-jar-
with-dependencies.jar \  
-O /opt/jmx_prometheus_httpserver/jmx_prometheus_httpserver.jar \  
&& wget
https://github.com/kelseyhightower/confd/releases/download/v${CONFD}/confd-${CONFD}-linux-
amd64 \  
-O /usr/local/bin/confd \  
&& chmod +x /usr/local/bin/confd  
  
COPY confd /etc/confd  
COPY entrypoint.sh /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  

