FROM nginx:1.12.2-alpine  
  
ENV \  
CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0
\  
\  
CONSUL_HTTP_ADDR= \  
CONSUL_TOKEN= \  
VAULT_ADDR= \  
VAULT_TOKEN= \  
\  
SET_CONTAINER_TIMEZONE=true \  
CONTAINER_TIMEZONE=Europe/Moscow \  
\  
VAULT_PATH=secret/certificates \  
NGINX_WORKER_CONNECTIONS=1024  
RUN \  
rm /etc/nginx/conf.d/default.conf \  
&& mkdir -p /etc/nginx/certificates \  
&& mkdir -p /var/lib/nginx/cache \  
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
&& ( ( crontab -l ; echo '*/5 * * * * /usr/local/bin/resolve.sh' ) | crontab -
) \  
\  
&& apk del .build-deps  
  
COPY store.sh /usr/local/bin/store.sh  
COPY resolve.sh /usr/local/bin/resolve.sh  
COPY start.sh /usr/local/bin/start.sh  
COPY templates /root/templates  
  
CMD ["/usr/local/bin/start.sh"]  

