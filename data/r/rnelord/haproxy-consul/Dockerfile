FROM ubuntu  
  
ENV CONSUL_TEMPLATE_VERSION=0.8.0  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y haproxy=1.5.4-1ubuntu2.1~ubuntu14.04.1 && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \  
rm -rf /var/lib/apt/lists/*  
  
ADD https://github.com/hashicorp/consul-
template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz /  
  
RUN tar zxvf consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz &&
\  
mv consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64/consul-template
/usr/local/bin/consul-template && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64  
  
RUN mkdir -p /haproxy /consul-template/config.d /consul-template/template.d  
  
VOLUME /consul-template  
  
ENTRYPOINT ["consul-template"]  
CMD ["-consul", "consul.service.consul:8500", \  
"-config", "/consul-template/config.d", \  
"-wait", "2s:10s"]  

