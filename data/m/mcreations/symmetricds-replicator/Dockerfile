FROM mcreations/symmetricds:3.8.16  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
MAINTAINER Yousef Irman <irman@m-creations.net>  
  
ENV MASTER_JDBC ""  
ENV MASTER_USER ""  
ENV MASTER_PASSWORD ""  
ENV MASTER_JDBC_DRIVER ""  
ENV SLAVE_JDBC ""  
ENV SLAVE_USER ""  
ENV SLAVE_PASSWORD ""  
ENV SLAVE_JDBC_DRIVER ""  
ENV MASTER_ENGINE=masterEngine  
ENV MASTER_ID=000  
ENV MASTER_GROUP_ID=masterGroup  
ENV SLAVE_ENGINE=slaveEngine  
ENV SLAVE_ID=001  
ENV SLAVE_GROUP_ID=slaveGroup  
ENV MASTER_SLAVE_ROUTER=master_2_slave_router  
ENV SLAVE_MASTER_ROUTER=slave_2_master_router  
ENV PROCESSING_ORDER=100  
ENV MAX_BATCH_SIZE=100000  
ENV INITIAL_BATCH_SIZE=1000  
ENV JOB_PURGE_PERIOD_TIME_MS=7200000  
ENV JOB_ROUTING_PERIOD_TIME_MS=5000  
ENV JOB_PUSH_PERIOD_TIME_MS=10000  
ENV JOB_PULL_PERIOD_TIME_MS=10000  
ENV INITIAL_LOAD_CREATE_FIRST=true  
ENV AUTO_REGISTRATION=true  
ENV AUTO_RELOAD=true  
  
ENV SYMMETRICDS_FOLDER=/opt/symds-configurator  
ENV SYMMETRICDS_CONFIGURATOR_VERSION=1.0  
ENV SYMMETRICDS_CONFIGURATOR_ARTIFACT_ID=symmetricds-configurator  
ENV
SYMMETRICDS_CONFIGURATOR_ARTIFACT=${SYMMETRICDS_CONFIGURATOR_ARTIFACT_ID}-${SYMMETRICDS_CONFIGURATOR_VERSION}-standalone.jar  
  
RUN opkg update && opkg install mariadb-client mariadb-client-extra && rm -rf
/tmp/opkg-lists/* &&\  
for d in engines logs tmp ; do mkdir -p /data/$d ; rm -rf
${SYMMETRICDS_HOME}/$d ; ln -s /data/$d ${SYMMETRICDS_HOME}/ ; done &&\  
echo 'export PATH=$PATH:$SYMMETRICDS_HOME/bin' >> /etc/profile &&\  
mkdir -p ${SYMMETRICDS_FOLDER} &&\  
wget --progress=dot:mega -O
${SYMMETRICDS_FOLDER}/${SYMMETRICDS_CONFIGURATOR_ARTIFACT}
https://search.maven.org/remotecontent?filepath=com/m-creations/symmetricds/${SYMMETRICDS_CONFIGURATOR_ARTIFACT_ID}/${SYMMETRICDS_CONFIGURATOR_VERSION}/${SYMMETRICDS_CONFIGURATOR_ARTIFACT}  
  
ADD image/root /  
  
CMD ["/start-symmertic-ds-replicator"]  

