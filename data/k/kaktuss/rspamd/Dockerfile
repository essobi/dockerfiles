FROM alpine:3.7  
ENV \  
CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0
\  
\  
USER_UID=1000 \  
USER_GID=1000 \  
\  
RSPAMD_SERVICE= \  
\  
CONSUL_HTTP_ADDR= \  
CONSUL_TOKEN= \  
VAULT_ADDR= \  
VAULT_TOKEN=  
  
RUN \  
apk add --no-cache \  
ca-certificates \  
postgresql-client \  
rspamd-client \  
rspamd-controller \  
rspamd \  
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
  
COPY rspamd_start.sh /usr/local/bin/rspamd_start.sh  
COPY templates /root/templates  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
EXPOSE 11333 11334  
CMD ["/usr/local/bin/entrypoint.sh"]  

