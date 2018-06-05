FROM pdouble16/autopilotpattern-base:1.2.0  
FROM alpine:3.7  
  
ARG BUILD_DATE  
ARG SOURCE_TYPE  
ARG SOURCE_REF  
ARG DOCKERFILE_PATH  
  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
# The official Prometheus base image has no package manager so rather than  
# artisanally hand-rolling curl and the rest of our stack we'll just use  
# Alpine so we can use `docker build`.  
  
ENV CONTAINERPILOT="/etc/containerpilot.json5"  
  
RUN apk add \--no-cache curl bash jq \  
# add Prometheus. alas, the Prometheus developers provide no checksum  
&& export PROM_VERSION=1.7.2 \  
&& export
PROM_CHECKSUM=a5d56b613b77e1d12e99ed5f77359d097c63cb6db64e8b04496eff186df11484
\  
&& export prom=prometheus-${PROM_VERSION}.linux-amd64 \  
&& curl -Lso /tmp/${prom}.tar.gz
https://github.com/prometheus/prometheus/releases/download/v${PROM_VERSION}/${prom}.tar.gz
\  
&& echo "${PROM_CHECKSUM} /tmp/${prom}.tar.gz" | sha256sum -c \  
&& tar zxf /tmp/${prom}.tar.gz -C /tmp \  
&& mkdir /etc/prometheus /usr/share/prometheus \  
&& mv /tmp/${prom}/prometheus /bin/prometheus \  
&& mv /tmp/${prom}/promtool /bin/promtool \  
&& mv /tmp/${prom}/prometheus.yml /etc/prometheus/ \  
&& mv /tmp/${prom}/consoles /usr/share/prometheus/consoles \  
&& mv /tmp/${prom}/console_libraries /usr/share/prometheus/console_libraries \  
&& ln -s /usr/share/prometheus/console_libraries
/usr/share/prometheus/consoles/ /etc/prometheus/ \  
&& rm /tmp/prometheus-${PROM_VERSION}.linux-amd64.tar.gz \  
# Install Consul template, releases at https://releases.hashicorp.com/consul-
template/  
&& export CONSUL_TEMPLATE_VERSION=0.18.5 \  
&& export
CONSUL_TEMPLATE_CHECKSUM=b0cd6e821d6150c9a0166681072c12e906ed549ef4588f73ed58c9d834295cd2
\  
&& curl \--retry 7 \--fail -Lso /tmp/consul-template.zip
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& echo "${CONSUL_TEMPLATE_CHECKSUM} /tmp/consul-template.zip" | sha256sum -c
\  
&& unzip /tmp/consul-template.zip -d /usr/local/bin \  
&& rm /tmp/consul-template.zip  
# Add Containerpilot configuration  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
  
# Add Prometheus config template  
# ref https://prometheus.io/docs/operating/configuration/  
# for details on building your own config  
COPY etc/prometheus.yml.ctmpl /etc/prometheus/prometheus.yml.ctmpl  
COPY bin /usr/local/bin  
  
WORKDIR /prometheus  
ENTRYPOINT []  
CMD ["/usr/local/bin/containerpilot"]  
  
HEALTHCHECK \--interval=1m30s \--timeout=10s \--retries=3 CMD /usr/bin/test
"$(cat /var/run/healthcheck)" = "0" || exit 1  
  
LABEL maintainer="Patrick Double (pat@patdouble.com)" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://bitbucket.org/double16" \  
org.label-schema.name="Autopilot Prometheus Server" \  
org.label-schema.url="https://github.com/double16/autopilotpattern-prometheus"
\  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type='git' \  
org.label-schema.vcs-url="https://github.com/double16/autopilotpattern-
prometheus.git"  

