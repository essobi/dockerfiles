FROM debian  
MAINTAINER (https://www.danieldent.com/)  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget build-essential
bind9utils libbind-dev libkrb5-dev libssl-dev libcap-dev libxml2-dev dnsutils
&& \  
wget ftp://ftp.nominum.com/pub/nominum/dnsperf/2.0.0.0/dnsperf-
src-2.0.0.0-1.tar.gz && \  
echo "23d486493f04554d11fca97552e860028f18c5ed6e35348e480a7448fa8cfaad
dnsperf-src-2.0.0.0-1.tar.gz" | sha256sum -c && \  
tar -xvvzf dnsperf-src-2.0.0.0-1.tar.gz && \  
cd dnsperf-src-2.0.0.0-1 && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -Rf dnsperf-src-2.0.0.0-1 dnsperf-src-2.0.0.0-1.tar.gz && \  
apt-get autoremove -y build-essential && \  
rm -Rf /var/lib/apt /var/cache/apt  

