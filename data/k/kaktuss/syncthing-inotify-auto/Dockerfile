FROM debian:9  
ENV CONSUL_TEMPLATE_VERSION=0.18.5  
ENV
CONSUL_TEMPLATE_SHA256=b0cd6e821d6150c9a0166681072c12e906ed549ef4588f73ed58c9d834295cd2  
  
ENV SYNCTHING_INOTIFY_VERSION=0.8.7  
ENV
SYNCTHING_INOTIFY_SHA256=2d433132e6792780248494eea509cc9b34a9af127a1a8a3120be6e73bca3a406  
  
USER root  
  
RUN \  
apt-get update \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
curl \  
unzip \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
gosu \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& cd /usr/local/bin \  
&& curl -L https://github.com/syncthing/syncthing-
inotify/releases/download/v${SYNCTHING_INOTIFY_VERSION}/syncthing-inotify-
linux-amd64-v${SYNCTHING_INOTIFY_VERSION}.tar.gz -o "syncthing-inotify-linux-
amd64-v${SYNCTHING_INOTIFY_VERSION}.tar.gz" \  
&& echo -n "$SYNCTHING_INOTIFY_SHA256 syncthing-inotify-linux-
amd64-v${SYNCTHING_INOTIFY_VERSION}.tar.gz" | sha256sum -c - \  
&& tar -xvzf "syncthing-inotify-linux-
amd64-v${SYNCTHING_INOTIFY_VERSION}.tar.gz" syncthing-inotify \  
&& rm "syncthing-inotify-linux-amd64-v${SYNCTHING_INOTIFY_VERSION}.tar.gz" \  
  
&& apt-get purge -y --auto-remove \  
ca-certificates \  
curl \  
unzip \  
  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY syncthing.hcl /etc/syncthing.hcl  
COPY config.xml.template /home/user/config.xml.template  
COPY start.sh.template /home/user/start.sh.template  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
  
ENV SYNC_SERVICE=  
ENV SYNC_IGNORE_DELETE=  
ENV SYNC_IP=  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

