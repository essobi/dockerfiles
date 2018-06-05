# Dockerfile for bridger: transcriptome assembler  
# bridger release 2014-12-01  
# usage: docker run -v `pwd`:/data -w /data inutano/bridger bridger --seqType
fq --left /data/left.fastq.gz --right /data/right.fastq.gz --CPU 4  
# from ubuntu  
FROM ubuntu:trusty  
  
# :)  
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com  
  
RUN apt-get -y update && \  
apt-get install -y \  
wget \  
make \  
libncurses5-dev \  
libncursesw5-dev \  
libboost-all-dev \  
g++ && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src  
ENV VERSION 2014-12-01  
RUN wget
"https://sourceforge.net/projects/rnaseqassembly/files/Bridger_r${VERSION}.tar.gz"
&& \  
tar zxvf Bridger_r${VERSION}.tar.gz && \  
cd Bridger_r${VERSION} && \  
./configure && \  
make && \  
cp -r /src/Bridger_r${VERSION} /usr/bin && \  
ln -s /usr/bin/Bridger_r${VERSION}/Bridger.pl /usr/bin/bridger  
  
CMD /bin/bash  

