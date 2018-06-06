FROM rawmind/alpine-jdk8:1.8.112  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV SERVICE_HOME=/opt/kafka-manager \  
SERVICE_NAME=kafka-manager \  
SERVICE_VERSION=1.3.1.8 \  
SERVICE_USER=kafka \  
SERVICE_UID=10003 \  
SERVICE_GROUP=kafka \  
SERVICE_GID=10003 \  
SERVICE_VOLUME=/opt/tools \  
SERVICE_URL=https://github.com/yahoo/kafka-manager  
ENV SERVICE_CONF=${SERVICE_HOME}/conf/application.conf  
  
# Install and configure kafka manager  
ADD kafka-manager-1.3.1.8.zip /opt/  
RUN unzip /opt/${SERVICE_NAME}-${SERVICE_VERSION}.zip -d /opt/ && \  
rm /opt/${SERVICE_NAME}-${SERVICE_VERSION}.zip && \  
mv /opt/${SERVICE_NAME}-${SERVICE_VERSION} ${SERVICE_HOME} && \  
mkdir ${SERVICE_HOME}/logs && \  
rm ${SERVICE_CONF} && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} &&\  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh \  
&& chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 9000  

