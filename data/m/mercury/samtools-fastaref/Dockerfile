FROM ubuntu:14.04  
MAINTAINER th10@sanger.ac.uk  
  
WORKDIR /tmp  
  
# Build a local fork of htslib  
RUN \  
apt-get -q=2 update && \  
apt-get -q=2 install ca-certificates && \  
apt-get -q=2 -y --no-install-recommends install build-essential git zlib1g-dev
libbz2-dev liblzma-dev libcurl4-openssl-dev libncurses5-dev automake autoconf
&& \  
git clone https://github.com/wtsi-hgi/htslib.git && \  
cd htslib && \  
git checkout 62cfaa0fe71e6fd8f0beac45d5264ab5fef3c30c && \  
autoreconf && \  
./configure && \  
make && \  
cp htsfile /usr/local/bin && \  
cp bgzip /usr/local/bin && \  
cp tabix /usr/local/bin  
  
# Build local fork of samtools  
RUN \  
git clone https://github.com/wtsi-hgi/samtools.git && \  
cd samtools && \  
git checkout 2e36cc84942eee4ba24e9d4c7747027f10b8b042 && \  
autoreconf && \  
./configure && \  
make && \  
cp samtools /usr/local/bin  
  
# Cleanup  
RUN \  
rm -rf /tmp/htslib && \  
rm -rf /tmp/samtools && \  
apt-get -q=2 -y purge build-essential git automake autoconf && \  
apt-get -q=2 -y autoremove && \  
apt-get -q=2 -y clean && \  
rm -rf /var/lib/apt/lists/*  

