FROM java:openjdk-7-jdk-alpine  
  
ARG CASSANDRA_VERSION=2.0.17  
# Make Alpine Linux resolve localhost  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
RUN apk add --update --no-cache wget supervisor bash openssl curl tar g++  
  
# install g++ & glibc  
# to make snappy native library work as it as dependecy on c++ & libc  
# see https://github.com/gliderlabs/docker-alpine/issues/11 and
https://github.com/gliderlabs/docker-alpine/issues/106  
RUN apk --update --no-cache update glibc-2.21-r2 glibc-bin-2.21-r2  
  
RUN mkdir -p /data /logs /init /opt/cassandra  
  
RUN wget --no-check-certificate --progress=dot:mega -O -
http://archive.apache.org/dist/cassandra/$CASSANDRA_VERSION/apache-
cassandra-$CASSANDRA_VERSION-bin.tar.gz | tar -zx -C /opt/cassandra --strip-
components=1  
# FIXME : following does not work as mirror does not have older cassandra
versions  
#RUN wget -q -O - $(wget -q -O -
"http://www.apache.org/dyn/closer.cgi?as_json=1" | jq -r
.preferred)/dist/cassandra/$CASSANDRA_VERSION/apache-
cassandra-$CASSANDRA_VERSION-bin.tar.gz | \  
# tar -xzf - -C /opt/cassandra --strip-components=1  
EXPOSE 7000 7001 7199 9160 9042  
CMD "/opt/cassandra/bin/start.sh"  
  
ADD cassandra.yaml /opt/cassandra/conf/cassandra.yaml  
ADD cassandra-env.sh /opt/cassandra/conf/cassandra-env.sh  
ADD log4j-server.properties /opt/cassandra/conf/log4j-server.properties  
ADD start.sh /opt/cassandra/bin/start.sh  
ADD cassandra-topology.properties /opt/cassandra/conf/cassandra-
topology.properties  

