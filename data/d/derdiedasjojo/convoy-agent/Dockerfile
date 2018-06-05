FROM ubuntu:15.10  
  
MAINTAINER Rancher Labs, Inc.  
  
RUN apt-get update && apt-get install -y software-properties-common kmod  
RUN add-apt-repository ppa:gluster/glusterfs-3.7 && apt-get update && apt-get
install -y curl glusterfs-client nfs-common  
RUN mkdir -p /var/lib/rancher/convoy-agent && \  
curl -sSL -o convoy.tar.gz
https://github.com/rancher/convoy/releases/download/v0.5.0-rc1/convoy.tar.gz
&& tar -xvzf convoy.tar.gz && mv convoy/convoy /var/lib/rancher/convoy-agent
&& \  
curl -sSL -o share-mnt
https://github.com/rancher/runc/releases/download/share-mnt-v0.1.2/share-mnt
&& chmod u+x share-mnt && mv share-mnt /var/lib/rancher/convoy-agent  
  
ENV PATH /var/lib/rancher/convoy-agent:$PATH  
  
RUN curl -sSL -o convoy-agent.tar.gz https://github.com/rancher/convoy-
agent/releases/download/v0.9.0/convoy-agent.tar.xz && tar -xf convoy-
agent.tar.gz && mv ./convoy-agent /var/lib/rancher/convoy-agent  
COPY convoy /var/lib/rancher/convoy  
COPY share-mnt /var/lib/rancher/convoy-agent  
#COPY convoy-agent /var/lib/rancher/convoy-agent  
COPY launch /  
  
ENTRYPOINT ["/launch"]  

