FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV VERSION v4.21-9613-beta-2016.04.24  
RUN apt-get update && \  
apt-get -y -q install gcc make curl dnsmasq supervisor && \  
curl -L http://www.softether-
download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Server/64bit_-
_Intel_x64_or_AMD64/softether-vpnserver-${VERSION}-linux-x64-64bit.tar.gz | \  
tar -xzv -C /opt  
  
WORKDIR /opt/vpnserver  
  
RUN make i_read_and_agree_the_license_agreement && \  
apt-get purge -y -q --auto-remove gcc make && \  
apt-get clean && \  
rm -fr /var/lib/apt  
  
ADD resources/bin/ /usr/local/bin/  
ADD resources/etc/ /etc/  
  
RUN chmod +x /usr/local/bin/*  
  
VOLUME ["/opt/vpnserver/vpnserver_config"]  
  
EXPOSE 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp  
  
CMD ["/usr/local/bin/run"]  

