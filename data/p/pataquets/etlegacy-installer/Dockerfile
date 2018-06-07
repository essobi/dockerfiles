FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN \  
curl -o /tmp/install.sh -sSL https://www.etlegacy.com/download/file/86 \  
&& \  
chmod a+x /tmp/install.sh && \  
mkdir -vp /etlegacy/ && \  
/tmp/install.sh --skip-license --prefix=/etlegacy/ && \  
rm -v /tmp/install.sh  

