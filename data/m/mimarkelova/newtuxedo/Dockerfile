################################################################  
# RNA-seq pipeline  
# including hisat2, samtools, stringtie and gffcompare  
# Based on Ubuntu  
################################################################  
  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Maria M <mimarkelova@gmail.com>  
  
# install dependencies first  
RUN apt-get update && apt-get install -y \  
build-essential \  
gcc-multilib \  
zlib1g-dev \  
curl \  
wget \  
cmake \  
python \  
python-pip \  
python-dev \  
python2.7-dev \  
python-numpy \  
python-matplotlib \  
hdf5-tools \  
libhdf5-dev \  
hdf5-helpers \  
libhdf5-serial-dev \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
icu-devtools \  
libssl-dev \  
libxml2-dev \  
r-bioc-biobase \  
git \  
apt-utils \  
pigz  
  
# Deploy bowtie2  
RUN cd /tmp && \  
wget -q
https://github.com/BenLangmead/bowtie2/releases/download/v2.3.4.1/bowtie2-2.3.4.1-linux-x86_64.zip
&& \  
unzip bowtie2-2.3.4.1-linux-x86_64.zip && \  
cd bowtie2-2.3.4.1-linux-x86_64 && \  
cp bowtie2 bowtie2-align-l bowtie2-align-s bowtie2-build bowtie2-build-l
bowtie2-build-s bowtie2-inspect bowtie2-inspect-l bowtie2-inspect-s
/usr/local/bin/ && \  
cd /usr/local/bin/ && \  
chmod ugo+x bowtie2 bowtie2-align-l bowtie2-align-s bowtie2-build
bowtie2-build-l bowtie2-build-s bowtie2-inspect bowtie2-inspect-l
bowtie2-inspect-s && \  
cd /tmp && \  
rm -rf bowtie2-2.3.4.1-linux-x86_64 bowtie2-2.3.4.1-linux-x86_64.zip  
  
# Install hisat2  
WORKDIR /home/docker  
RUN wget
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-Linux_x86_64.zip
&& \  
unzip hisat2-2.1.0-Linux_x86_64.zip  
RUN cp -p hisat2-2.1.0/hisat2 hisat2-2.1.0/hisat2-* /usr/bin  
  
# Install samtools  
WORKDIR /home/docker  
RUN wget
https://github.com/samtools/samtools/releases/download/1.4/samtools-1.4.tar.bz2
&& \  
tar -jxf samtools-1.4.tar.bz2 && \  
cd samtools-1.4 && \  
make && \  
make install && \  
cp samtools /usr/bin/  
  
# Install stringtie  
WORKDIR /home/docker  
RUN wget
http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.3b.Linux_x86_64.tar.gz
&& \  
tar zxf stringtie-1.3.3b.Linux_x86_64.tar.gz && \  
cp ./stringtie-1.3.3b.Linux_x86_64/stringtie /usr/bin/  
  
# Download stringtie prepDE  
WORKDIR /home/docker  
RUN wget http://ccb.jhu.edu/software/stringtie/dl/prepDE.py  
  
# Install gffcompare  
WORKDIR /home/docker  
RUN git clone https://github.com/gpertea/gclib && \  
git clone https://github.com/gpertea/gffcompare && \  
cd gffcompare && \  
make release  
ENV PATH "/gffcompare:$PATH"  
  
# Cleanup  
RUN rm -rf /docker/hisat2-2.1.0  
RUN rm -rf /docker/sratoolkit.2.8.2-1-ubuntu64  
RUN rm -rf /docker/samtools-1.4  
RUN rm -rf /docker/stringtie-1.3.3b.Linux_x86_64  
RUN apt-get clean  
RUN apt-get remove --yes --purge build-essential gcc-multilib apt-utils
zlib1g-dev vim  
  
# Set default working path  
WORKDIR /home/docker  

