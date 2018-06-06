FROM ubuntu:xenial  
  
ENV NODENAME=default \  
MODE=none \  
INTERFACE=none \  
ADDRESS_FAMILY=none \  
CONNECT_TO=none \  
DEVICE=none \  
DEVICE_TYPE=none \  
HOSTNAMES=none \  
KEY_EXPIRE=none \  
MAC_EXPIRE=none \  
MAX_TIMEOUT=none \  
PING_INTERVAL=none \  
PING_TIMEOUT=none  
ENV ADDRESS=none \  
CIPHER=none \  
CLAMP_MSS=none \  
COMPRESSION=none \  
DIGEST=none \  
INDIRECT_DATA=none \  
MAC_LENGTH=none \  
PMTU=none \  
PMTU_DISCOVERY=none \  
SUBNET=none \  
PORT=none  
  
ENV VPN_IP=none \  
SSH_PASS=none  
  
RUN apt-get update && \  
apt-get install -y net-tools tinc cron sshpass && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD config/run.sh /etc/run.sh  
ADD config/tinc-* /etc/default/  
RUN chmod +x /etc/run.sh && \  
mkdir -p /etc/tinc/hosts && \  
mkdir -p /usr/tinc-cron/scripts  
  
EXPOSE 655/tcp 655/udp  
  
VOLUME /etc/tinc /usr/cron  
  
CMD /etc/run.sh

