FROM alpine:3.5  
ENV CONSUL_TEMPLATE_VERSION=0.18.2  
ENV
CONSUL_TEMPLATE_SHA256=6fee6ab68108298b5c10e01357ea2a8e4821302df1ff9dd70dd9896b5c37217c  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
curl unzip \  
  
&& apk add \--no-cache dkimproxy \  
  
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
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
COPY dkimproxy.hcl /etc/dkimproxy.hcl  
COPY store.sh /usr/local/bin/store.sh  
COPY dkimproxy.map.template /root/dkimproxy.map.template  
COPY start_dkimproxy.sh.template /root/start_dkimproxy.sh.template  
COPY start_template.sh /usr/local/bin/start_template.sh  
  
CMD ["/usr/local/bin/start_template.sh"]  

