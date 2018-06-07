# Builds an image for Apache Kafka 0.9.0.1 from binary distribution.  
FROM ubuntu:trusty  
MAINTAINER George Cooper <george.cooper@egloo.com>  
  
# Install Oracle Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  
  
# The Scala 2.11 build is currently recommended by the project.  
ENV KAFKA_VERSION=0.11.0.0 KAFKA_SCALA_VERSION=2.11 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN mkdir /kafka /data /logs  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates  
  
# Download Kafka binary distribution  
ADD
http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
/tmp/  
ADD
https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.md5
/tmp/  
  
WORKDIR /tmp  
  
# Check artifact digest integrity  
RUN echo VERIFY CHECKSUM: && \  
gpg --print-md MD5 ${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \  
cat ${KAFKA_RELEASE_ARCHIVE}.md5  
  
# Install Kafka to /kafka  
RUN tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \  
rm -rf kafka_*  
  
ADD config /kafka/config  
ADD start.sh /start.sh  
  
# Set up a user to run Kafka  
RUN groupadd kafka && \  
useradd -d /kafka -g kafka -s /bin/false kafka && \  
chown -R kafka:kafka /kafka /data /logs  
USER kafka  
ENV PATH /kafka/bin:$PATH  
WORKDIR /kafka  
  
# broker, jmx  
EXPOSE 9092 ${JMX_PORT}  
VOLUME [ "/data", "/logs" ]  
  
CMD ["/start.sh"]  
  

