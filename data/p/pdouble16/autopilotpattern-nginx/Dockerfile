# A minimal Nginx container including ContainerPilot  
FROM pdouble16/autopilotpattern-base:1.2.0  
FROM debian:stretch-slim  
  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
  
ENV NGINX_VERSION="1.10.3-1+deb9u1" \  
CONTAINERPILOT="/etc/containerpilot.json5"  
  
RUN echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
nginx-extras=${NGINX_VERSION} gettext-base \  
bc \  
ca-certificates \  
curl \  
unzip \  
procps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/local/lib/lua && curl \--fail -s -o
/usr/local/lib/lua/prometheus.lua
https://raw.githubusercontent.com/knyar/nginx-lua-
prometheus/24ab338427bcfd121ac6c9a264a93d482e115e14/prometheus.lua \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
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
&& rm /tmp/consul-template.zip \  
# Add Dehydrated  
&& export DEHYDRATED_VERSION=v0.3.1 \  
&& curl \--retry 8 \--fail -Lso /tmp/dehydrated.tar.gz
"https://github.com/lukas2511/dehydrated/archive/${DEHYDRATED_VERSION}.tar.gz"
\  
&& tar xzf /tmp/dehydrated.tar.gz -C /tmp \  
&& mv /tmp/dehydrated-0.3.1/dehydrated /usr/local/bin \  
&& rm -rf /tmp/dehydrated-0.3.1 \  
# Add jq  
&& export JQ_VERSION=1.5 \  
&& curl \--retry 8 \--fail -Lso /usr/local/bin/jq
"https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64"
\  
&& chmod a+x /usr/local/bin/jq \  
# Add our configuration files and scripts  
&& rm -f /etc/nginx/conf.d/default.conf \  
# Usable SSL certs written here  
&& mkdir -p /var/www/ssl \  
# Temporary/work space for keys  
&& mkdir -p /var/www/acme/ssl \  
# ACME challenge tokens written here  
&& mkdir -p /var/www/acme/challenge  
  
COPY etc/acme /etc/acme  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
COPY etc/nginx /etc/nginx/templates  
COPY bin /usr/local/bin  
  
EXPOSE 80 443  
  
STOPSIGNAL SIGQUIT  
  
CMD [ "/usr/local/bin/containerpilot"]  
  
LABEL maintainer="Patrick Double <pat@patdouble.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.name="Autopilot Pattern Nginx with Extras and Full Prometheus
Monitoring" \  
org.label-schema.url="https://github.com/double16/autopilotpattern-nginx" \  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type='git' \  
org.label-schema.vcs-url="https://github.com/double16/autopilotpattern-
nginx.git"  

