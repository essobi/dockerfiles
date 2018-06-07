# clusterhq-flocker-cli Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Hugh Cannon <hugh@hughcannon.com>  
  
RUN apt-get update && \  
apt-get -y install apt-transport-https software-properties-common  
RUN add-apt-repository -y "deb https://clusterhq-
archive.s3.amazonaws.com/ubuntu/$(lsb_release --release --short)/\$(ARCH) /"
&& \  
apt-get update && \  
apt-get -y --force-yes install clusterhq-flocker-cli  
  
VOLUME /flockercerts  
WORKDIR /flockercerts  
  
ENTRYPOINT ["flocker-ca"]  

