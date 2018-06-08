FROM ubuntu:14.04  
MAINTAINER jcrandall@alum.mit.edu  
  
# Install build dependencies, build samtools from source  
RUN \  
apt-get -q=2 update && \  
apt-get -q=2 -y \--no-install-recommends install ca-certificates build-
essential git autoconf zlib1g-dev libcurl4-gnutls-dev libbz2-dev libssl-dev
liblzma-dev libncurses-dev zlib1g libcurl3-gnutls && \  
cd /tmp && \  
git clone https://github.com/samtools/htslib.git && \  
cd htslib && \  
git checkout 1.6 && \  
make && \  
cp htsfile /usr/local/bin && \  
cp bgzip /usr/local/bin && \  
cp tabix /usr/local/bin && \  
cd .. && \  
git clone https://github.com/samtools/samtools.git && \  
cd samtools && \  
git checkout 1.6 && \  
make && \  
cp samtools /usr/local/bin && \  
cd .. && \  
rm -rf /tmp/htslib && \  
rm -rf /tmp/samtools && \  
apt-get -q=2 -y purge ca-certificates build-essential git autoconf zlib1g-dev
libcurl4-gnutls-dev libbz2-dev libssl-dev liblzma-dev libncurses-dev && \  
apt-get -q=2 -y autoremove && \  
apt-get -q=2 -y clean && \  
rm -rf /var/lib/apt/lists/*  
  

