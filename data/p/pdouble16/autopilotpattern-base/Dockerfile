FROM alpine:3.7  
ARG BUILD_DATE  
ARG DOCKERFILE_PATH  
ARG SOURCE_REF  
ARG SOURCE_TYPE  
  
ENV CONSUL_VERSION="1.1.0" \  
CONTAINERPILOT_VER="3.8.0" CONTAINERPILOT="/etc/containerpilot.json5" \  
NODE_EXPORTER_VERSION="0.15.2"  
RUN apk --no-cache add curl bash \  
&& export
CONSUL_CHECKSUM=09c40c8b5be868003810064916d8460bff334ccfb59a5046390224b27e052c45
\  
&& curl --retry 7 --fail -vo /tmp/consul.zip
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
\  
&& echo "${CONSUL_CHECKSUM} /tmp/consul.zip" | sha256sum -c \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& rm /tmp/consul.zip \  
&& mkdir -p /etc/consul \  
&& export CONTAINERPILOT_CHECKSUM=84642c13683ddae6ccb63386e6160e8cb2439c26 \  
&& curl -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz"
\  
&& echo "${CONTAINERPILOT_CHECKSUM} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \  
&& rm /tmp/containerpilot.tar.gz \  
&& curl --fail -sL
"https://github.com/prometheus/node_exporter/releases/download/v${NODE_EXPORTER_VERSION}/node_exporter-${NODE_EXPORTER_VERSION}.linux-
amd64.tar.gz" |\  
tar -xzO -f - node_exporter-${NODE_EXPORTER_VERSION}.linux-amd64/node_exporter
> /usr/local/bin/node_exporter \  
&& chmod +x /usr/local/bin/node_exporter \  
&& rm -rf /tmp/*  
  
COPY bin/consul-manage /usr/local/bin/consul-manage  
COPY etc/consul.hcl /etc/consul/consul.hcl.orig  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
  
CMD ["/usr/local/bin/containerpilot"]  
  
HEALTHCHECK \--interval=60s --timeout=10s --retries=3 CMD
["/usr/local/bin/consul-manage", "health"] || exit 1  
  
LABEL maintainer="Patrick Double <pat@patdouble.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://github.com/double16" \  
org.label-schema.name="Autopilot Multi-Stage Base with Consul and Prometheus
Monitoring" \  
org.label-schema.url="https://github.com/double16/autopilotpattern-base" \  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type=$SOURCE_TYPE \  
org.label-schema.vcs-url="https://github.com/double16/autopilotpattern-
base.git"  

