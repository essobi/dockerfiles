FROM phenompeople/centos-sunjre:8u152  
MAINTAINER Rajesh Jonnalagadda(<admin.squad@phenompeople.com>)  
ARG SCALA_VERSION=2.11  
ARG KAFKA_VERSION=1.0.0  
EXPOSE 9092  
RUN useradd kafka -s /bin/false -u 401 && \  
wget -q -O /tmp/kafka.tar.gz http://www-
us.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
&& \  
tar -xzf /tmp/kafka.tar.gz -C /opt && \  
ln -sf /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka && \  
chown -R kafka:kafka /opt/kafka  
ENV KAFKA_HOME=/opt/kafka  
WORKDIR ${KAFKA_HOME}  
USER kafka  
ENTRYPOINT ["./bin/kafka-server-start.sh", "config/server.properties"]

