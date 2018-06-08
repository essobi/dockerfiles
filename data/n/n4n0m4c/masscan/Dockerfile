FROM ubuntu  
RUN \  
apt update && \  
apt -y dist-upgrade && \  
apt -y install git clang make libc6-dev libpcap-dev linux-kernel-headers gcc
&& \  
cd /tmp && \  
git clone https://github.com/r0p0s3c/masscan && \  
cd masscan && \  
make -j && \  
mv bin/masscan /bin && \  
rm -rf /tmp/masscan && \  
apt --purge -yy remove git clang make linux-kernel-headers gcc && \  
apt --purge -yy autoremove && \  
rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["/bin/masscan"]  

