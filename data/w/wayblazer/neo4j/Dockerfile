# wayblazer/neo4j  
FROM c12e/debian  
MAINTAINER Ricky Stillwell ricky@wayblazer.com  
  
RUN apt-get update && \  
apt-get install -y supervisor wget  
  
#ENV NEO4j_VERSION community-2.2.5  
ENV NEO4j_VERSION enterprise-2.2.5  
RUN wget -q -O /tmp/neo4j-$NEO4j_VERSION-unix.tar.gz
http://dist.neo4j.org/neo4j-$NEO4j_VERSION-unix.tar.gz && \  
tar -zxf /tmp/neo4j-$NEO4j_VERSION-unix.tar.gz -C /opt && \  
ln -s /opt/neo4j-$NEO4j_VERSION /opt/neo4j && \  
wget -q -O /opt/neo4j/lib/gson-2.2.4.jar
http://search.maven.org/remotecontent?filepath=com/google/code/gson/gson/2.2.4/gson-2.2.4.jar  
#wget -q -O /opt/neo4j/lib/c12e-plugin-0.1.6-SNAPSHOT.jar
https://s3.amazonaws.com/c1sandbox/downloads/neo4j-ext/c12e-plugin-0.1.6-SNAPSHOT.jar  
ADD neo4j-server.properties /opt/neo4j/conf/neo4j-server.properties  
ADD neo4j-wrapper.conf /opt/neo4j/conf/neo4j-wrapper.conf  
ADD neo4j.properties /opt/neo4j/conf/neo4j.properties  
RUN mkdir -p /data  
RUN mkdir -p /logs  
  
# Define mountable directories.  
VOLUME ["/data"]  
VOLUME ["/logs"]  
VOLUME ["/config"]  
  
# supervisord  
ADD neo4j_supervisor.conf /etc/supervisor/supervisord.conf  
  
# Ports  
EXPOSE 7474 1337 5001 6001 6362  
CMD ["/usr/bin/supervisord"]  

