# Raisonata Cassandra 2.0 Base Image  
#  
# VERSION 0.1  
#  
# Installs Cassandra 2.1.3 package.  
# Sseed nodes should be configured by child images.  
FROM dockerfile/java:oracle-java8  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CASSANDRA_CONFIG /etc/cassandra  
  
# Tools  
ADD scripts/cassandra-common.sh /usr/local/sbin/cassandra-common  
  
# Configs  
ADD conf/log4j-server.properties ${CASSANDRA_CONFIG}  
  
# Add DataStax sources  
ADD conf/datastax_key /tmp/datastax_key  
RUN apt-key add /tmp/datastax_key  
RUN echo "deb http://debian.datastax.com/community stable main" >
/etc/apt/sources.list.d/datastax.list  
  
# Workaround for https://github.com/docker/docker/issues/6345  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
# Install Cassandra 2.1.3  
RUN apt-get update && \  
apt-get install -y cassandra=2.1.3 dsc21=2.1.3-1 && \  
rm -rf /var/lib/apt/lists/*  
  
# Necessary since cassandra is trying to override the system limitations  
# See https://groups.google.com/forum/#!msg/docker-
dev/8TM_jLGpRKU/dewIQhcs7oAJ  
RUN rm -f /etc/security/limits.d/cassandra.conf  
  
EXPOSE 7199 7000 7001 9160 9042 22 8012 61621  
VOLUME ["/store"]  
CMD [""]  

