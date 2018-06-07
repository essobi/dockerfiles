FROM tritruongtr/oracle-java7  
  
MAINTAINER Tri Truong <tritruong.tr@gmail.com>  
  
ENV ZOOKEEPER_VER=3.4.9  
RUN apt-get update && \  
apt-get -y install ca-certificates maven && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY pom.xml /exhibitor/pom.xml  
  
RUN wget -q
http://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VER}/zookeeper-${ZOOKEEPER_VER}.tar.gz.md5
&& \  
wget -q
http://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VER}/zookeeper-${ZOOKEEPER_VER}.tar.gz
&& \  
md5sum -c zookeeper-${ZOOKEEPER_VER}.tar.gz.md5 && \  
tar xzf zookeeper-${ZOOKEEPER_VER}.tar.gz && \  
rm /zookeeper-${ZOOKEEPER_VER}.tar.gz* && \  
mv /zookeeper-${ZOOKEEPER_VER} /zookeeper && \  
cd /exhibitor && \  
mvn clean package && \  
mv target/exhibitor-1.5.6.jar ./ && \  
rm -rf /exhibitor/target && \  
rm /exhibitor/pom.xml  
  
COPY exhibitor-wrapper /exhibitor-wrapper  
  
ENTRYPOINT ["/exhibitor-wrapper"]  

