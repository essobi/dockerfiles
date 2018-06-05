FROM continuumio/miniconda  
MAINTAINER Fabrice Jossinet (fjossinet@gmail.com)  
RUN apt-get update && apt-get install -y git wget build-essential  
  
#bowtie2  
WORKDIR /  
RUN apt-get -y install zip unzip libtbb-dev libreadline-dev zlib1g-dev  
RUN wget -q https://github.com/BenLangmead/bowtie2/archive/master.zip && unzip
master.zip  
WORKDIR bowtie2-master  
RUN make && make install && make clean  
  
#tophat2  
WORKDIR /  
RUN apt-get -y install libbz2-dev libboost-all-dev  
RUN wget -qO tophat-2.1.1.tar.gz
https://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.tar.gz && tar -xzvf
tophat-2.1.1.tar.gz  
WORKDIR tophat-2.1.1  
RUN ./configure  
RUN make && make install && make clean  
  
#samtools  
WORKDIR /  
RUN apt-get -y install libncurses5-dev liblzma-dev  
RUN wget -qO samtools-1.4.tar.bz2
https://github.com/samtools/samtools/releases/download/1.4/samtools-1.4.tar.bz2
&& bunzip2 -d samtools-1.4.tar.bz2 && tar -xvf samtools-1.4.tar  
WORKDIR samtools-1.4  
RUN ./configure  
RUN make && make install && make clean  

