FROM debian:8-slim  
  
# Dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
wget ca-certificates  
  
WORKDIR /srv  
  
# Prince  
ENV PRINCE_VERSION 11.3  
ENV PRINCE_REVISION 1  
RUN wget
https://www.princexml.com/download/prince_${PRINCE_VERSION}-${PRINCE_REVISION}_debian8.0_amd64.deb
\  
&& dpkg --force-all --install
prince_${PRINCE_VERSION}-${PRINCE_REVISION}_debian8.0_amd64.deb \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends -f
install \  
&& rm -f prince_${PRINCE_VERSION}-${PRINCE_REVISION}_debian8.0_amd64.deb  
  
# Dropbear  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends -f
install \  
dropbear  
  
# Cleanup  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y purge \  
wget ca-certificates \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --purge autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# User  
RUN adduser --disabled-password --gecos "" prince \  
&& passwd -d -u prince  
  
CMD ["bash"]  

