FROM mbe1224/confluent-kafka:3.3.0  
  
ENV COMPONENT=kafka-connect  
  
EXPOSE 8083  
  
RUN echo "===> Installing Schema Registry (for Avro jars), JDBC,
Elasticsearch, Hadoop and S3 connectors ..." \  
&& apt-get -qq update \  
&& apt-get install -y \  
confluent-schema-registry=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
confluent-kafka-connect-jdbc=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
confluent-kafka-connect-hdfs=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
confluent-kafka-connect-
elasticsearch=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
confluent-kafka-connect-storage-
common=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
confluent-kafka-connect-s3=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
&& echo "===> Cleaning up ..." \  
&& apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* \  
echo "===> Setting up ${COMPONENT} dirs ..." \  
&& mkdir -p /etc/${COMPONENT} /etc/${COMPONENT}/secrets /etc/${COMPONENT}/jars
/etc/confluent/docker \  
&& chmod -R ag+w /etc/${COMPONENT} /etc/${COMPONENT}/secrets
/etc/${COMPONENT}/jars \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/apply-mesos-overrides" -O
"/etc/confluent/docker/apply-mesos-overrides" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/configure" -O
"/etc/confluent/docker/configure" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/ensure" -O "/etc/confluent/docker/ensure" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/launch" -O "/etc/confluent/docker/launch" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/log4j.properties.template" -O
"/etc/confluent/docker/log4j.properties.template" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/run" -O "/etc/confluent/docker/run" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/kafka-connect-
base/include/etc/confluent/docker/kafka-connect.properties.template" -O
"/etc/confluent/docker/kafka-connect.properties.template" \  
&& chmod a+x "/etc/confluent/docker/apply-mesos-overrides" \  
&& chmod a+x "/etc/confluent/docker/configure" \  
&& chmod a+x "/etc/confluent/docker/ensure" \  
&& chmod a+x "/etc/confluent/docker/launch" \  
&& chmod a+x "/etc/confluent/docker/run"  
  
VOLUME ["/etc/${COMPONENT}/jars", "/etc/${COMPONENT}/secrets"]  
  
CMD ["/etc/confluent/docker/run"]  

