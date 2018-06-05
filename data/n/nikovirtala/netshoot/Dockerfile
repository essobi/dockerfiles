FROM alpine:edge  
  
RUN set -ex \  
&& apk update \  
&& apk add --no-cache \  
tcpdump \  
bridge-utils \  
netcat-openbsd \  
util-linux \  
iptables \  
iputils \  
iproute2 \  
iftop \  
drill \  
apache2-utils \  
strace \  
curl \  
ethtool \  
ipvsadm \  
ngrep \  
iperf \  
nmap \  
conntrack-tools \  
bind-utils  
  
ADD netgen.sh /usr/local/bin/netgen  
  
CMD ["sh"]  

