# Docker file to create Logstash container.  
FROM cgswong/java:openjre8  
  
# Setup environment  
ENV LS_VERSION 1.5.3  
ENV LS_HOME /opt/logstash  
ENV LS_CFG_BASE_DIR /etc/logstash  
ENV LS_CFG_SSL_DIR ${LS_CFG_BASE_DIR}/.ssl  
ENV LS_CFG_FILE_DIR ${LS_CFG_BASE_DIR}/conf.d  
ENV LS_USER logstash  
ENV LS_GROUP logstash  
  
# Install requirements and Logstash  
RUN apk --update add \  
curl \  
python \  
py-pip \  
bash &&\  
mkdir -p \  
${LS_CFG_SSL_DIR} \  
${LS_CFG_FILE_DIR} \  
/opt &&\  
curl -sSL --insecure --location
https://download.elasticsearch.org/logstash/logstash/logstash-${LS_VERSION}.tar.gz
| tar zxf - -C /opt &&\  
ln -s /opt/logstash-${LS_VERSION} ${LS_HOME} &&\  
addgroup ${LS_GROUP} &&\  
adduser -h ${LS_HOME} -D -s /bin/bash -G ${LS_GROUP} ${LS_USER} &&\  
chown -R ${LS_USER}:${LS_GROUP} ${LS_HOME}/ ${LS_CFG_BASE_DIR} &&\  
chmod 700 ${LS_CFG_SSL_DIR}  
  
# Configure environment  
COPY src/ /  
  
# Listen for defaults: 5000/tcp:udp (syslog), 5002/tcp (logstash-forwarder),
5004/tcp (journald), 5006/udp (Logspout), 4560/tcp (log4j)  
EXPOSE 5000 5002 5004 5006 4560  
# Expose volumes  
VOLUME ["${LS_CFG_BASE_DIR}"]  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [""]  

