# SoftEther VPN server  
FROM debian:8  
MAINTAINER Rural Telecom <support@rural-telecom.fr>  
  
ENV VERSION v4.19-9578-beta-2015.09.15  
WORKDIR /usr/local/vpnserver  
  
RUN apt-get update &&\  
apt-get -y -q install gcc make wget iptables && \  
apt-get clean && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \  
wget http://www.softether-
download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Server/64bit_-
_Intel_x64_or_AMD64/softether-vpnserver-${VERSION}-linux-x64-64bit.tar.gz -O
/tmp/softether-vpnserver.tar.gz &&\  
tar -xzvf /tmp/softether-vpnserver.tar.gz -C /usr/local/ &&\  
rm /tmp/softether-vpnserver.tar.gz &&\  
make i_read_and_agree_the_license_agreement &&\  
apt-get purge -y -q --auto-remove gcc make wget  
  
ADD runner.sh /usr/local/vpnserver/runner.sh  
RUN chmod 755 /usr/local/vpnserver/runner.sh  
RUN touch /usr/local/vpnserver/vpn_server.config  
RUN chmod 755 /usr/local/vpnserver/vpn_server.config  
  
EXPOSE 80/tcp 53/tcp 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp 8080/tcp
500/udp 4500/udp  
  
ENTRYPOINT ["/usr/local/vpnserver/runner.sh"]  

