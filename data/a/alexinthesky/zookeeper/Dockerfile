FROM zookeeper:3.4.11  
  
LABEL org.label-schema.vendor="ITM Red"  
LABEL org.label-schema.name="dockerhub.sandbox.pfex.digitas.fr/red/zookeeper"  
LABEL org.label-schema.description="The zookeeper ITM Red docker image"  
ENV CONSUL_TEMPLATE_VERSION=0.19.4  
ENV ZK_HOME=/zookeeper-3.4.11  
  
RUN addgroup zk && adduser -S -G zk zk  
  
# Set up certificates, our base tools, and Consul.  
RUN apk add \--update \--no-cache jq curl && \  
mkdir -p /tmp/build && \  
cd /tmp/build && \  
curl -O https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
cp consul-template /bin && \  
cd /tmp && \  
rm -rf /tmp/build && \  
apk del gnupg && \  
rm -rf /root/.gnupg  
  
ENV CLUSTER_ID="MYCLUSTER" \  
CONSUL_HOST="localhost" \  
CONSUL_PORT=8500  
  
EXPOSE 2181 2888 3888  
COPY ./start-zk /  
COPY ./get-container-id.sh /  
COPY ./get-container-id_swarm.sh /  
RUN chmod +x /get-container-id.sh /get-container-id_swarm.sh  
CMD ["/start-zk"]  
  

