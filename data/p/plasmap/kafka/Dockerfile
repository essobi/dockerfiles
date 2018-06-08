FROM java:8-jdk  
MAINTAINER Jan Schulte <jan@plasmap.io>  
  
# Builds an image for Apache Kafka 0.8.2.2 from binary distribution.  
#  
# The Scala 2.10 build is currently recommended by the project.  
ENV KAFKA_VERSION=0.8.2.2 KAFKA_SCALA_VERSION=2.10 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN mkdir /kafka /data /logs /config  
  
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
  
# ADD config /kafka/config  
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
VOLUME [ "/data", "/logs", "/config" ]  
  
CMD ["/start.sh"]  

