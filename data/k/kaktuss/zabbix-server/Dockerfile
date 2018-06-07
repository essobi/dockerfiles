FROM zabbix/zabbix-server-pgsql:alpine-3.2.1  
ENV CONSUL_TEMPLATE_VERSION=0.18.1  
ENV
CONSUL_TEMPLATE_SHA256=99dcee0ea187c74d762c5f8f6ceaa3825e1e1d4df6c0b0b5b38f9bcb0c80e5c8  
  
RUN \  
apk add --update-cache curl unzip curl-dev \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& echo 'Include=/usr/local/etc/zabbix_server.conf.d/*.conf' >>
/etc/zabbix/zabbix_server.conf \  
  
&& apk del curl unzip curl-dev && rm -rf /var/cache/apk/*  
  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
ENV DB_ADDR=  
  
COPY consul_template.hcl /etc/consul_template.hcl  
COPY zabbix_server.conf.template /root/zabbix_server.conf.template  
  
ENTRYPOINT [ "consul-template", "-config", "/etc/consul_template.hcl" ]  

