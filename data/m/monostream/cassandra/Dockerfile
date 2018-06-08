FROM cassandra:3.11  
LABEL maintainer="manuel@monostream.com"  
  
ENV CASSANDRA_CONFIG /etc/cassandra  
ENV CASSANDRA_LIB /usr/share/cassandra/lib  
  
# install netcat to check cqlsh port and wget  
RUN apt-get update && \  
apt-get install -y --no-install-recommends netcat wget && \  
rm -rf /var/lib/apt/lists/*  
  
# download dumb-init 1.2.1  
RUN wget -nv -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 && \  
chmod 755 /usr/local/bin/dumb-init  
  
# jmx exporter  
RUN wget -nv -O ${CASSANDRA_LIB}/jmx_prometheus_javaagent-0.3.0.jar
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar
&& \  
chmod 755 ${CASSANDRA_LIB}/jmx_prometheus_javaagent-0.3.0.jar  
RUN wget -nv -O ${CASSANDRA_CONFIG}/cassandra-prometheus.yml
https://raw.githubusercontent.com/prometheus/jmx_exporter/master/example_configs/cassandra.yml  
  
#RUN set -ex; \  
# echo 'JVM_OPTS="$JVM_OPTS
-javaagent:'${CASSANDRA_LIB}/jmx_prometheus_javaagent-0.3.0.jar=7070:${CASSANDRA_CONFIG}/cassandra-
prometheus.yml'"' >> ${CASSANDRA_CONFIG}/cassandra-env.sh  
# setup environment  
WORKDIR /app/  
ENV PATH "/app:${PATH}"  
COPY cqlsh_create_user.sh .  
COPY docker-entrypoint.sh .  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "docker-entrypoint.sh"]  
  
EXPOSE 7000 7001 7070 7199 9042 9160  
CMD ["cassandra", "-f"]

