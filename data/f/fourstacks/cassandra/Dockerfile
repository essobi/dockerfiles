FROM cassandra:3.7  
ENV CASSANDRA_OPTIONS=-R  
  
ADD http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
jvm/1.3.4/jolokia-jvm-1.3.4-agent.jar /opt/jolokia-jvm-1.3.4.jar  
RUN chmod +r /opt/jolokia-jvm-1.3.4.jar  
ENV JVM_OPTS="-javaagent:/opt/jolokia-jvm-1.3.4.jar=port=7777,host=*
$JVM_OPTS"  
ADD cassandra.yaml /etc/cassandra/cassandra.yaml  
  
ADD backup /usr/bin/backup  
ADD restore /usr/bin/restore  
RUN chmod +x /usr/bin/backup /usr/bin/restore  

