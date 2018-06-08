FROM ubuntu:16.04  
MAINTAINER Mitz Amano <mitz@linux.com>  
  
ENV VERSION v4.22-9634-beta-2016.11.27  
WORKDIR /usr/local/vpnclient  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y -q install iptables gcc make wget dhcpcd5 iproute2 && \  
apt-get clean && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \  
wget http://www.softether-
download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Client/64bit_-
_Intel_x64_or_AMD64/softether-vpnclient-${VERSION}-linux-x64-64bit.tar.gz -O
/tmp/softether-vpnclient.tar.gz &&\  
tar -xzvf /tmp/softether-vpnclient.tar.gz -C /usr/local/ && \  
rm /tmp/softether-vpnclient.tar.gz && \  
make i_read_and_agree_the_license_agreement && \  
apt-get purge -y -q --auto-remove gcc make wget  
  
ADD entrypoint.sh /  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

