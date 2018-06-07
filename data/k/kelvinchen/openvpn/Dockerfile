FROM kelvinchen/base:latest  
  
# Install OpenVPN  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
openvpn \  
easy-rsa \  
iptables \  
bridge-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/share/easy-rsa  
  
EXPOSE 1194/udp  
  
VOLUME /config  
  
COPY container-root/ /  
  
CMD ["/init"]  

