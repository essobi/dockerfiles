FROM heimdallproject/heimdall:dev  
  
# Add some stuff via apk  
RUN apk add \--no-cache \  
curl \  
unzip \  
bc  
  
# Install Consul  
# Releases at https://releases.hashicorp.com/consul  
RUN export CONSUL_VERSION=0.7.3 \  
&& export
CONSUL_CHECKSUM=901a3796b645c3ce3853d5160080217a10ad8d9bd8356d0b73fcd6bc078b7f82
\  
&& curl --retry 7 --fail -vo /tmp/consul.zip
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
\  
&& echo "${CONSUL_CHECKSUM} /tmp/consul.zip" | sha256sum -c \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& rm /tmp/consul.zip \  
&& mkdir /config  
  
# Create empty directories for Consul config and data  
RUN mkdir -p /etc/consul \  
&& mkdir -p /var/lib/consul  
  
# Add Containerpilot and set its configuration  
ENV CONTAINERPILOT_VER 3.0.0-dev.2  
  
RUN export CONTAINERPILOT_CHECKSUM=18332438fa764cc6f3d6bf21de3ae1c0641a42d9 \  
&& curl -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz"
\  
&& echo "${CONTAINERPILOT_CHECKSUM} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /bin \  
&& rm /tmp/containerpilot.tar.gz  
  
# Consul session data written here  
RUN mkdir -p /var/consul \  
&& mkdir -p /usr/local/bin  
  
# Add our configuration files and scripts  
COPY etc /etc  
COPY bin /usr/local/bin  
  
ENTRYPOINT [ "/bin/containerpilot", \  
"-config", \  
"/etc/containerpilot.json"]  

