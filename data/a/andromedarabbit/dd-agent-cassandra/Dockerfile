FROM datadog/docker-dd-agent:latest-jmx  
  
ENV CASSANDRA_VERSION 3.11.2  
RUN cd /opt \  
&& curl --silent -O
http://archive.apache.org/dist/cassandra/${CASSANDRA_VERSION}/apache-
cassandra-${CASSANDRA_VERSION}-bin.tar.gz \  
&& tar zxf apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \  
&& mv -v apache-cassandra-${CASSANDRA_VERSION} cassandra \  
&& rm -fv apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz  
  
ENV PATH="/opt/cassandra/bin:${PATH}"

