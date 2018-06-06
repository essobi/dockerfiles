# Builds a docker image for the Kafka REST Proxy.  
FROM cgswong/confluent-platform:1.0.1  
ENV CONFLUENT_USER confluent  
ENV CONFLUENT_GROUP confluent  
ENV RP_CFGDIR "/etc/kafka-rest"  
ENV JMX_PORT 18082  
COPY kafka-rest-docker.sh /usr/local/bin/  
COPY log4j.properties ${SR_CFGDIR}/  
  
RUN groupadd -r ${CONFLUENT_GROUP} &&\  
useradd -r -g ${CONFLUENT_GROUP} ${CONFLUENT_USER} &&\  
chown -R ${CONFLUENT_USER}:${CONFLUENT_GROUP} ${RP_CFGDIR} /var/log/kafka
/usr/local/bin/kafka-rest-docker.sh &&\  
chmod +x /usr/local/bin/kafka-rest-docker.sh  
  
USER ${CONFLUENT_USER}  
VOLUME ["${RP_CFGDIR}"]  
# Expose client port (8081/http), JMX  
EXPOSE 8082 ${JMX_PORT}  
  
ENTRYPOINT ["/usr/local/bin/kafka-rest-docker.sh"]  

