FROM ubuntu:17.10  
  
RUN export NDPPD_VERSION=0.2.5 \  
&& apt-get update \  
&& apt-get install \--no-install-recommends -qy g++ make wget ca-certificates
&& \  
# Fetch source code from GitHub  
wget -q -O - "$@"
https://github.com/DanielAdolfsson/ndppd/archive/${NDPPD_VERSION}.tar.gz | tar
-xzC /usr/src && \  
cd /usr/src/ndppd-${NDPPD_VERSION} && \  
# Build and install into /usr/local/sbin/ directory  
make && make install && \  
cd / && \  
# Remove old packages  
apt-get purge -qy g++ make wget ca-certificates && apt-get -qy autoremove && \  
# Delete source directories  
rm -rf /usr/src/ndppd-${NDPPD_VERSION} && \  
# Delete package caches  
rm -rf /var/lib/apt /var/lib/dpkg /var/log  
  
# Add configuration bootstrapper  
ADD init.sh /init.sh  
  
CMD ["/bin/sh", "/init.sh"]  

