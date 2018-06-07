from deployable/debian-build:8  
# Builds the ndjbdns package  
ENV NDJBDNS_VERSION=1.06  
run set -uex; \  
cd /tmp; \  
curl --progress-bar
http://pjp.dgplug.org/ndjbdns/ndjbdns-${NDJBDNS_VERSION}.tar.gz >
ndjbdns-${NDJBDNS_VERSION}.tar.gz.tmp; \  
mv ndjbdns-${NDJBDNS_VERSION}.tar.gz.tmp ndjbdns-${NDJBDNS_VERSION}.tar.gz; \  
tar -xvzf ndjbdns-${NDJBDNS_VERSION}.tar.gz; \  
cd ndjbdns-${NDJBDNS_VERSION}; \  
./configure --prefix=/ndjbdns; \  
make -j1; \  
make install  
  

