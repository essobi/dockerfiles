FROM ubuntu:16.04  
MAINTAINER i.karpovich@currencysolutions.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget nfs-common  
RUN wget https://github.com/ContainX/docker-volume-
netshare/releases/download/v0.32/docker-volume-netshare_0.32_amd64.deb \  
&& dpkg -i docker-volume-netshare_0.32_amd64.deb  
  
ENTRYPOINT ["/usr/bin/docker-volume-netshare", "efs"]  

