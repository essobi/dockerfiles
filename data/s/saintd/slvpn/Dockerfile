FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install wget net-tools  
RUN wget -O /tmp/ArrayNetworksL3VPN_LINUX.zip
speedtest.dal05.softlayer.com/array/ArrayNetworksL3VPN_LINUX.zip  
RUN mkdir /root/ArrayNetworksL3VPN && mv /tmp/ArrayNetworksL3VPN_LINUX.zip
/root/ArrayNetworksL3VPN  
WORKDIR /root/ArrayNetworksL3VPN  
RUN sed -e '1,/BIGIN SELFEXTR/d' ArrayNetworksL3VPN_LINUX.zip |sed -e
'1,/BIGIN SELFEXTR/d' > ./test.tar.gz  
#RUN sed -e '1,/#BIGIN SELFEXTR/d' ArrayNetworksL3VPN_LINUX.zip >
./test.tar.gz  
RUN tar zxvf test.tar.gz  
RUN chown root array_vpnc array_loader array_vpnc64 array_loader64  
RUN chmod 4755 array_vpnc array_loader array_vpnc64 array_loader64  
RUN rm -f ArrayNetworksL3VPN_LINUX.zip test.tar.gz  
WORKDIR /root  
RUN mv ArrayNetworksL3VPN /usr/local/array_vpn  
ADD run.sh /run.sh  
CMD ["sh", "/run.sh"]  
  
# E.g.: docker run --name=slvpn --net=host --privileged -d -e
VPN_HOST="vpn.ams03.softlayer.com" -e VPN_PORT="443" -e VPN_USER="MyVPNUser"
-e VPN_PASS="MyVPNPass" saintd/slvpn  
# You can now ssh to your SL's hosts through the private VLAN! :)  

