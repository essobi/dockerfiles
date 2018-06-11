#  
# Cassandra Dockerfile for Usergrid  
#  
# https://github.com/yep/usergrid-cassandra  
#  
FROM yep1/usergrid-java  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CASSANDRA_VERSION 2.1.12  
WORKDIR /root  
  
# add datastax repository and install cassandra  
RUN \  
echo "deb http://debian.datastax.com/community stable main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list && \  
curl https://debian.datastax.com/debian/repo_key | apt-key add - && \  
apt-get update && \  
apt-get update -o Dir::Etc::sourcelist="sources.list.d/cassandra.sources.list"
-o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0" && \  
apt-get install -yq cassandra=${CASSANDRA_VERSION} net-tools && \  
rm -rf /var/lib/apt/lists/*  
  
# persist database and logs between container starts  
VOLUME ["/var/lib/cassandra", "/var/log/cassandra"]  
  
# set default command when starting container with "docker run"  
CMD /root/run.sh  
  
# available ports:  
# 7000 intra-node communication  
# 7001 intra-node communication over tls  
# 7199 jmx  
# 9042 cassandra native transport (cassandra query language, cql)  
# 9160 cassandra thrift interface (legacy)  
EXPOSE 9042 9160  
COPY run.sh /root/run.sh  

