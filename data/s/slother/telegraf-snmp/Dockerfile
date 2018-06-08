FROM telegraf  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export DEBIAN_RELEASE=$(awk -F'[" ]' '/VERSION=/{print $3}' /etc/os-release |
tr -cd '[[:alnum:]]._-' ) && \  
sed -i '/main/d' /etc/apt/sources.list && \  
sed -i '/contrib/d' /etc/apt/sources.list && \  
sed -i '/non-free/d' /etc/apt/sources.list && \  
echo "deb http://httpredir.debian.org/debian ${DEBIAN_RELEASE} main contrib
non-free" >> /etc/apt/sources.list && \  
echo "deb http://httpredir.debian.org/debian ${DEBIAN_RELEASE}-updates main
contrib non-free" >> /etc/apt/sources.list && \  
echo "deb http://security.debian.org ${DEBIAN_RELEASE}/updates main contrib
non-free" >> /etc/apt/sources.list && \  
set -x &&\  
apt-get update && \  
apt-get -y install snmp snmp-mibs-downloader && \  
rm -r /var/lib/apt/lists/*  
  
RUN mkdir -p $HOME/.snmp/mibs  
RUN sed -i '/mibs/d' /etc/snmp/snmp.conf  
RUN echo "mibs +ALL" >> /etc/snmp/snmp.conf  
  
VOLUME $HOME/.snmp/mibs  

