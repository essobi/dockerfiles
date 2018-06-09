FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
transmission-remote-cli \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
ENTRYPOINT [ "transmission-remote" ]  

