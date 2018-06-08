FROM pataquets/ubuntu:xenial  
  
RUN \  
echo "deb http://ppa.launchpad.net/retroshare/stable/ubuntu xenial main" \  
| tee /etc/apt/sources.list.d/retroshare.list && \  
DEBIAN_FRONTEND=noniteractive \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
144729B5  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install retroshare \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "retroshare-nogui", "--stderr", "--ip-address", "0.0.0.0" ]  

