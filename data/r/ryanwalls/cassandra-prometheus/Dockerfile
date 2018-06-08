FROM cassandra:3.11.2  
ADD
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.1/jmx_prometheus_javaagent-0.3.1.jar
.  
ADD cassandra.yml .  
RUN chmod 777 jmx_prometheus_javaagent-0.3.1.jar  
RUN chmod 777 cassandra.yml  
RUN ls -l  
RUN echo 'JVM_OPTS="$JVM_OPTS
-javaagent:'/jmx_prometheus_javaagent-0.3.1.jar=7070:$PWD/cassandra.yml'"' >>
$CASSANDRA_CONFIG/cassandra-env.sh  
  
EXPOSE 7070

