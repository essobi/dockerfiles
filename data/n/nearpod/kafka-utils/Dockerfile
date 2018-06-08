FROM nearpod/kafka:kafka-1.0.0  
  
ARG KAFKA_UTILS_USER=kafka  
ARG KAFKACAT_VERSION=1.3.1  
  
ENV HOME=/config  
  
USER root  
  
RUN set -ex; \  
WORKDIR=$(pwd); \  
apk add \--no-cache bash bash-completion curl ca-certificates python2 openssl
librdkafka; \  
apk add \--no-cache --virtual build-dependencies python-dev build-base py2-pip
libffi-dev openssl-dev librdkafka-dev; \  
pip install kafka-utils; \  
curl -q -sSLO
"https://github.com/edenhill/kafkacat/archive/${KAFKACAT_VERSION}.tar.gz"; \  
tar -xf "${KAFKACAT_VERSION}.tar.gz"; \  
cd kafkacat-"${KAFKACAT_VERSION}"; \  
./configure; make; make install; \  
cd "$WORKDIR"; \  
rm -rf "${KAFKACAT_VERSION}.tar.gz" "kafkacat-${KAFKACAT_VERSION}"; \  
apk del build-dependencies  
  
WORKDIR /config  
  
USER kafka  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
[ `id -u "$KAFKA_UTILS_USER"` -eq 1000 ]; \  
[ `id -g "$KAFKA_UTILS_USER"` -eq 1000 ]; \  
kafka-utils -v; \  
kafkacat -V  

