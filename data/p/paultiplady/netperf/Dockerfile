FROM ubuntu:14.04  
MAINTAINER paultiplady@gmail.com  
  
# Satisfy deps  
RUN apt-get update && \  
apt-get install -y gcc make curl && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
# Download netperf  
RUN curl -LO ftp://ftp.netperf.org/netperf/netperf-2.7.0.tar.gz && tar -xzf
netperf-2.7.0.tar.gz  
RUN cd netperf-2.7.0 && ./configure && make && make install  
  
CMD ["/usr/local/bin/netserver", "-D"]  
  

