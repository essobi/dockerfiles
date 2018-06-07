FROM jboss/base-jdk:8  
MAINTAINER "Kamesh Sampath<kamesh.sampath@hotmail.com>"  
USER root  
  
ENV ACTIVEMQ_ARTEMIS_VERSION 2.4.0  
ENV ARTEMIS_HOME /opt/apache-artemis-${ACTIVEMQ_ARTEMIS_VERSION}  
ENV BROKERS_HOME /opt/brokers  
ENV BROKER_NAME mybroker  
ENV ARTEMIS_USER jboss  
ENV ARTEMIS_PASSWORD jboss  
  
RUN yum -y install epel-release && \  
yum -y install wget curl xmlstarlet \  
&& yum -y clean all \  
&& rm -rf /var/cache/yum \  
&& cd /opt \  
&& wget -q
https://repository.apache.org/content/repositories/releases/org/apache/activemq/apache-
artemis/${ACTIVEMQ_ARTEMIS_VERSION}/apache-
artemis-${ACTIVEMQ_ARTEMIS_VERSION}-bin.tar.gz && \  
wget -q
https://repository.apache.org/content/repositories/releases/org/apache/activemq/apache-
artemis/${ACTIVEMQ_ARTEMIS_VERSION}/apache-
artemis-${ACTIVEMQ_ARTEMIS_VERSION}-bin.tar.gz.asc && \  
wget -q http://apache.org/dist/activemq/KEYS && \  
gpg --import KEYS && \  
gpg apache-artemis-${ACTIVEMQ_ARTEMIS_VERSION}-bin.tar.gz.asc && \  
tar xfz apache-artemis-${ACTIVEMQ_ARTEMIS_VERSION}-bin.tar.gz && \  
mkdir -p /opt/brokers && \  
${ARTEMIS_HOME}/bin/artemis create ${BROKERS_HOME}/${BROKER_NAME} \  
\--home ${ARTEMIS_HOME} \  
\--user ${ARTEMIS_USER} \  
\--password ${ARTEMIS_PASSWORD} \  
\--allow-anonymous  
  
COPY run-broker.sh container-limits java-default-options ${BROKERS_HOME}/  
  
RUN chmod 755 ${BROKERS_HOME}/run-broker.sh ${BROKERS_HOME}/java-default-
options ${BROKERS_HOME}/container-limits \  
&& chown -R jboss ${BROKERS_HOME} \  
&& usermod -g root -G `id -g jboss` jboss \  
&& chmod -R "g+rwX" ${BROKERS_HOME} \  
&& chown -R jboss:root ${BROKERS_HOME} \  
&& cd ${BROKERS_HOME}/${BROKER_NAME}/etc && \  
xmlstarlet ed -L -N amq="http://activemq.org/schema" \  
-u "/amq:broker/amq:web/@bind" \  
-v "http://0.0.0.0:8161" bootstrap.xml  
  
EXPOSE 8161 61616 5445 5672 1883 61613  
#TODO volumes  
USER jboss  
  
CMD [ "/bin/sh","-c", "${BROKERS_HOME}/run-broker.sh" ]

