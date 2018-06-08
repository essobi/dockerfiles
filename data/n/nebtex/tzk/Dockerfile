FROM debian:experimental  
MAINTAINER Cristian Lozano "criloz@nebtex.com"  
# This is the release of Consul to pull in.  
ENV CONSUL_VERSION=0.7.2  
# This is the release of tzk-daemon to pull in.  
ENV TZKD_VERSION=0.2.0  
# This is the release of https://github.com/hashicorp/docker-base to pull in
order  
# to provide HashiCorp-built versions of basic utilities like dumb-init and
gosu.  
ENV DOCKER_BASE_VERSION=0.0.4  
# Create a consul user and group first so the IDs get set the same way, even
as  
# the rest of this may change over time.  
RUN useradd -ms /bin/bash consul  
  
RUN apt-get update -y  
# Set up Consul.  
RUN apt-get install -y libpcap-dev libcap2-bin ca-certificates unzip curl wget
&& \  
wget
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
unzip -d /bin consul_${CONSUL_VERSION}_linux_amd64.zip  
  
# Install Tinc and utility packages  
RUN echo "deb http://http.debian.net/debian experimental main" >>
/etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools supervisor curl &&
\  
DEBIAN_FRONTEND=noninteractive apt-get install -y -t experimental tinc  
  
# The /consul/data dir is used by Consul to store state. The agent will be
started  
# with /consul/config as the configuration directory so you can add additional  
# config files in that location.  
RUN mkdir -p /consul/data && \  
mkdir -p /consul/config && \  
chown -R consul:consul /consul  
  
# Remove SUID programs  
RUN for i in `find / -perm +6000 -type f 2>/dev/null`; do chmod a-s $i; done  
  
# installing unzip sigil  
RUN apt-get install liblzo2-2 -y && \  
curl -fsSL
https://github.com/gliderlabs/sigil/releases/download/v0.4.0/sigil_0.4.0_Linux_x86_64.tgz
| tar -zxC /usr/local/bin  
  
# install caddy https proxy for consul  
# Installing caddy proxy ...  
RUN curl -LO
https://github.com/mholt/caddy/releases/download/v0.9.3/caddy_linux_amd64.tar.gz
&& \  
mkdir -p caddy && \  
tar -xvf caddy_linux_amd64.tar.gz -C caddy && \  
cd caddy && \  
cp caddy_linux_amd64 /usr/local/bin/caddy && \  
chown root:root /usr/local/bin/caddy && \  
chmod 755 /usr/local/bin/caddy && \  
setcap 'cap_net_bind_service=+ep' /usr/local/bin/caddy &&\  
mkdir /etc/caddy &&\  
chown -R root:www-data /etc/caddy &&\  
mkdir /etc/ssl/caddy &&\  
chown -R www-data:root /etc/ssl/caddy &&\  
chmod 0770 /etc/ssl/caddy &&\  
mkdir /var/www &&\  
chown www-data:www-data /var/www &&\  
chmod 555 /var/www  
  
# install tzk daemon  
RUN wget https://github.com/NebTex/tzk-
daemon/releases/download/v${TZKD_VERSION}/tzkd_linux_amd64 && \  
cp tzkd_linux_amd64 /usr/local/bin/tzkd && \  
chmod +x /usr/local/bin/tzkd && \  
mkdir -p /etc/tzk.d  
  
ADD templates/ /templates  
  
EXPOSE 655/tcp 655/udp  
EXPOSE 80  
EXPOSE 443  
# The /consul/data dir is used by Consul to store state. The agent will be
started  
# with /consul/config as the configuration directory so you can add additional  
# config files in that location.  
RUN mkdir -p /consul/data && \  
mkdir -p /consul/config && \  
chown -R consul:consul /consul  
  
# Expose the consul data directory as a volume since there's mutable state in
there.  
VOLUME /consul/data  
VOLUME /etc/tinc  
  
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
  
ADD entrypoint.sh /bin/entrypoint.sh  
RUN chmod +x /bin/entrypoint.sh  
  
ENTRYPOINT [ "/bin/entrypoint.sh" ]  

