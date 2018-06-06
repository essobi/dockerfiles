# DOCKERFILE for samtools https://github.com/tseemann/abricate  
FROM ummidock/assemblerflow_base:1.0.0  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
gcc \  
gzip \  
make \  
wget \  
zlib1g-dev  
  
WORKDIR /NGStools  
  
RUN wget
https://sourceforge.net/projects/samtools/files/samtools/1.4.1/samtools-1.4.1.tar.bz2  
RUN mkdir samtools && tar jxf samtools-1.4.1.tar.bz2 -C samtools --strip-
components=1  
WORKDIR /NGStools/samtools/  
RUN ./configure --without-curses --disable-bz2 --disable-lzma  
RUN make && mv samtools /usr/bin/  
WORKDIR /NGStools/  
RUN rm -rf samtools-1.4.1.tar.bz2 samtools  
  

