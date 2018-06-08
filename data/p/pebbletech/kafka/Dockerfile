# Builds an image for Apache Kafka 0.8.1.1 from binary distribution.  
#  
# The netflixoss/java base image runs Oracle Java 7 installed atop the  
# ubuntu:trusty (14.04) official image. Docker's official java images are  
# OpenJDK-only currently, and the Kafka project, Confluent, and most other  
# major Java projects test and recommend Oracle Java for production for
optimal  
# performance.  
FROM netflixoss/java:7  
MAINTAINER Ches Martin <ches@whiskeyandgrits.net>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates \  
python3-pip  
  
# The Scala 2.10 build is currently recommended by the project.  
ENV KAFKA_VERSION=0.10.0.0 KAFKA_SCALA_VERSION=2.11 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN mkdir /kafka /data  
  
# Cache-friendly download and verify:  
WORKDIR /tmp  
RUN wget
http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
&& \  
wget
https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.md5
&& \  
echo VERIFY CHECKSUM: && \  
gpg --print-md MD5 ${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \  
cat ${KAFKA_RELEASE_ARCHIVE}.md5 && \  
tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \  
rm -rf kafka_*  
  
COPY requirements.txt /exhibitor/requirements.txt  
RUN pip3 install -r /exhibitor/requirements.txt  
  
COPY config /kafka/config  
COPY start.sh /start.sh  
COPY start.py /start.py  
  
# Set up a user to run Kafka  
RUN groupadd kafka && \  
useradd -d /kafka -g kafka -s /bin/false kafka && \  
chown -R kafka:kafka /kafka /data  
USER kafka  
ENV PATH /kafka/bin:$PATH  
WORKDIR /kafka  
  
# broker, jmx  
EXPOSE 9092 ${JMX_PORT}  
VOLUME [ "/data" ]  
  
CMD ["/start.sh"]  
  

