FROM frolvlad/alpine-glibc:alpine-3.7  
  
MAINTAINER dockerfiles@nearpod.com  
  
WORKDIR /usr/local  
  
ARG KAFKA_HEALTH_CHECK_VERSION=0.0.2  
  
ENV KAFKA_USER=kafka  
ENV LANG="C.UTF-8"  
RUN set -ex; \  
WORKDIR="$PWD"; \  
apk --no-cache add ca-certificates curl bash tini; \  
curl -q -sSLO "https://github.com/andreas-schroeder/kafka-health-
check/releases/download/v${KAFKA_HEALTH_CHECK_VERSION}/kafka-health-
check_${KAFKA_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz"; \  
curl -q -sSLO "https://github.com/andreas-schroeder/kafka-health-
check/releases/download/v${KAFKA_HEALTH_CHECK_VERSION}/kafka-health-
check_${KAFKA_HEALTH_CHECK_VERSION}_checksums.txt"; \  
grep "kafka-health-check_${KAFKA_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz"
"kafka-health-check_${KAFKA_HEALTH_CHECK_VERSION}_checksums.txt" | sha256sum
-c; \  
tar -xzf "kafka-health-check_${KAFKA_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz"
-C /usr/local/bin kafka-health-check; \  
rm -f "kafka-health-check_${KAFKA_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz"
"kafka-health-check_${KAFKA_HEALTH_CHECK_VERSION}_checksums.txt"  
RUN set -ex; \  
WORKDIR="$PWD"; \  
addgroup -g 1000 "$KAFKA_USER"; \  
adduser -D -h "$WORKDIR" -u 1000 -G "$KAFKA_USER" "$KAFKA_USER"; \  
[ `id -u "$KAFKA_USER"` -eq 1000 ]; \  
[ `id -g "$KAFKA_USER"` -eq 1000 ]  
  
USER kafka:kafka  
  
ENTRYPOINT ["/sbin/tini", "--"]  

