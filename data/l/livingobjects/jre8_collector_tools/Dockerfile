FROM livingobjects/jre8:8u121_4  
  
# Update dependency  
RUN apt-get -y update && apt-get install -y --no-install-recommends \  
tcpdump \  
snmp && \  
apt-get autoclean && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
  
addgroup pcap && \  
addgroup lo-daemon pcap && \  
addgroup root pcap && \  
chgrp pcap /usr/sbin/tcpdump && \  
chmod 750 /usr/sbin/tcpdump && \  
# setcap not possible on docker hub, it appears that they are using aufs as
storage backend  
# setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump && \  
ln -s /usr/sbin/tcpdump /usr/local/bin/tcpdump && \  
# Add sudo without password for docker with AUFS  
echo 'lo-daemon ALL=(ALL) NOPASSWD: /usr/sbin/tcpdump' >> /etc/sudoers && \  
visudo -c -x /etc/sudoers  
  

