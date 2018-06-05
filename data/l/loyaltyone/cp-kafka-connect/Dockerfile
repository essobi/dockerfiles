FROM confluentinc/cp-kafka-connect:4.0.0-3  
MAINTAINER LoyaltyOne  
  
RUN wget -P /usr/local/share/
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar  
  
COPY bootstrap setup-plugins.sh s3-cp.sh /usr/local/bin/  
COPY kafka-connect-metrics.yml setup-plugins.sh s3-cp.sh /usr/local/share/  
  
#TODO: This is for local. Should remove  
COPY config/certs /root/certs  
  
RUN setup-plugins.sh  
  
ENTRYPOINT ["/usr/local/bin/bootstrap", "/usr/local/bin/s3-cp.sh",
"/etc/confluent/docker/run"]

