FROM alpine:3.5  
# Alpine packages  
RUN apk --no-cache \  
add \  
curl \  
bash \  
ca-certificates  
  
# The Consul binary  
ENV CONSUL_VERSION=0.7.3-rfc2782 \  
CONSUL_URL_BASE=https://github.com/zeroae/consul/releases/download \  
CONSUL_CHECKSUM=9c13de0de9697fc646899cbf58d39d13b061c803c2d306c321281246890d1576
\  
CONSUL_UI_CHECKSUM=dfdc79391dafb72aefa6c1e114b242a1c4385ccb066f9cfa60001f741f0014e6  
RUN export archive=consul_${CONSUL_VERSION}_linux_amd64.zip \  
&& curl -Lso /tmp/${archive} ${CONSUL_URL_BASE}/v${CONSUL_VERSION}/${archive}
\  
&& echo "${CONSUL_CHECKSUM} /tmp/${archive}" | sha256sum -c \  
&& cd /bin \  
&& unzip /tmp/${archive} \  
&& chmod +x /bin/consul \  
&& rm /tmp/${archive}  
  
# The Consul web UI  
RUN export archive=consul_${CONSUL_VERSION}_web_ui.zip \  
&& curl -Lso /tmp/${archive} ${CONSUL_URL_BASE}/v${CONSUL_VERSION}/${archive}
\  
&& echo "${CONSUL_UI_CHECKSUM} /tmp/${archive}" | sha256sum -c \  
&& mkdir /ui \  
&& cd /ui \  
&& unzip /tmp/${archive} \  
&& rm /tmp/${archive}  
  
# Add Containerpilot and set its configuration  
ENV CONTAINERPILOT_VERSION 2.6.0  
ENV CONTAINERPILOT file:///etc/containerpilot.json  
  
RUN export CONTAINERPILOT_CHECKSUM=c1bcd137fadd26ca2998eec192d04c08f62beb1f \  
&& export archive=containerpilot-${CONTAINERPILOT_VERSION}.tar.gz \  
&& curl -Lso /tmp/${archive} \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/${archive}"
\  
&& echo "${CONTAINERPILOT_CHECKSUM} /tmp/${archive}" | sha1sum -c \  
&& tar zxf /tmp/${archive} -C /usr/local/bin \  
&& rm /tmp/${archive}  
  
# configuration files and bootstrap scripts  
COPY etc/containerpilot.json etc/  
COPY etc/consul.json etc/consul/  
COPY bin/* /usr/local/bin/  
  
# Put Consul data on a separate volume to avoid filesystem performance issues  
# with Docker image layers. Not necessary on Triton, but...  
VOLUME ["/data"]  
  
# We don't need to expose these ports in order for other containers on Triton  
# to reach this container in the default networking environment, but if we  
# leave this here then we get the ports as well-known environment variables  
# for purposes of linking.  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
  
#ENV GOMAXPROCS 2  
ENV SHELL /bin/bash  

