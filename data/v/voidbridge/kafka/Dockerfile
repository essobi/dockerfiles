FROM voidbridge/java:latest  
MAINTAINER Tom Dearman <tom.dearman@voidbridge.com>  
  
ARG SCALA_VERSION=2.11  
ARG KAFKA_VERSION=0.9.0.1  
RUN yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y hostname bind-utils python-pip && \  
pip install j2cli && \  
yum clean all -y  
  
RUN mkdir -p /opt/kafka && \  
curl -fL
http://apache.mirror.anlx.net/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
| \  
tar -zxf - -C /opt/kafka --strip-components 1  
  
ADD files /  
ADD templates /tmp/templates  
RUN chmod 755 /usr/bin/run-kafka  
  
ENV HEAP_FRACTION=0.5 \  
DEFAULT_PARTITIONS=1 \  
LOG_RETENTION_HOURS=168 \  
DEFAULT_REPLICATION_FACTOR=1  
USER 1001  
EXPOSE 9092  
VOLUME /mnt/data  
CMD ["run-kafka"]  

