FROM postgres:9.6  
ENV CONSUL_TEMPLATE_VERSION=0.19.3  
ENV
CONSUL_TEMPLATE_SHA256=47b3f134144b3f2c6c1d4c498124af3c4f1a4767986d71edfda694f822eb7680  
  
RUN \  
apt-get update \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
curl \  
unzip \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
cron \  
  
&& rm -rf /etc/cron.daily/* \  
&& rm -rf /etc/cron.hourly/* \  
&& rm -rf /etc/cron.monthly/* \  
&& rm -rf /etc/cron.weekly/* \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& apt-get purge -y --auto-remove \  
curl \  
unzip \  
ca-certificates \  
  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
ENV BACKUP_HOST=  
ENV BACKUP_PATH=  
  
ENV SET_CONTAINER_TIMEZONE=true  
ENV CONTAINER_TIMEZONE=Europe/Moscow  
  
COPY backup.sh /usr/local/bin/backup.sh  
COPY pgpass.template /root/pgpass.template  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

