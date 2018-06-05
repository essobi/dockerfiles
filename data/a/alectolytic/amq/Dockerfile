FROM centos:7  
  
RUN yum -y install wget tar java  
RUN yum -y clean all  
  
ENV ACTIVEMQ_VERSION=5.13.0  
ENV ACTIVEMQ_MIRROR=http://apache.mirror.uber.com.au  
ENV ACTIVEMQ_URL_PATH=activemq/${ACTIVEMQ_VERSION}/apache-
activemq-${ACTIVEMQ_VERSION}-bin.tar.gz  
ENV ACTIVEMQ_SOURCE=${ACTIVEMQ_MIRROR}/${ACTIVEMQ_URL_PATH}  
ENV ACTIVEMQ_HOME=/opt/apache/activemq/  
ENV ACTIVEMQ_CONF=${ACTIVEMQ_HOME}/conf  
ENV ACTIVEMQ_DATA=${ACTIVEMQ_HOME}/data  
ENV ACTIVEMQ_USER=activemq  
ENV ACTIVEMQ_OPTS=""  
  
ENV HTTP_PORT=8161  
ENV HTTPS_PORT=8162  
ENV OPENWIRE_PORT=61616  
ENV MQTT_PORT=1883  
ENV AMQP_PORT=5672  
ENV STOMP_PORT=61613  
ENV OPENWIRE_SSL_PORT=61617  
ENV MQTT_SSL_PORT=8883  
ENV AMQP_SSL_PORT=5671  
ENV STOMP_SSL_PORT=61614  
  
# copy licence  
COPY LICENSE /LICENSE  
  
# create the parent dir  
RUN mkdir -p $(dirname ${ACTIVEMQ_HOME})  
  
# prepare activemq system user  
RUN useradd \  
\--home-dir ${ACTIVEMQ_HOME} \--no-create-home \  
\--system \  
\--comment "ActiveMQ User" \  
${ACTIVEMQ_USER}  
# create home directory with amq release  
RUN cd /tmp \  
&& TARBALL=$(basename ${ACTIVEMQ_SOURCE}) \  
&& wget \--output-document=${TARBALL} ${ACTIVEMQ_SOURCE} \  
&& tar xvf ${TARBALL} \  
&& mv apache-activemq-${ACTIVEMQ_VERSION} ${ACTIVEMQ_HOME} \  
&& chown -R ${ACTIVEMQ_USER}:${ACTIVEMQ_USER} ${ACTIVEMQ_HOME} \  
&& rm ${TARBALL}  
  
USER ${ACTIVEMQ_USER}  
WORKDIR ${ACTIVEMQ_HOME}  
  
VOLUME ["${ACTIVEMQ_CONF}", "${ACTIVEMQ_DATA}"]  
  
EXPOSE ${HTTP_PORT} ${HTTPS_PORT} ${OPENWIRE_PORT} ${MQTT_PORT} ${AMQP_PORT} \  
${STOMP_PORT} ${OPENWIRE_SSL_PORT} ${MQTT_SSL_PORT} ${AMQP_SSL_PORT} \  
${STOMP_SSL_PORT}  
# workaround for centos JAVA_HOME  
ENV JAVA_HOME=/usr/lib/jvm/jre  
  
ENTRYPOINT ["./bin/activemq"]  
  
CMD ["console"]

