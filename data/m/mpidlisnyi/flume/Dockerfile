FROM java:openjdk-8-jdk  
MAINTAINER Maksim Podlesnyi <mpodlesnyi@smartling.com>  
  
ENV FLUME_VERSION=1.7.0 \  
FLUME_CONF_DIR=/conf \  
FLUME_AGENT_NAME=test \  
MAVEN_VERSION=3.5.0 \  
LOG4J_PROPERTIES=/opt/flume/log4j.properties \  
PATH=${PATH}:/opt/flume/bin \  
HADOOP_COMMON_LIB_NATIVE_DIR=/usr/local/hadoop/lib/native  
  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/flume ${FLUME_CONF_DIR} /opt/maven
${HADOOP_COMMON_LIB_NATIVE_DIR}  
  
#TODO add verification  
RUN wget -qO- http://archive.apache.org/dist/flume/${FLUME_VERSION}/apache-
flume-${FLUME_VERSION}-bin.tar.gz \  
| tar zxvf - -C /opt/flume --strip 1  
  
# thanks http://shout.setfive.com/2016/05/04/apache-flume-setting-up-flume-
for-an-s3-sink/  
COPY pom.xml /opt/flume/pom.xml  
  
RUN wget -qO- http://apache.ip-
connect.vn.ua/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
| tar zxvf - -C /opt/maven --strip 1 \  
&& cd /opt/flume/ \  
&& /opt/maven/bin/mvn process-sources \  
&& rm -rf /opt/maven/ \  
&& rm -f /opt/flume/pom.xml  
  
COPY log4j.properties ${LOG4J_PROPERTIES}  
COPY entrypoint.sh /entrypoint  
WORKDIR /opt/flume/  
RUN chmod +x /entrypoint  
  
RUN sed -i
's/FLUME_CLASSPATH=\"\"/FLUME_CLASSPATH=\"\/usr\/local\/hadoop\/lib\/native\/*\"/g'
bin/flume-ng  
RUN sed -i
's/FLUME_JAVA_LIBRARY_PATH=\"\"/FLUME_JAVA_LIBRARY_PATH=\"\/usr\/local\/hadoop\/lib\/native\"/g'
bin/flume-ng  
  
ENTRYPOINT [ "/entrypoint" ]  

