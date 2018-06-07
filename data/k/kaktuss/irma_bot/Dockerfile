FROM debian:9  
  
ENV \  
CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0
\  
\  
SET_CONTAINER_TIMEZONE=true \  
CONTAINER_TIMEZONE=Europe/Moscow \  
\  
USER_UID=1000 \  
USER_GID=1000 \  
\  
CONSUL_HTTP_ADDR= \  
CONSUL_TOKEN= \  
VAULT_ADDR= \  
VAULT_TOKEN= \  
\  
IRMA_NOTIFY_URL= \  
IRMA_MODE=development \  
IRMA_BOT_NAME=irma_bot \  
IRMA_DB= \  
IRMA_DB_PORT= \  
REDIS_ADDR= \  
REDIS_PORT=  
  
  
RUN \  
apt-get update \  
\  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
build-essential \  
cpanminus \  
curl \  
git \  
libextutils-makemaker-cpanfile-perl \  
unzip \  
\  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
libanyevent-perl \  
libclass-xsaccessor-perl \  
libcpanel-json-xs-perl \  
libdbd-pg-perl \  
libev-perl \  
libhash-merge-perl \  
libio-socket-ssl-perl \  
libmodule-build-tiny-perl \  
libmoo-perl \  
libparams-validate-perl \  
libpq5 \  
libsql-abstract-perl \  
libtest-compile-perl \  
libtest-fatal-perl \  
libtest-tcp-perl \  
libtext-trim-perl \  
liburi-perl \  
libyaml-libyaml-perl \  
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
## Latest YAML::XS needs to latest JSON::Validator  
&& cpanm YAML::XS \  
\  
&& cpanm https://github.com/kak-tus/irma_bot.git@0.11 \  
\  
&& apt-get purge -y --auto-remove \  
build-essential \  
cpanminus \  
curl \  
git \  
libextutils-makemaker-cpanfile-perl \  
libpq-dev \  
unzip \  
\  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 9000  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY templates /root/templates  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

