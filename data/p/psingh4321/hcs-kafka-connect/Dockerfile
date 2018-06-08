FROM confluentinc/cp-kafka-connect-base  
  
LABEL io.confluent.docker=true  
ARG COMMIT_ID=unknown  
LABEL io.confluent.docker.git.id=$COMMIT_ID  
ARG BUILD_NUMBER=-1  
LABEL io.confluent.docker.build.number=$BUILD_NUMBER  
  
COPY jars/. /etc/kafka-connect/jars/  
  
ENV COMPONENT=kafka-connect  
  
RUN echo "===> Installing JDBC, Elasticsearch and Hadoop connectors ..." \  
&& apt-get -qq update \  
&& apt-get install -y \  
confluent-kafka-connect-
jdbc=${CONFLUENT_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION}
\  
confluent-kafka-connect-
hdfs=${CONFLUENT_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION}
\  
confluent-kafka-connect-
elasticsearch=${CONFLUENT_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION}
\  
confluent-kafka-connect-storage-
common=${CONFLUENT_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION}
\  
confluent-kafka-
connect-s3=${CONFLUENT_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION}
\  
&& echo "===> Cleaning up ..." \  
&& apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/*  
  

