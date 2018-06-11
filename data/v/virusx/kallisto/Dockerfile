FROM ubuntu:16.04  
ENV KALLISTO_VERSION=0.43.1  
RUN apt-get update && \  
apt-get install -y wget && \  
cd /root/ && \  
wget
"https://github.com/pachterlab/kallisto/releases/download/v0.43.1/kallisto_linux-v${KALLISTO_VERSION}.tar.gz"
-O- \  
| tar --no-same-owner -xz && \  
mv kallisto_linux-v${KALLISTO_VERSION}/kallisto /usr/local/bin/ && \  
rm -rf kallisto_linux-v${KALLISTO_VERSION}/ && \  
apt-get purge -y wget && \  
apt-get autoremove -y --purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

