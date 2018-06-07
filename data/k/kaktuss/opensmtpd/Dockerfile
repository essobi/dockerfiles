FROM alpine:3.7  
ENV \  
CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0
\  
\  
CONSUL_HTTP_ADDR= \  
CONSUL_TOKEN= \  
VAULT_ADDR= \  
VAULT_TOKEN=  
  
RUN \  
apk add --no-cache \  
ca-certificates \  
expect \  
opensmtpd \  
postgresql-client \  
rspamd-client \  
\  
&& apk add --no-cache --virtual .build-deps \  
curl \  
unzip \  
\  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
\  
&& apk del .build-deps  
  
COPY templates /root/templates  
COPY nc.expect /usr/local/bin/nc.expect  
  
CMD ["/usr/local/bin/consul-template", "-config",
"/root/templates/service.hcl"]  

