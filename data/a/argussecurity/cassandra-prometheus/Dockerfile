FROM cassandra:3.3  
ENV CASSANDRA_CONFIG=/etc/cassandra  
  
# authentication  
RUN sed -i -e "s/^authenticator.*/authenticator: PasswordAuthenticator/"
$CASSANDRA_CONFIG/cassandra.yaml  
  
# prometheus (PROMETHEUS_PORT can be injected on runtime)  
ADD
http://central.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.6/jmx_prometheus_javaagent-0.6.jar
/usr/app/jmx_prometheus_javaagent.jar  
ADD prometheus-config.yml /usr/app/prometheus-config.yml  
RUN chmod +r /usr/app/jmx_prometheus_javaagent.jar && \  
echo 'JVM_OPTS="$JVM_OPTS
-javaagent:/usr/app/jmx_prometheus_javaagent.jar=${PROMETHEUS_PORT:-31500}:/usr/app/prometheus-
config.yml"' >> $CASSANDRA_CONFIG/cassandra-env.sh  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["/docker-entrypoint.sh", "cassandra", "-f"]  

