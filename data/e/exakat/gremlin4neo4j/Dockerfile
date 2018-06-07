FROM openjdk:8  
MAINTAINER Exakat, Damien Seguy, dseguy@exakat.io  
  
RUN \  
echo "====> Basics" && \  
mkdir /usr/src/gremlin/ && \  
cd /usr/src/gremlin && \  
apt-get update && apt-get install -y --no-install-recommends \  
git \  
maven \  
lsof && \  
\  
echo "====> Neo4j" && \  
wget --quiet http://dist.neo4j.org/neo4j-community-2.3.11-unix.tar.gz && \  
tar zxf neo4j-community-2.3.11-unix.tar.gz && \  
mv neo4j-community-2.3.11 neo4j && \  
export NEO4J_HOME=/usr/src/gremlin/neo4j && \  
sed -i.bak
s/dbms\.security\.auth_enabled=true/dbms\.security\.auth_enabled=false/
neo4j/conf/neo4j-server.properties && \  
sed -i.bak
s%#org.neo4j.server.thirdparty_jaxrs_classes=org.neo4j.examples.server.unmanaged=/examples/unmanaged%org.neo4j.server.thirdparty_jaxrs_classes=com.thinkaurelius.neo4j.plugins=/tp%
neo4j/conf/neo4j-server.properties && \  
sed -i.bak
s%org.neo4j.server.webserver.port=7474%org.neo4j.server.webserver.port=7777%
neo4j/conf/neo4j-server.properties && \  
sed -i.bak
s%#org.neo4j.server.webserver.address=0.0.0.0%org.neo4j.server.webserver.address=0.0.0.0%
neo4j/conf/neo4j-server.properties && \  
rm neo4j/conf/neo4j-server.properties.bak && \  
rm -rf neo4j-community-2.3.11-unix.tar.gz && \  
\  
echo "====> Gremlin 3" && \  
git clone https://github.com/thinkaurelius/neo4j-gremlin-plugin && \  
cd neo4j-gremlin-plugin && \  
sed -i.bak s_\<tinkerpop-version\>3.1.0-incubating\</tinkerpop-
version\>_\<tinkerpop-version\>3.2.0-incubating\</tinkerpop-version\>_
tinkerpop3/pom.xml && \  
mvn clean package -DskipTests -Dtp.version=3 && \  
unzip target/neo4j-gremlin-plugin-tp3-2.3.1-server-plugin.zip -d
../neo4j/plugins/gremlin-plugin && \  
cd .. && \  
rm -rf /usr/src/gremlin/neo4j-gremlin-plugin && \  
\  
echo "====> Cleanup" && \  
apt-get clean && \  
apt-get remove -y --purge maven  
  
WORKDIR /usr/src/gremlin  
  
COPY gremlin-start.sh /gremlin-start.sh  
  
EXPOSE 7777  
  
ENTRYPOINT ["/gremlin-start.sh"]  
  
CMD ["neo4j"]  

