FROM ubuntu:16.04  
  
RUN apt-get update -yq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq iptables openssl strongswan
strongswan-ikev2 && \  
rm -rf /var/lib/apt/lists/*  
# RUN wget https://download.strongswan.org/strongswan-5.5.1.tar.bz2 && \  
# echo "4eba9474f7dc6c8c8d7037261358e68d strongswan-5.5.1.tar.bz2" >> MD5SUM
&& \  
# md5sum -c MD5SUM && \  
# tar xf strongswan-5.5.1.tar.bz2  
  
EXPOSE 4500/udp 500/udp  

