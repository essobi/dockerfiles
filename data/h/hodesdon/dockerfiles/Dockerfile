# Documentation example  
  
FROM ubuntu:12.04  
  
MAINTAINER "Kate Hodesdon" <kate.hodesdon@sbgenomics.com>  
  
RUN apt-get -y update && \  
apt-get install -y wget build-essential zlib1g-dev libncurses5-dev && \  
wget --no-check-certificate
https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2
&& \  
tar jxf samtools-1.2.tar.bz2 && \  
cd samtools-1.2 && make && \  
make install  

