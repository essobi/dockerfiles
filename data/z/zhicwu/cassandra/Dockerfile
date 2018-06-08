#  
# This docker image is just for development and testing purpose - please do
NOT use on production  
#  
#  
# Stage 1 - Build Lucene Index Plugin  
#  
FROM maven:3 as builder  
ENV CASSANDRA_LUCENE_INDEX_VERSION=3.0.14.0  
RUN wget https://github.com/Stratio/cassandra-lucene-
index/archive/${CASSANDRA_LUCENE_INDEX_VERSION}.zip \  
&& unzip ${CASSANDRA_LUCENE_INDEX_VERSION}.zip \  
&& cd cassandra-lucene-index* \  
&& mvn clean package \  
&& cd \- \  
&& rm -f cassandra-lucene-index*/plugin/target/*-javadoc.jar \  
&& rm -f cassandra-lucene-index*/plugin/target/*-sources.jar  
  
#  
# Stage 2 - Cassandra  
#  
# Pull Base Image  
FROM zhicwu/java:8  
# Set Maintainer Details  
MAINTAINER Zhichun Wu <zhicwu@gmail.com>  
  
# Set Environment Variables  
ENV CASSANDRA_VERSION=3.0.14 CASSANDRA_CONF=/etc/cassandra
CASSANDRA_LIB=/usr/share/cassandra/lib \  
CASSANDRA_DATA=/var/lib/cassandra CASSANDRA_LOG=/var/log/cassandra  
  
#ENV MX4J_VERSION=3.0.1 MX4J_ADDRESS=0.0.0.0 MX4J_PORT=18081  
ENV JOLOKIA_VERSION=1.3.7 JOLOKIA_HOST=0.0.0.0 JOLOKIA_PORT=8778  
# Set Labels - mx4j_version="MX4J Tools $MX4J_VESION"  
LABEL cassandra_version="Apache Cassandra $CASSANDRA_VERSION"
jolokia_version="Jolokia ${JOLOKIA_VERSION}"  
  
# Create Hard-coded Cassandra User and Group  
RUN groupadd -g 7878 cassandra \  
&& useradd -u 7878 -g cassandra -s /bin/sh -d $CASSANDRA_LIB cassandra  
  
# Install Cassandra  
RUN echo 'deb http://www.apache.org/dist/cassandra/debian '`echo
"${CASSANDRA_VERSION}" | awk '{split($0,v,"."); print v[1] v[2]}'`'x main' \  
>> /etc/apt/sources.list.d/cassandra.list \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated cassandra="$CASSANDRA_VERSION"
cassandra-tools="$CASSANDRA_VERSION" \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -ri ' \  
s/^(rpc_address:).*/\1 0.0.0.0/; \  
' "$CASSANDRA_CONF/cassandra.yaml" \  
&& chown -R cassandra:cassandra $CASSANDRA_CONF $CASSANDRA_DATA $CASSANDRA_LIB
$CASSANDRA_LOG  
  
# Add Lucene Index Support  
COPY \--from=builder cassandra-lucene-index*/plugin/target/cassandra-lucene-
index-plugin-*.jar $CASSANDRA_LIB/.  
  
# Setup Remote JMX and Add Jolokia(please use separate instance hosting hawtio
for monitoring / management)  
RUN cp -f $JAVA_HOME/jre/lib/management/jmxremote.access
$JAVA_HOME/jre/lib/management/jmxremote.access.bak \  
&& chown root:cassandra $JAVA_HOME/jre/lib/management/jmxremote.access* \  
&& chmod 664 $JAVA_HOME/jre/lib/management/jmxremote.access* \  
&& wget http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
jvm/${JOLOKIA_VERSION}/jolokia-jvm-${JOLOKIA_VERSION}-agent.jar \  
-O $CASSANDRA_LIB/jolokia-jvm-${JOLOKIA_VERSION}-agent.jar  
  
VOLUME ["/var/lib/cassandra"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# 7000: intra-node communication  
# 7001: TLS intra-node communication  
# 7199: JMX  
# 8778: Jolokia  
# 9042: CQL  
# 9160: thrift service  
# 18081: MX4J  
EXPOSE 7000 7001 7199 8778 9042 9160  
CMD ["cassandra", "-f"]  

