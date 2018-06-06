FROM qnib/d-consul  
  
ENV CEPH_VERSION=kraken \  
DEBIAN_VERSION=jessie \  
ETCDCTL_VERSION=v0.4.5 \  
ETCDCTL_ARCH=linux-amd64  
  
ENV KVIATOR_VERSION 0.0.7  
ENV CONFD_VERSION 0.11.0  
  
# Install prerequisites  
RUN apt-get update && apt-get install -y wget unzip jq python-pip \  
&& apt-get update \  
&& apt-get install -y wget unzip jq apt-transport-https \  
&& wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add \- \  
&& echo deb https://download.ceph.com/debian-${CEPH_VERSION}/
${DEBIAN_VERSION} main | tee /etc/apt/sources.list.d/ceph-${CEPH_VERSION}.list
\  
&& pip install docopt python-consul  

