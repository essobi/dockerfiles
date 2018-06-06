FROM travix/base-alpine:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV CONSUL_VERSION=0.6.4  
# install consul.io server  
RUN apk --update add \  
curl \  
unzip \  
&& rm /var/cache/apk/* \  
&& mkdir -p /opt/consul /data \  
&& curl -fSL
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
-o consul.zip \  
&& unzip consul.zip -d /opt/consul \  
&& rm -f consul.zip  
  
COPY ./config /config/  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
# runtime environment variables  
ENV DATA_CENTER_NAME="dc1" \  
BOOTSTRAP_EXPECT="" \  
JOIN_CLUSTER_ADDRESS="" \  
CONSUL_LOCAL_CONFIG='{"ui":true,"dns_config":{"allow_stale": false}}' \  
CONSUL_PARAMS="-server" \  
ATLAS_NAME="" \  
ATLAS_TOKEN=""  
CMD echo "${CONSUL_LOCAL_CONFIG}" > /config/local_config.json; \  
consulParameters="agent ${CONSUL_PARAMS} -config-dir=/config
-dc=${DATA_CENTER_NAME}"; \  
if [ "${BOOTSTRAP_EXPECT}" != "" ]; then \  
consulParameters="${consulParameters} -bootstrap-expect=${BOOTSTRAP_EXPECT}";
\  
fi; \  
if [ "${JOIN_CLUSTER_ADDRESS}" != "" ]; then \  
consulParameters="${consulParameters} -retry-join=${JOIN_CLUSTER_ADDRESS}"; \  
fi; \  
if [ "${ATLAS_NAME}" != "" ]; then \  
consulParameters="${consulParameters} -atlas=${ATLAS_NAME}"; \  
if [ "${ATLAS_TOKEN}" != "" ]; then \  
consulParameters="${consulParameters} -atlas-token=${ATLAS_TOKEN} -atlas-
join"; \  
fi; \  
fi; \  
echo "Starting /opt/consul/consul $consulParameters"; \  
/opt/consul/consul $consulParameters

