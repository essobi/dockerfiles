FROM jeanblanchard/busybox-java:8  
ENV
KAFKA_RELEASE="http://apache.mirrors.spacedump.net/kafka/0.8.2.1/kafka_2.10-0.8.2.1.tgz"  
ENV KAFKA_FILE="/tmp/kafka.tar.gz"  
RUN DEBIAN_FRONTEND="noninteractive" \  
mkdir -p /tmp/kafka && \  
curl -Lo $KAFKA_FILE $KAFKA_RELEASE && \  
gunzip < $KAFKA_FILE | tar -C /tmp/kafka -xvf - && \  
mv /tmp/kafka/* /opt/kafka && \  
ls /opt/kafka/bin  
  
USER root  
  
ADD scripts/mirrormaker.sh mirrormaker.sh  
  
ENTRYPOINT ["sh", "-ex", "./mirrormaker.sh"]  

