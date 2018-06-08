FROM ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
munin-node && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN \  
sed -ri 's/^log_file.*/# \0/; \  
s/^pid_file.*/# \0/; \  
s/^background 1$/background 0/; \  
s/^setsid 1$/setsid 0/; \  
' /etc/munin/munin-node.conf && \  
/bin/echo -e "cidr_allow 192.168.0.0/16\ncidr_allow 172.16.0.0/12\ncidr_allow
10.0.0.0/8" >> /etc/munin/munin-node.conf  
  
CMD ["/bin/sh", "-c", "munin-node-configure --remove --shell | sh; exec
/usr/sbin/munin-node --config /etc/munin/munin-node.conf"]  

