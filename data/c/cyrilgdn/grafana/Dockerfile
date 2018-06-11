FROM grafana/grafana:4.6.3  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
wget \  
unzip \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dumb-init  
ENV DUMB_INIT_VERSION=1.2.1 \  
DUMB_INIT_SHA256=057ecd4ac1d3c3be31f82fc0848bf77b1326a975b4f8423fe31607205a0fe945  
  
RUN wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 \  
&& echo "${DUMB_INIT_SHA256} /usr/local/bin/dumb-init" | sha256sum -c - \  
&& chmod +x /usr/local/bin/dumb-init  
  
# Install consul-template  
ENV CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0  
  
RUN wget -q -O /tmp/consul-template.zip https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo "${CONSUL_TEMPLATE_SHA256} /tmp/consul-template.zip" | sha256sum -c -
\  
&& gunzip -c /tmp/consul-template.zip > /usr/local/bin/consul-template \  
&& chmod +x /usr/local/bin/consul-template \  
&& rm /tmp/consul-template.zip  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["consul-template", "-config=/srv/consul-template.cfg"]  
  
EXPOSE 3000  
# Install the plugins in a non-standard place, since /var/lib/grafana is going  
# to be overwritten at runtime due to being a Docker VOLUME.  
ENV GF_PATHS_PLUGINS=/srv/grafana/plugins  
RUN mkdir --parents ${GF_PATHS_PLUGINS} && chown grafana:grafana
${GF_PATHS_PLUGINS} && \  
gosu grafana grafana-cli --pluginsDir "${GF_PATHS_PLUGINS}" plugins install
grafana-piechart-panel 1.2.0 && \  
gosu grafana grafana-cli --pluginsDir "${GF_PATHS_PLUGINS}" plugins install
natel-discrete-panel 0.0.6  

