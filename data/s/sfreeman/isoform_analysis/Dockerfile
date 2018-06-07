FROM ubuntu:16.04  
MAINTAINER Sam Freeman  
  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && apt-get install -y \  
build-essential \  
cmake \  
libboost-all-dev \  
libboost-program-options-dev \  
libtbb-dev \  
libncurses5-dev \  
libreadline6-dev \  
openjdk-7-jdk \  
openjdk-8-jdk \  
python2.7 \  
unzip \  
vim-common \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# samtools  
RUN cd /opt && \  
wget --no-check-certificate
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar -xf samtools-1.3.1.tar.bz2 && rm samtools-1.3.1.tar.bz2 && cd
samtools-1.3.1 && make && make install && make clean  
  
# bowtie2  
RUN cd /opt && \  
wget -O bowtie2.zip https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.3.1/bowtie2-2.3.1-linux-x86_64.zip/download && \  
unzip bowtie2.zip && rm bowtie2.zip  
ENV PATH $PATH:/opt/bowtie2-2.3.1  
  
# tophat  
RUN cd /opt && \  
wget --no-check-certificate
http://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.tar.gz && \  
tar -xf tophat-2.1.1.tar.gz && rm tophat-2.1.1.tar.gz && cd tophat-2.1.1 &&
./configure && make && make install && make clean  
  
# cufflinks  
RUN cd /opt && \  
wget http://cole-trapnell-
lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
&& \  
tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz && rm
cufflinks-2.2.1.Linux_x86_64.tar.gz  
ENV PATH /opt/cufflinks-2.2.1.Linux_x86_64:$PATH  
  
  
# clean up  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  

