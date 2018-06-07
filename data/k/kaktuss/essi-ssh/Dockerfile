FROM kaktuss/essi:0.31  
ENV CONSUL_TEMPLATE_VERSION=0.18.2  
ENV
CONSUL_TEMPLATE_SHA256=6fee6ab68108298b5c10e01357ea2a8e4821302df1ff9dd70dd9896b5c37217c  
  
RUN \  
apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
curl unzip \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
COPY config.template /root/config.template  
COPY start.sh /usr/local/bin/start.sh  
COPY store.sh /usr/local/bin/store.sh  
COPY essi.hcl /etc/essi.hcl  
COPY init_hosts.sh.template /root/init_hosts.sh.template  
  
CMD ["/usr/local/bin/consul-template", "-config", "/etc/essi.hcl"]  

