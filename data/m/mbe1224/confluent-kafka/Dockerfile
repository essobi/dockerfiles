FROM mbe1224/confluent-base:3.3.0  
ENV COMPONENT=kafka  
  
EXPOSE 9092  
RUN echo "===> installing ${COMPONENT}..." \  
&& apt-get update && apt-get install -y confluent-
kafka-${SCALA_VERSION}=${KAFKA_VERSION}-${CONFLUENT_DEB_VERSION} \  
&& echo "===> clean up ..." \  
&& apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* \  
&& echo "===> Setting up ${COMPONENT} dirs..." \  
&& mkdir -p /var/lib/${COMPONENT}/data /etc/${COMPONENT}/secrets
/etc/confluent/docker \  
&& chmod -R ag+w /etc/${COMPONENT} /var/lib/${COMPONENT}/data
/etc/${COMPONENT}/secrets \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/ensure" -O
"/etc/confluent/docker/ensure" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/kafka.properties.template"
-O "/etc/confluent/docker/kafka.properties.template" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/launch" -O
"/etc/confluent/docker/launch" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/log4j.properties.template"
-O "/etc/confluent/docker/log4j.properties.template" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/run" -O
"/etc/confluent/docker/run" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka/include/etc/confluent/docker/tools-
log4j.properties.template" -O "/etc/confluent/docker/tools-
log4j.properties.template" \  
&& chmod a+x "/etc/confluent/docker/ensure" \  
&& chmod a+x "/etc/confluent/docker/launch" \  
&& chmod a+x "/etc/confluent/docker/run"  
COPY "/include/etc/confluent/docker/configure"
"/etc/confluent/docker/configure"  
RUN chmod a+x "/etc/confluent/docker/configure"  
  
VOLUME ["/var/lib/${COMPONENT}/data", "/etc/${COMPONENT}/secrets"]  
  
CMD ["/etc/confluent/docker/run"]

