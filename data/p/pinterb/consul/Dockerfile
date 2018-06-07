FROM pinterb/base:alpine  
MAINTAINER Brad Pinter "brad.pinter@gmail.com"  
# This is the release of Consul to pull in.  
ENV CONSUL_VERSION 0.6.4  
ENV CONSUL_SHA256
abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627  
ENV GLIBC_PKG_VERSION 2.23-r3  
ENV DUMB_INIT_VERSION 1.1.3  
## Create a consul user and group first so the IDs get set the same way, even
as  
## the rest of this may change over time.  
#RUN addgroup consul && \  
# adduser -S -G consul consul  
RUN apk --update add --no-cache ca-certificates && \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub "https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/${GLIBC_PKG_VERSION}/sgerrand.rsa.pub" && \  
curl -Lo glibc-${GLIBC_PKG_VERSION}.apk "https://github.com/sgerrand/alpine-
pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-${GLIBC_PKG_VERSION}.apk"
&& \  
curl -Lo glibc-bin-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-
bin-${GLIBC_PKG_VERSION}.apk" && \  
curl -Lo glibc-i18n-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-i18n-${GLIBC_PKG_VERSION}.apk"
&& \  
apk add glibc-${GLIBC_PKG_VERSION}.apk glibc-bin-${GLIBC_PKG_VERSION}.apk
glibc-i18n-${GLIBC_PKG_VERSION}.apk && \  
rm -rf /var/cache/apk/*  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
/tmp/consul.zip  
RUN echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& cd /bin \  
&& unzip /tmp/consul.zip \  
&& chmod +x /bin/consul \  
&& rm /tmp/consul.zip  
  
RUN curl -Lo /usr/local/bin/dumb-init "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64"  
RUN chmod +x /usr/local/bin/dumb-init  
  
## The /consul/data dir is used by Consul to store state. The agent will be
started  
## with /consul/config as the configuration directory so you can add
additional  
## config files in that location.  
RUN mkdir -p /consul/data && \  
mkdir -p /consul/config  
# mkdir -p /consul/config && \  
# chown -R consul:consul /consul  
# Expose the consul data directory as a volume since there's mutable state in
there.  
VOLUME [ "/consul/data", "/consul/config" ]  
  
# Server RPC is used for communication between Consul clients and servers for
internal  
# request forwarding.  
EXPOSE 8300  
# Serf LAN and WAN (WAN is used only by Consul servers) are used for gossip
between  
# Consul agents. LAN is within the datacenter and WAN is between just the
Consul  
# servers in all datacenters.  
EXPOSE 8301 8301/udp 8302 8302/udp  
  
# CLI, HTTP, and DNS (both TCP and UDP) are the primary interfaces that
applications  
# use to interact with Consul.  
EXPOSE 8400 8500 8600 8600/udp  
  
ENTRYPOINT ["/bin/consul"]  
CMD ["--help"]  

