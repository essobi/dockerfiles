FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
DBB231E7B333BDB6F6CCA46BD56E6F37B99D3486 && \  
. /etc/lsb-release && \  
echo "deb http://ppa.launchpad.net/gridcoin/gridcoin-stable/ubuntu
${DISTRIB_CODENAME} main" \  
| tee -a /etc/apt/sources.list.d/gridcoin.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
gridcoinresearchd \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
ENTRYPOINT [ "gridcoinresearchd" ]  

