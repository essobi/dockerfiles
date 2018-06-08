FROM debian:8  
ENV OC_VERSION=v1.3.0 \  
OC_HASH=3ab7af3d097b57f933eccef684a714f2368804e7  
  
RUN apt update && apt install -y curl && rm -rf /var/apt/lists/*  
  
RUN curl -L
https://github.com/openshift/origin/releases/download/${OC_VERSION}/openshift-
origin-client-tools-${OC_VERSION}-${OC_HASH}-linux-64bit.tar.gz \  
| tar xz && install /openshift-origin-client-
tools-${OC_VERSION}-${OC_HASH}-linux-64bit/oc /usr/bin/oc && rm -rf openshift*  
  
RUN useradd -d /tmp app  
USER app  
  

