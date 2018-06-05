FROM ubuntu:xenial  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
version="1.7" \  
description="Samtools image for use in Workflows"  
  
RUN apt-get update && apt-get install -y \  
bzip2 \  
g++ \  
gcc \  
cmake \  
patch \  
libncurses-dev \  
libbz2-dev \  
liblzma-dev \  
make \  
git \  
autoconf \  
automake \  
ncurses-dev \  
wget \  
zlib1g-dev \  
zlib1g \  
python \  
pkg-config  
  
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
ENV version 1.7  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/samtools/releases/download/${version}/samtools-${version}.tar.bz2
&& \  
tar --bzip2 -xf samtools-${version}.tar.bz2  
  
WORKDIR /tmp/samtools-${version}  
RUN ./configure --enable-plugins --prefix=$SAMTOOLS_INSTALL_DIR && \  
make all all-htslib && \  
make install install-htslib  
  
WORKDIR /  
  
RUN ln -s $SAMTOOLS_INSTALL_DIR/bin/samtools /usr/bin/samtools  
WORKDIR /tmp  
RUN git clone https://github.com/lh3/bwa.git && \  
cd bwa && \  
make && \  
cp bwa /usr/local/bin && \  
cd /tmp && \  
git clone https://github.com/lh3/minimap2 && \  
cd minimap2 && \  
make && \  
cp minimap2 /usr/local/bin  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.8/bcftools-1.8.tar.bz2
-O /tmp/bcftools-1.8.tar.bz2 && \  
cd /tmp && \  
tar -xf bcftools-1.8.tar.bz2 && \  
cd /tmp/bcftools-1.8 && \  
make && \  
make install  
RUN cd /tmp && \  
git clone git://github.com/GregoryFaust/samblaster.git && \  
cd samblaster && \  
make && \  
cp samblaster /usr/local/bin  
RUN cd /tmp && \  
git clone \--recursive https://github.com/sfu-compbio/sinvict.git && \  
cd sinvict && \  
make && \  
cp sinvict /usr/local/bin  
RUN cd /tmp && \  
git clone https://github.com/vcftools/vcftools.git && \  
cd vcftools && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  
RUN cd /tmp && \  
git clone git://github.com/pezmaster31/bamtools.git && \  
mkdir bamtools/build && \  
cd bamtools/build && \  
cmake -DCMAKE_INSTALL_PREFIX=/root/bamtools .. && \  
make && \  
make install && \  
cp /root/bamtools/bin/bamtools /usr/bin && \  
chmod +x /usr/bin/bamtools  
RUN cd /tmp && \  
git clone https://github.com/arq5x/bedtools2.git && \  
cd /tmp/bedtools2 && \  
make && \  
make install  
RUN wget -c http://opengene.org/fastp/fastp -O /usr/local/bin/fastp && \  
chmod +x /usr/local/bin/fastp  
ENV URL http://files.happy366.cn/files/docker/  
RUN wget -c $URL/testdoc.sh -O /usr/bin/testdoc.sh && \  
wget -c $URL/rundoc.sh -O /usr/bin/rundoc.sh && \  
chmod +x /usr/bin/rundoc.sh && \  
chmod +x /usr/bin/testdoc.sh  

