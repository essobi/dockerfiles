#################### BASE IMAGE ######################  
FROM ubuntu:16.04  
  
#################### MAINTAINER ######################  
MAINTAINER Daniel E. Martin-Herranz <daniel@chronomics.co.uk>  
  
################## INSTALLATION ######################  
WORKDIR /usr/local/bin  
  
## General tools  
  
RUN apt-get update -y && apt-get install -y wget unzip less vim bzip2 make gcc
zlib1g-dev libncurses-dev git g++ python openjdk-8-jre curl libbz2-dev
liblzma-dev build-essential python-pip libpython2.7-dev && pip install
--upgrade pip  
  
## FastQC  
  
ENV DST=/tmp/  
ENV URL=http://www.bioinformatics.babraham.ac.uk/projects/fastqc/  
ENV ZIP=fastqc_v0.11.7.zip  
RUN wget $URL/$ZIP -O $DST/$ZIP && unzip - $DST/$ZIP -d $DST && rm $DST/$ZIP
&& cd $DST/FastQC && chmod 755 fastqc && ln -s $DST/FastQC/fastqc
/usr/local/bin/fastqc  
  
## Cutadapt  
  
RUN pip install 'cutadapt==1.15'  
  
## Trim Galore  
  
WORKDIR /tmp/  
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz
-o trim_galore.tar.gz  
RUN tar xvzf trim_galore.tar.gz  
RUN mv TrimGalore-0.4.5/trim_galore /usr/local/bin  
  
## BWA  
  
WORKDIR /usr/local/bin  
RUN git clone https://github.com/lh3/bwa && cd bwa && git checkout
9f26bfcc7780753129b60717ecab0ebba6f04b7c && make  
ENV PATH=$PATH:/usr/local/bin/bwa  
  
## Samtools  
  
WORKDIR /usr/local/  
RUN wget
https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2  
RUN tar xvjf samtools-1.7.tar.bz2 && rm samtools-1.7.tar.bz2 && cd
samtools-1.7 \  
&& ./configure --prefix=/usr/local/bin/samtools-1.7/ && make && make install  
ENV PATH=$PATH:/usr/local/bin/samtools-1.7/bin/  
  
## Strelka2  
  
WORKDIR /usr/local/  
RUN git clone https://github.com/Illumina/strelka.git && cd strelka && git
checkout 105d8371f84018750eaaff6e205e3de1dbd6dfdd && mkdir build && cd build
&& ../configure --jobs=4 --prefix=/usr/local/bin/ && make -j4 install  
  
## Cramtools  
  
WORKDIR /usr/local/bin/  
RUN git clone https://github.com/enasequence/cramtools.git  
  
################## END OF DOCKERFILE ######################  

