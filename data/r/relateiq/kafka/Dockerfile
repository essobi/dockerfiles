FROM relateiq/oracle-java7  
  
RUN apt-get update && apt-get install -y wget  
  
ENV KAFKA_VERSION=0.10.1.0 KAFKA_SCALA_VERSION=2.11 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN mkdir /data && \  
mkdir -p /kafka/logs  
  
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
  
ENV PATH /kafka/bin:$PATH  
WORKDIR /kafka  
  
VOLUME [ "/data", "/kafka/logs" ]  
  
# broker, jmx  
EXPOSE 9092 ${JMX_PORT}  
  
ADD
http://repo1.maven.org/maven2/org/slf4j/slf4j-log4j12/1.7.6/slf4j-log4j12-1.7.6.jar
/kafka/lib/slf4j-log4j12.jar  
ADD config /kafka/config  
ADD start.sh /start.sh  
  
CMD ["/start.sh"]  

