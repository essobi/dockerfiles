FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install --no-install-recommends \  
tcpd \  
xinetd \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
# Switch from 'connections per second' rate limiting, since it disables the  
# service completely (potential DoS) to 'maximum instances of service per  
# source IP address' limit. The limit is the same default as for 'cps' (50).  
RUN \  
sed -i 's/^}$/cps = 0 0\nper_source = 50\n}/' /etc/xinetd.conf && \  
grep "cps = 0" /etc/xinetd.conf && \  
grep "per_source = 50" /etc/xinetd.conf && \  
nl /etc/xinetd.conf  
  
ENTRYPOINT [ "xinetd", "-dontfork" ]  

