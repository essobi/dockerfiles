FROM brennovich/protobuf-tools:latest  
MAINTAINER Felipe Sabino <felipe@sabino.pro>  
  
RUN apk update && \  
apk add gcc g++ make unzip git wget ca-certificates --no-cache && \  
rm -fr /var/cache/apk/*  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /usr/lib/mvn  
ENV PATH $MAVEN_HOME/bin:$PATH  
ENV MAVEN_OPTS -Xmx768m -XX:+UseConcMarkSweepGC -XX:MaxPermSize=128m
-XX:+CMSPermGenSweepingEnabled  
  
RUN wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \  
rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \  
mv apache-maven-$MAVEN_VERSION /usr/lib/mvn  
  
RUN git clone https://github.com/dremio/dremio-oss.git /dremio-git && \  
cd /dremio-git && \  
mvn clean install -DskipTests && \  
mv /dremio-git/distribution/server/target/dremio-community*/dremio-community*/
/dremio && \  
rm -rf /dremio-git  
  
WORKDIR /dremio  
  
EXPOSE 9047 31010  
CMD /dremio/bin/dremio start && tail -f /dremio/log/server.out  

