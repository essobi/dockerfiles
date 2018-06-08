FROM sandinh/varnish  
  
ARG CONSUL_TEMPLATE_VERSION=0.19.4  
ARG BUILD_PACKAGES="wget"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
$BUILD_PACKAGES && \  
wget --no-check-certificate -qO /tmp/consul-template.tgz \  
https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tgz && \  
tar -xzf /tmp/consul-template.tgz -C /usr/bin && \  
rm /tmp/consul-template.tgz && \  
apt-get purge -y --auto-remove $BUILD_PACKAGES && \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /  

