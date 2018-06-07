FROM kaktuss/letsencrypt-simp_le-auto:0.19  
ENV CONSUL_TEMPLATE_VERSION=0.18.2  
ENV
CONSUL_TEMPLATE_SHA256=6fee6ab68108298b5c10e01357ea2a8e4821302df1ff9dd70dd9896b5c37217c  
  
RUN \  
apk add --no-cache --virtual .build-deps curl unzip \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& apk del .build-deps  
  
COPY generator.hcl /etc/generator.hcl  
COPY simp_le.conf.template /root/simp_le.conf.template  
COPY simp_le_new.conf.template /root/simp_le_new.conf.template  
COPY store.sh /usr/local/bin/store.sh  
COPY generator /etc/periodic/hourly/generator  
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
ENV CERTS_VAULT_PATH=secret/certificates/  
  
ENTRYPOINT [ "crond", "-f" ]  

