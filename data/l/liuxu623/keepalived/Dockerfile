FROM alpine:3.6  
  
# Keepalived version  
ARG KEEPALIVED_VERSION=1.3.9  
  
# Download, build and install Keepalived  
RUN apk --no-cache add \  
curl \  
gcc \  
ipset \  
ipset-dev \  
iptables \  
iptables-dev \  
libnfnetlink \  
libnfnetlink-dev \  
libnl3 \  
libnl3-dev \  
make \  
musl-dev \  
openssl \  
openssl-dev \  
&& curl -o keepalived.tar.gz -SL
http://keepalived.org/software/keepalived-${KEEPALIVED_VERSION}.tar.gz \  
&& mkdir /keepalived-sources \  
&& tar -xzf keepalived.tar.gz --strip 1 -C /keepalived-sources \  
&& cd /keepalived-sources \  
&& ./configure --disable-dynamic-linking \  
&& make && make install \  
&& cd - && mkdir -p /etc/keepalived \  
&& rm -f keepalived.tar.gz \  
&& rm -rf /keepalived-sources \  
&& apk --no-cache del \  
curl \  
gcc \  
ipset-dev \  
iptables-dev \  
libnfnetlink-dev \  
libnl3-dev \  
make \  
musl-dev \  
openssl-dev  

