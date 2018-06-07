FROM konstruktoid/java  
  
LABEL org.label-schema.name="cassandra" \  
org.label-schema.vcs-url="git://github.com/konstruktoid/Cassandra_Build.git"  
  
ENV REPO 'deb http://debian.datastax.com/community stable main'  
ENV DIRS '/var/log/cassandra/ /var/lib/cassandra/data
/var/lib/cassandra/commitlog /var/lib/cassandra/saved_cache'  
RUN \  
apt-get update && \  
apt-get -y install procps curl --no-install-recommends && \  
curl -L http://debian.datastax.com/debian/repo_key | apt-key add - && \  
echo $REPO > /etc/apt/sources.list.d/cassandra.sources.list  
  
RUN \  
mkdir -p $DIRS && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install dsc30 cassandra-tools --no-install-recommends && \  
chown -R cassandra:cassandra $DIRS && \  
chmod -R 0755 $DIRS && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo  
  
EXPOSE 7000 7001 7199 9042 9160  
CMD ["cassandra", "-f"]  

