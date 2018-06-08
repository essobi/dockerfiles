FROM debian:jessie  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# JAVA  
ENV JAVA_MAJOR_VERSION 8  
ENV JAVA_UPDATE_VERSION 102  
ENV JAVA_BUILD_NUMBER 14  
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& grep '^networkaddress.cache.ttl=' $JAVA_HOME/jre/lib/security/java.security
|| echo 'networkaddress.cache.ttl=60' >>
$JAVA_HOME/jre/lib/security/java.security \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# HADOOP  
ENV HADOOP_VERSION 2.7.3  
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION  
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
ENV PATH $PATH:$HADOOP_HOME/bin  
RUN curl -sL --retry 3 \  
"http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf $HADOOP_HOME/share/doc \  
&& chown -R root:root $HADOOP_HOME  
  
# SIGIL  
ENV SIGIL_VERSION 0.4.0  
RUN curl -s -L --retry 3 \  
"https://github.com/gliderlabs/sigil/releases/download/v${SIGIL_VERSION}/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz"
\  
| gunzip \  
| tar -x -C /usr/bin/  
  
# FLUME  
ENV FLUME_VERSION 1.7.0  
RUN curl -sL --retry 3 --insecure \  
"https://github.com/apache/flume/archive/release-${FLUME_VERSION}.tar.gz" \  
| gunzip \  
| tar x -C /tmp/ \  
&& curl -sL
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
| gunzip \  
| tar x -C /tmp/ \  
&& MAVEN_OPTS="-Xms512m -Xmx1024m" /tmp/apache-maven-3.3.9/bin/mvn --batch-
mode -f /tmp/flume-release-${FLUME_VERSION}/pom.xml install
-Dmaven.test.skip=true \  
&& mv /tmp/flume-release-${FLUME_VERSION}/flume-ng-dist/target/apache-
flume-${FLUME_VERSION}-bin/apache-flume-${FLUME_VERSION}-bin /usr/flume \  
&& rm -rf /root/.m2 \  
&& rm -rf /tmp/*  
  
WORKDIR /usr/flume  
COPY docker-entrypoint.sh /  
COPY agent.conf /etc/flume/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["agent", "--name", "agent", "--conf", "conf", "--conf-file",
"/etc/flume/agent.conf", "-Dflume.root.logger=INFO,console"]  

