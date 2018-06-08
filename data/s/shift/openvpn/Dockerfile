# Original credits:  
# https://github.com/jpetazzo/dockvpn  
# https://github.com/kylemanna/docker-openvpn  
#  
# Leaner build then Ubunutu  
FROM shift/ubuntu:15.04  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
RUN apt-get update && apt-get install --yes openvpn iptables git-core \  
&& git clone https://github.com/OpenVPN/easy-rsa.git /usr/local/share/easy-rsa
\  
&& cd /usr/local/share/easy-rsa && git checkout -b tested
89f369c5bbd13fbf0da2ea6361632c244e8af532 \  
&& ln -s /usr/local/share/easy-rsa/easyrsa3/easyrsa /usr/local/bin \  
&& rm -rf /var/lib/apt/lists/*  
  
# Needed by scripts  
ENV OPENVPN /etc/openvpn  
ENV EASYRSA /usr/local/share/easy-rsa/easyrsa3  
ENV EASYRSA_PKI $OPENVPN/pki  
ENV EASYRSA_VARS_FILE $OPENVPN/vars  
  
VOLUME ["/etc/openvpn"]  
  
# Internally uses port 1194, remap using docker  
EXPOSE 1194/udp  
# Management interface.  
EXPOSE 7507/tcp  
  
WORKDIR /etc/openvpn  
CMD ["ovpn_run"]  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  

