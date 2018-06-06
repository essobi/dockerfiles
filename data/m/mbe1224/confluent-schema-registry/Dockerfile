FROM mbe1224/confluent-base:3.3.0  
ENV COMPONENT=schema-registry  
  
EXPOSE 8081  
RUN echo "===> installing ${COMPONENT}..." \  
&& apt-get update && apt-get install -y
confluent-${COMPONENT}=${CONFLUENT_VERSION}-${CONFLUENT_DEB_VERSION} \  
&& echo "===> clean up ..." \  
&& apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* \  
&& echo "===> Setting up ${COMPONENT} dirs" \  
&& mkdir -p /etc/${COMPONENT}/secrets /etc/confluent/docker \  
&& chmod -R ag+w /etc/${COMPONENT} /etc/${COMPONENT}/secrets \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/admin.properties.template" -O
"/etc/confluent/docker/admin.properties.template" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/apply-mesos-overrides" -O
"/etc/confluent/docker/apply-mesos-overrides" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/configure" -O
"/etc/confluent/docker/configure" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/ensure" -O
"/etc/confluent/docker/ensure" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/launch" -O
"/etc/confluent/docker/launch" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/log4j.properties.template" -O
"/etc/confluent/docker/log4j.properties.template" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-registry/include/etc/confluent/docker/run"
-O "/etc/confluent/docker/run" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/schema-
registry/include/etc/confluent/docker/schema-registry.properties.template" -O
"/etc/confluent/docker/schema-registry.properties.template" \  
&& chmod a+x "/etc/confluent/docker/apply-mesos-overrides" \  
&& chmod a+x "/etc/confluent/docker/configure" \  
&& chmod a+x "/etc/confluent/docker/ensure" \  
&& chmod a+x "/etc/confluent/docker/launch" \  
&& chmod a+x "/etc/confluent/docker/run"  
  
VOLUME ["/etc/${COMPONENT}/secrets"]  
  
CMD ["/etc/confluent/docker/run"]

