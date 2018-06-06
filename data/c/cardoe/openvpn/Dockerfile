# Original credit: https://github.com/jpetazzo/dockvpn  
# Forked from improvements by: https://github.com/kylemanna/docker-openvpn  
# Leaner build than Ubuntu  
FROM debian:jessie  
  
MAINTAINER Doug Goldstein <cardoe@cardoe.com>  
  
# Building a container we won't have an interactive prompt to debconf  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install OpenVPN, iptables and curl while cleaning up any storage used  
# Done as one big command to keep the image leaner  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install openvpn iptables curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
# Install easyrsa 3.0.0-rc2 (switch to release when available)  
RUN cd /usr/local/share/ && \  
curl -sSL https://github.com/OpenVPN/easy-
rsa/releases/download/v3.0.0-rc2/EasyRSA-3.0.0-rc2.tgz | tar -zx && \  
mv EasyRSA-3.0.0-rc2 easyrsa && \  
ln -s /usr/local/share/easyrsa/easyrsa /usr/local/bin  
  
# Needed by scripts  
ENV OPENVPN /etc/openvpn  
ENV EASYRSA /usr/local/share/easyrsa  
ENV EASYRSA_PKI $OPENVPN/pki  
ENV EASYRSA_VARS_FILE $OPENVPN/vars  
  
VOLUME ["/etc/openvpn"]  
  
# Internally uses port 1194, remap using docker  
EXPOSE 1194/udp  
  
WORKDIR /etc/openvpn  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
ENTRYPOINT ["/usr/local/bin/ovpn_main"]  
CMD []  

