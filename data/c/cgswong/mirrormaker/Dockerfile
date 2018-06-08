FROM cgswong/confluent-platform:1.0b2.11.5  
  
ENV CONFLUENT_USER confluent  
ENV CONFLUENT_GROUP confluent  
ENV MM_CFG_DIR "/etc/kafka-mirrormaker"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY mirrormaker-docker.sh /usr/local/bin/  
  
RUN apt-get -y update &&\  
apt-get -y upgrade &&\  
apt-get -y install \  
openssh-client &&\  
groupadd -r ${CONFLUENT_GROUP} &&\  
useradd -r -g ${CONFLUENT_GROUP} ${CONFLUENT_USER} &&\  
mkdir -p ${MM_CFG_DIR}/.ssh &&\  
chown -R ${CONFLUENT_USER}:${CONFLUENT_GROUP} /usr/local/bin/mirrormaker-
docker.sh ${MM_CFG_DIR} &&\  
chmod 700 ${MM_CFG_DIR}/.ssh &&\  
chmod +x /usr/local/bin/mirrormaker-docker.sh  
  
USER ${CONFLUENT_USER}  
  
VOLUME [ "${MM_CFG_DIR}" ]  
  
ENTRYPOINT ["/usr/local/bin/mirrormaker-docker.sh"]  

