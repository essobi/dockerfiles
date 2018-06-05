FROM ubuntu:16.04  
# Installing dependencies of SIPp  
RUN apt-get update && \  
apt-get install -y make \  
g++ \  
libncurses5-dev \  
libssl-dev \  
openssl \  
libnet1-dev \  
libpcap0.8-dev \  
libsctp-dev \  
wget && \  
rm -rf /var/lib/apt/lists/*  
# Optional, only fr troubleshooting  
RUN apt-get update && \  
apt-get -y install \  
nano \  
ssh \  
tcpdump \  
&& rm -rf /var/lib/apt/lists/*  
# Downloading and compiling the source code of SIPp  
RUN wget
https://sourceforge.net/projects/sipp/files/sipp/3.4/sipp-3.3.990.tar.gz/download
&& \  
tar -xvzf download && \  
cd sipp-3.3.990 && \  
./configure --with-sctp --with-pcap --with-openssl && \  
make  
  
# Alternately install SIPp form ubuntu repository  
# apt-get install sip-tester  
# Copy SIPp Scripts and sample sound pcaps  
RUN mkdir scripts && mkdir pcap  
COPY scripts/ /scripts/  
COPY pcap/ /pcap/  

