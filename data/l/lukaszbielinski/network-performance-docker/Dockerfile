FROM oberthur/docker-ubuntu:16.04  
MAINTAINER Lukasz Bielinski <l.bielinski@oberthur.com>  
  
# Prepare image  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install apache2-utils iperf3 curl gcc make libgeoip-dev libc6-dev
bind9utils libbind-dev libkrb5-dev libssl-dev libcap-dev libxml2-dev \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN curl -LO ftp://ftp.netperf.org/netperf/netperf-2.7.0.tar.gz && tar -xzf
netperf-2.7.0.tar.gz  
RUN cd netperf-2.7.0 && ./configure --prefix=/usr && make && make install  
  
RUN curl ftp://ftp.nominum.com/pub/nominum/dnsperf/2.1.0.0/dnsperf-
src-2.1.0.0-1.tar.gz -O && tar xfvz dnsperf-src-2.1.0.0-1.tar.gz  
RUN cd dnsperf-src-2.1.0.0-1 && ./configure --prefix=/usr && make && make
install  
  
COPY dnsperf /queries  
  
ENTRYPOINT ["iperf3"]  

