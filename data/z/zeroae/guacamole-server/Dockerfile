#  
# Dockerfile for guacd in autopilot mode.  
#  
# Start from CentOS base image  
FROM guacamole/guacd:latest  
MAINTAINER Patrick Sodre <psodre@gmail.com>  
  
# Environment variables  
ENV \  
CONSUL_VERSION=0.7.2 \  
CONSUL_SHA256=aa97f4e5a552d986b2a36d48fdc3a4a909463e7de5f726f3c5a89b8a1be74a58
\  
CONSUL_TEMPLATE_VERSION=0.16.0 \  
CONSUL_TEMPLATE_SHA256=064b0b492bb7ca3663811d297436a4bbf3226de706d2b76adade7021cd22e156
\  
CONTAINERPILOT_VERSION=2.6.0 \  
CONTAINERPILOT_SHA1=c1bcd137fadd26ca2998eec192d04c08f62beb1f \  
CONTAINERPILOT=file:///etc/containerpilot.json  
  
# We need unzip for installing CONSUL  
RUN rm -Rf /etc/yum.repos.d/epel.repo \  
&& yum -y install unzip \  
&& yum clean all  
  
# Install Consul  
# Releases at https://releases.hashicorp.com/consul  
RUN curl --retry 7 --fail -vo /tmp/consul.zip \  
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
\  
&& echo "${CONSUL_SHA256} /tmp/consul.zip" | sha256sum -c \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& rm /tmp/consul.zip \  
&& mkdir /config  
  
# Create empty directories for Consul config and data  
RUN mkdir -p /etc/consul \  
&& mkdir -p /var/lib/consul  
  
  
# Install Consul template  
# Releases at https://releases.hashicorp.com/consul-template/  
RUN curl --retry 7 --fail -Lso /tmp/consul-template.zip \  
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& echo "${CONSUL_TEMPLATE_SHA256} /tmp/consul-template.zip" | sha256sum -c \  
&& unzip /tmp/consul-template.zip -d /usr/local/bin \  
&& rm /tmp/consul-template.zip  
  
  
# Install ContainerPilot  
# Releases at https://github.com/joyent/containerpilot/  
RUN curl --retry 7 --fail -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz"
\  
&& echo "${CONTAINERPILOT_SHA1} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \  
&& rm /tmp/containerpilot.tar.gz  
  
# Copy configuration files  
COPY etc /etc  
  
# Start guacd, listening on port 0.0.0.0:4822  
EXPOSE 4822  
CMD [ "/usr/local/bin/containerpilot", \  
"/usr/local/sbin/guacd", "-b", "0.0.0.0", "-f" ]  
  

