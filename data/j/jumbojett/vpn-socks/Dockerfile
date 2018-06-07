FROM debian:buster-slim  
LABEL maintainer="mjett@mitre.org"  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update && apt-get -y install openconnect git build-essential
libevent-dev autoconf automake && \  
mkdir -p /vpn && cd /vpn && \  
git clone https://github.com/cernekee/ocproxy.git && cd ocproxy && \  
./autogen.sh && \  
./configure && \  
make && \  
# Build done  
# Cleanup  
apt-get purge --auto-remove -y git build-essential autoconf automake && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /vpn/ocproxy  
EXPOSE 1080  
ENTRYPOINT ["/usr/sbin/openconnect", "-m", "1290", "--script-tun", "--script",
"./ocproxy -D 1080 -g -k 5"]  

