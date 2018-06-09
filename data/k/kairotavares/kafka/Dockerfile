FROM anapsix/alpine-java  
  
MAINTAINER Wurstmeister  
  
RUN apk add --update unzip wget curl docker jq coreutils sudo grep  
  
ENV KAFKA_VERSION="0.10.1.0" SCALA_VERSION="2.11"  
ADD download-kafka.sh /tmp/download-kafka.sh  
  
RUN chmod a+x /tmp/download-kafka.sh \  
&& /tmp/download-kafka.sh \  
&& tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt \  
&& rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
&& ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka  
  
ENV KAFKA_HOME /opt/kafka  
ENV PATH ${PATH}:${KAFKA_HOME}/bin  
  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
ADD broker-list.sh /usr/bin/broker-list.sh  
ADD create-topics.sh /usr/bin/create-topics.sh  
ADD sudoers /etc/  
  
# The scripts need to have executable permission  
RUN chmod a+x /usr/bin/entrypoint.sh && \  
chmod a+x /usr/bin/start-kafka.sh && \  
chmod a+x /usr/bin/broker-list.sh && \  
chmod a+x /usr/bin/create-topics.sh  
  
# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["start-kafka.sh"]  
  

