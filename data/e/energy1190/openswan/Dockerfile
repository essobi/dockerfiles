FROM debian:jessie  
  
ENV VERSION=2.6.48  
  
RUN apt-get update && \  
apt-get install -q -y \  
libgmp3-dev \  
gawk \  
flex \  
bison \  
iproute \  
iptables \  
sed \  
python \  
wget \  
make \  
libgmp-dev \  
module-init-tools \  
autoconf \  
curl \  
gcc \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://download.openswan.org/openswan/openswan-${VERSION}.tar.gz &&
\  
tar -zxvf openswan-${VERSION}.tar.gz -C /usr/src/ && \  
rm -f openswan-${VERSION}.tar.gz && \  
cd /usr/src/openswan-${VERSION} && \  
make programs && \  
make install  
  
EXPOSE 500/udp 4500/udp  
  
CMD ["/usr/bin/tail", "-f", "/dev/null"]  

