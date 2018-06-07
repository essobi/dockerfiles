FROM debian:jessie  
MAINTAINER Roman Suvorov windj007@gmail.com  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -yqq openjdk-8-jdk openjdk-8-jre-headless wget unzip git maven
zip && \  
update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
&& java -version  
  
RUN git clone https://github.com/thinkaurelius/titan.git /tmp/titan && \  
cd /tmp/titan && \  
git fetch origin pull/1312/head:pr1312 && \  
git checkout pr1312 && \  
mvn clean install -DskipTests=true -Dgpg.skip=true -Paurelius-release && \  
mv titan-dist/titan-dist-hadoop-2/target/titan-1.1.0-SNAPSHOT-hadoop2.zip /srv
&& \  
cd /srv && \  
unzip titan-1.1.0-SNAPSHOT-hadoop2.zip && \  
rm -r /tmp/titan titan-1.1.0-SNAPSHOT-hadoop2.zip  
  
WORKDIR /srv/titan-1.1.0-SNAPSHOT-hadoop2  
  
COPY gremlin-server.yaml /srv/titan-1.1.0-SNAPSHOT-hadoop2/conf/gremlin-
server/  
COPY titan-cassandra-es.properties /srv/titan-1.1.0-SNAPSHOT-hadoop2/conf/  
COPY titan-bdb-es.properties /srv/titan-1.1.0-SNAPSHOT-hadoop2/conf/  
COPY entry-point.sh /entry-point.sh  
COPY gremlin-server.sh /srv/titan-1.1.0-SNAPSHOT-hadoop2/bin/  
  
ENTRYPOINT ["/entry-point.sh"]  
EXPOSE 8182  
VOLUME ["/data"]  
  
CMD ["bin/gremlin-server.sh", "conf/gremlin-server/gremlin-server.yaml"]  

