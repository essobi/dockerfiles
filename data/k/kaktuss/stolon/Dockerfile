FROM postgres:10.2  
  
ENV \  
STOLON_VERSION=0.9.0 \  
STOLON_SHA256=e31ece535a8a6343fc66a5612b62389da87ba266f705ac6a8d32c746a4d3cdfa
\  
\  
STOLON_SERVICE=\  
ETCD_HTTP_ADDR= \  
PG_REPL_USERNAME= \  
PG_REPL_PASSWORD= \  
PG_SU_PASSWORD= \  
EXT_HOSTNAME= \  
STOLON_CLUSTER_NAME= \  
STOLON_IP= \  
\  
SET_CONTAINER_TIMEZONE=true \  
CONTAINER_TIMEZONE=Europe/Moscow \  
\  
LANG=ru_RU.UTF-8  
  
RUN \  
apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
curl \  
\  
&& cd /usr/local/bin \  
&& curl -L
https://github.com/sorintlab/stolon/releases/download/v${STOLON_VERSION}/stolon-v${STOLON_VERSION}-linux-
amd64.tar.gz -o stolon-v${STOLON_VERSION}-linux-amd64.tar.gz \  
&& echo -n "$STOLON_SHA256 stolon-v${STOLON_VERSION}-linux-amd64.tar.gz" |
sha256sum -c - \  
&& tar -zxvf stolon-v${STOLON_VERSION}-linux-amd64.tar.gz \  
\  
&& cp ./stolon-v${STOLON_VERSION}-linux-amd64/bin/stolon-keeper ./ \  
&& cp ./stolon-v${STOLON_VERSION}-linux-amd64/bin/stolon-proxy ./ \  
&& cp ./stolon-v${STOLON_VERSION}-linux-amd64/bin/stolon-sentinel ./ \  
&& cp ./stolon-v${STOLON_VERSION}-linux-amd64/bin/stolonctl ./ \  
\  
&& rm -rf ./stolon-v${STOLON_VERSION}-linux-amd64 \  
&& rm stolon-v${STOLON_VERSION}-linux-amd64.tar.gz \  
\  
&& localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias
ru_RU.UTF-8 \  
\  
&& apt-get purge -y --auto-remove \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY stolon-entrypoint.sh /usr/local/bin/stolon-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/stolon-entrypoint.sh"]  

