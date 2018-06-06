# Builds a docker image for Kafka MirrorMaker.  
FROM cgswong/confluent-platform:2.0.1  
ENV CONFLUENT_USER confluent  
ENV CONFLUENT_GROUP confluent  
ENV MM_CFGDIR "/etc/kafka-mirrormaker"  
ENV JMX_PORT 7023  
COPY mirrormaker-docker.sh /usr/local/bin/  
COPY tools-log4j.properties ${SR_CFGDIR}/  
  
RUN groupadd -r ${CONFLUENT_GROUP} &&\  
useradd -r -g ${CONFLUENT_GROUP} ${CONFLUENT_USER} &&\  
mkdir -p ${MM_CFGDIR} &&\  
chown -R ${CONFLUENT_USER}:${CONFLUENT_GROUP} /var/log/kafka
/usr/local/bin/mirrormaker-docker.sh ${MM_CFGDIR} &&\  
chmod +x /usr/local/bin/mirrormaker-docker.sh  
  
USER ${CONFLUENT_USER}  
  
VOLUME [ "${MM_CFGDIR}" ]  
# Expose JMX  
EXPOSE ${JMX_PORT}  
  
ENTRYPOINT [ "/usr/local/bin/mirrormaker-docker.sh" ]  

