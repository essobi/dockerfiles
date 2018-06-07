FROM cassandra:3.11.2  
RUN mkdir /prometheus  
ADD
"https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar"
/prometheus  
RUN chmod 644 /prometheus/jmx_prometheus_javaagent-0.3.0.jar  
ADD cassandra.yml /prometheus/cassandra.yml  
  
# add dependencies for logstash-logback-encoder  
ADD lib /usr/share/cassandra/lib  
  
ENV JVM_OPTS "$JVM_OPTS
-javaagent:/prometheus/jmx_prometheus_javaagent-0.3.0.jar=61621:/prometheus/cassandra.yml
"  
EXPOSE 61621  

