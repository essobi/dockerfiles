## -*- docker-image-name: "docker-kafka" -*-  
#  
# Kafka Dockerfile  
# https://github.com/aelesbao/docker-kafka  
#  
FROM openjdk:8-jre-alpine  
MAINTAINER Augusto Elesbão <augusto@dharma.ws>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/aelesbao/docker-kafka.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1"  
  
# Install run dependencies  
RUN apk add --no-cache --virtual .run-deps \  
bash \  
su-exec  
  
ENV SCALA_VERSION="2.12" \  
KAFKA_VERSION="0.11.0.0" \  
KAFKA_HOME=/kafka \  
KAFKA_PORT=9092 \  
JMX_PORT=7203  
# Install Kafka  
RUN apk add --no-cache --virtual .build-deps \  
tar \  
gnupg \  
openssl \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& export KAFKA_RELEASE_ARCHIVE=kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
&& cd /tmp \  
&& wget -O ${KAFKA_RELEASE_ARCHIVE}
"https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}"
\  
&& wget -O ${KAFKA_RELEASE_ARCHIVE}.asc
"https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.asc"
\  
&& gpg --keyserver hkps.pool.sks-keyservers.net --recv-keys AB55EF5C \  
&& gpg --batch --verify ${KAFKA_RELEASE_ARCHIVE}.asc ${KAFKA_RELEASE_ARCHIVE}
\  
&& mkdir -p ${KAFKA_HOME} /data /logs \  
&& tar -xzf ${KAFKA_RELEASE_ARCHIVE} -C ${KAFKA_HOME} \--strip-components=1 \  
&& rm -rf /tmp/* \  
&& apk del .build-deps  
  
ADD config ${KAFKA_HOME}/config  
RUN adduser -D -h ${KAFKA_HOME} kafka kafka \  
&& chown -R kafka:kafka ${KAFKA_HOME} /data /logs  
  
WORKDIR ${KAFKA_HOME}  
ENV PATH ${KAFKA_HOME}/bin:${PATH}  
  
VOLUME [ "/data", "/logs" ]  
EXPOSE ${KAFKA_PORT} ${JMX_PORT}  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start-kafka"]  

