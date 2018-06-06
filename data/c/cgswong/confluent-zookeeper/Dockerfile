# Builds a docker image running Apache Zookeeper. Intended for use with Kafka.  
FROM cgswong/confluent-platform:2.0.1  
ENV ZK_DATADIR "/var/lib/zookeeper"  
ENV CONFLUENT_USER confluent  
ENV CONFLUENT_GROUP confluent  
ENV KAFKA_LOG4J_OPTS -Dlog4j.configuration=file:/etc/kafka/log4j.properties  
ENV ZOOCFGDIR /etc/kafka  
ENV ZOOCFG zookeeper.properties  
ENV JMXPORT 12181  
COPY zkStart.sh /usr/local/bin/  
COPY log4j.properties /etc/kafka/  
  
RUN groupadd -r ${CONFLUENT_GROUP} &&\  
useradd -r -g ${CONFLUENT_GROUP} ${CONFLUENT_USER} &&\  
mkdir -p ${ZK_DATADIR} &&\  
chown -R ${CONFLUENT_GROUP}:${CONFLUENT_USER} ${ZK_DATADIR} ${ZOOCFGDIR}
/var/log/kafka /usr/local/bin/zkStart.sh /etc/kafka/zookeeper.properties &&\  
chmod +x /usr/local/bin/zkStart.sh  
  
USER ${CONFLUENT_USER}  
VOLUME ["${ZK_DATADIR}","${ZOOCFGDIR}"]  
  
# Expose client port (2188/tcp), peer connection port (2888/tcp), leader
election port (3888/tcp), JMX  
EXPOSE 2181 2888 3888 ${JMXPORT}  
  
ENTRYPOINT ["/usr/local/bin/zkStart.sh"]  
CMD [""]  

