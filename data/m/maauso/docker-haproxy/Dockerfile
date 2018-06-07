#INSTALL 1/2 CONSUL_TEMPLATE  
FROM debian:jessie as consul-template  
LABEL authors="Miguel Ángel Ausó m.auso.p@gmail.com"  
  
# CONSUL-TEMPLATE OPTIONS  
ENV CONSUL_TEMPLATE_VERSION=0.18.5  
RUN apt-get update && \  
mkdir -p /tmp/consul-template && \  
cd /tmp/consul-template && \  
apt-get -y install wget unzip && \  
wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
# END 1/2  
# INSTALL 2/2 HAPROXY  
FROM debian:jessie  
LABEL description="HaProxy images integrate with Consul using consul template"  
LABEL version="1.7.9"  
  
# COPY CONSUL TEMPLATE  
COPY \--from=consul-template /tmp/consul-template /  
  
# HAPROXY OPTIONS  
ENV HAPROXY_MAXCONN_GLOBAL=50000 HAPROXY_SPREAD_CHECKS=5
HAPROXY_MAX_SPREAD_CHECKS=15000 HAPROXY_SPREAD-CHECKS=5 HAPROXY_RETRIES=3
HAPROXY_BACKLOG=10000 HAPROXY_MAXCONN=10000 HAPROXY_TIMEOUT_CONNECT=3s
HAPROXY_TIMEOUT_CLIENT=30s HAPROXY_TIMEOUT_SERVER=30s
HAPROXY_TIMEOUT_HTTP_KEEP_ALIVE=1s HAPROXY_TIMEOUT_HTTP_REQUEST=15s
HAPROXY_TIMEOUT_QUEUE=30s LOCAL_SYSLOG=127.0.0.1:514  
ENV CONSUL_SERVER=127.0.0.1:8500 TINI_VERSION=v0.14.0  
## HAProxy CONFIGURE  
COPY haproxy.cfg.ctmpl /haproxy.cfg.ctmpl  
  
# runtime dependencies  
RUN apt-get update && apt-get -y upgrade && apt-get install -y --no-install-
recommends \  
iptables \  
openssl \  
procps \  
python3 \  
runit \  
socat \  
ca-certificates  
  
# Build Haproxy  
COPY build-haproxy.sh \  
/haproxy/  
RUN chmod 755 /haproxy/build-haproxy.sh  
  
RUN apt-get update && apt-get install -y --no-install-recommends gcc libc6-dev
libffi-dev libpcre3-dev libreadline-dev libssl-dev zlib1g-dev make wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& /haproxy/build-haproxy.sh \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY *.lua /haproxy/  
  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh \  
&& mkdir -p /var/state/haproxy/ \  
&& mkdir -p /var/run/haproxy/  
  
# Script to star with consul-template and haproxy  
COPY config.conf /config.conf  
  
# All Tini does is spawn a single child (Tini is meant to be run in a
container), and wait for it to exit all the while reaping zombies and
performing signal forwarding.  
RUN apt-get update && apt-get install -y --no-install-recommends gnupg2 wget \  
&& wget --output-document=tini
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini \  
&& wget --output-document=tini.asc
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /tini.asc \  
&& rm -rf /tini.asc \  
&& mv tini /usr/bin/tini \  
&& chmod +x /usr/bin/tini \  
&& tini -- true \  
RUN apt-get purge -y --auto-remove gnupg2 wget  
  
ENTRYPOINT [ "tini", "-g", "--", "/consul-template" ]  
CMD [ "-config=/config.conf" ]  
  
# END 2/2

