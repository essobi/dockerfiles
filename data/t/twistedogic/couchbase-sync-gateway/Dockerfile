FROM google/debian:wheezy  
MAINTAINER Jordan Li  
ENV SYNC_GATEWAY_VERSION 1.0.3  
RUN export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y wget && \  
wget -q http://packages.couchbase.com/releases/couchbase-sync-
gateway/${SYNC_GATEWAY_VERSION}/couchbase-sync-gateway-
enterprise_${SYNC_GATEWAY_VERSION}_x86_64.deb -O package.deb && \  
dpkg -i package.deb && \  
rm package.deb  
  
# Add configurations  
ENV PATH /opt/couchbase-sync-gateway/bin:$PATH  
##################### INSTALLATION END #####################  
  
# Documentation http://developer.couchbase.com/mobile/develop/guides/sync-
gateway/index.html  
EXPOSE 4984 4985  

