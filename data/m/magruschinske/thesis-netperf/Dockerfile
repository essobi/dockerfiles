FROM debian:jessie  
MAINTAINER mathias.gruschinske@gmail.com  
  
RUN apt-get update && \  
apt-get install -y gcc make curl && \  
apt-get clean  
  
RUN mkdir -p /var/local/apps  
RUN cd /var/local/apps && curl -LO
ftp://ftp.netperf.org/netperf/netperf-2.7.0.tar.gz && tar -xzf
netperf-2.7.0.tar.gz  
RUN cd /var/local/apps/netperf-2.7.0 && ./configure && make && make install  
  
# EXPOSE 5000  
# CMD ["/usr/local/bin/netserver", "-D", "-p", "5000"]  

