FROM fedora:25  
MAINTAINER tgraf@tgraf.ch  
  
RUN \  
dnf -y install curl iproute iputils tcpdump strace ethtool gcc git perf tar &&
\  
curl -LO ftp://ftp.netperf.org/netperf/netperf-2.7.0.tar.gz && \  
tar -xzf netperf-2.7.0.tar.gz && \  
cd netperf-2.7.0 && ./configure --prefix=/usr && make && make install && \  
cd / && \  
rm -rf netperf-2.7.0 netperf-2.7.0.tar.gz && \  
rm -f /usr/share/info/netperf.info && \  
strip -s /usr/bin/netperf /usr/bin/netserver && \  
curl https://raw.githubusercontent.com/borkmann/stuff/master/super_netperf >
/usr/bin/super_netperf && \  
chmod +x /usr/bin/super_netperf && \  
dnf clean all  
  
CMD ["/bin/bash"]  

