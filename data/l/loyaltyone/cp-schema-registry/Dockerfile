FROM confluentinc/cp-schema-registry:4.0.0-3  
MAINTAINER LoyaltyOne  
  
RUN wget -P /usr/local/share/
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar  
  
COPY bootstrap /usr/local/bin/  
COPY schema-registry-metrics.yml /usr/local/share/  
  
ENTRYPOINT ["/usr/local/bin/bootstrap"]  
CMD ["/etc/confluent/docker/run"]

