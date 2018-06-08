# Builds an image for Apache Kafka 0.8.1.1 from binary distribution.  
#  
# The netflixoss/java base image runs Oracle Java 7 installed atop the  
# ubuntu:trusty (14.04) official image. Docker's official java images are  
# OpenJDK-only currently, and the Kafka project, Confluent, and most other  
# major Java projects test and recommend Oracle Java for production for
optimal  
# performance.  
FROM netflixoss/java:7  
# from an image built by Ches Martin <ches@whiskeyandgrits.net>  
MAINTAINER Charles Lescot  
  
# The Scala 2.10 build is currently recommended by the project.  
ENV KAFKA_VERSION=0.9.0.0 KAFKA_SCALA_VERSION=2.11 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
supervisor wget apt-transport-https curl vim  
  
WORKDIR /tmp  
  
# rancher confd section  
ADD https://github.com/rancher/compose-
templates/raw/master/utils/containers/confd/confd-0.11.0-dev-rancher-linux-
amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
COPY supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir -p /etc/supervisor/conf.d  
RUN mkdir -p /var/log/supervisor  
RUN chmod -R 600 /var/log/supervisor  
RUN bash -c 'mkdir -p /etc/confd/{conf.d,templates}'  
  
#copy confd inputs  
COPY ./conf.d /etc/confd/conf.d  
COPY ./templates /etc/confd/templates  
  
# end rancher confd section  
RUN mkdir /kafka /data /logs  
  
COPY zookeeper.properties /kafka/config/zookeeper.properties  
COPY log4j.properties /kafka/config/log4j.properties  
COPY tools-log4j.properties /kafka/config/tools-log4j.properties  
  
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
  
# Check artifact digest integrity  
RUN echo VERIFY CHECKSUM: && \  
gpg --print-md MD5 ${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \  
cat ${KAFKA_RELEASE_ARCHIVE}.md5  
  
# Install Kafka to /kafka  
RUN tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \  
rm -rf kafka_*  
  
ADD start.sh /start.sh  
  
# Set up a user to run Kafka  
RUN groupadd kafka && \  
useradd -d /kafka -g kafka -s /bin/false kafka && \  
chown -R kafka:kafka /kafka /data /logs  
  
ENV PATH /kafka/bin:$PATH  
WORKDIR /kafka  
  
# broker, jmx  
EXPOSE 9092 ${JMX_PORT}  
VOLUME [ "/data", "/logs"]  
  
CMD ["/usr/bin/supervisord"]  

