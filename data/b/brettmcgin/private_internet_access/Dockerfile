FROM ubuntu:16.04  
MAINTAINER Brett McGinnis <brettmcgin@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
openvpn \  
wget \  
unzip  
  
ARG VPN_DIR=/etc/openvpn  
  
RUN mkdir -p ${VPN_DIR} && \  
cd ${VPN_DIR}  
  
WORKDIR ${VPN_DIR}  
  
#openvpn.zip  
#openvpn-ip.zip  
#openvpn-ip-lport.zip  
#openvpn-tcp.zip  
#openvpn-ip-tcp.zip  
ARG OPENVPN_CONFIG=openvpn-ip  
  
RUN wget https://www.privateinternetaccess.com/openvpn/${OPENVPN_CONFIG}.zip
&& \  
unzip ${OPENVPN_CONFIG}.zip  
  
COPY openvpn.sh openvpn.sh  
  
ENV REGION='US West'  
ENV USERNAME=''  
ENV PASSWORD=''  
CMD sh openvpn.sh

