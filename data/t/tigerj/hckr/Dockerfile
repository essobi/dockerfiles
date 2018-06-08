# Base image  
FROM kalilinux/kali-linux-docker  
  
# install goodies  
RUN apt-get update && apt-get install -y \  
aircrack-ng \  
curl \  
cowsay \  
gcc \  
git \  
make \  
nmap \  
netcat \  
pciutils \  
pv \  
tcpdump \  
youtube-dl \  
wget  
  
## get github repos and build  
# hashcat  
WORKDIR /usr/src  
RUN git clone https://github.com/hashcat/hashcat.git  
WORKDIR /usr/src/hashcat  
RUN git submodule update --init && \  
make && \  
make install  
  
# hashcat-utils  
WORKDIR /tmp  
RUN git clone https://github.com/hashcat/hashcat-utils.git  
WORKDIR /tmp/hashcat-utils/src  
RUN make  
RUN for binaries in $(ls *.bin); do mv $binaries /usr/local/bin/$(echo
"$binaries" | sed 's/\\.bin//g'); done  
  
# create work dir  
RUN mkdir -p /home/hckr  
WORKDIR /home/hckr  
  
## now clean up  
RUN rm -rf /tmp/*  

