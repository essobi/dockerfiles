FROM debian:jessie-slim  
  
LABEL maintainer 'Guangwen Zhou <zgwmike@hotmail.com>'  
  
RUN apt-get update && apt-get install -y openssl libapr1 libexpat1 ca-
certificates  
  
ENV SIDECAR_BINARY_URL https://github.com/Graylog2/collector-
sidecar/releases/download/0.1.5/collector-sidecar_0.1.5-1_amd64.deb  
RUN apt-get install -y --no-install-recommends curl && curl -Lo collector.deb
${SIDECAR_BINARY_URL} && dpkg -i collector.deb && rm collector.deb && apt-get
purge -y --auto-remove curl  
  
ENV GS_UPDATE_INTERVAL=60 \  
GS_SEND_STATUS="true" \  
GS_LIST_LOG_FILES="[]" \  
GS_COLLECTOR_ID="file:/etc/graylog/collector-sidecar/collector-id" \  
GS_LOG_ROTATION_TIME=86400 \  
GS_LOG_MAX_AGE=604800 \  
GS_NODE_ID="graylog-collector-sidecar"  
ADD ./sidecar /sidecar  
  
CMD /sidecar/start.sh

