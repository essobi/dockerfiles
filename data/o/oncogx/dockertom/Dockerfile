### set the base image to Ubuntu  
FROM ubuntu:16.04  
  
### File author / maintainer  
MAINTAINER Olivier Harismendy "oharismendy@ucsd.edu"  
  
### change a working directory to /opt #######  
WORKDIR /opt  
  
### Set up CRAN repo  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list && \  
gpg \--keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add -  
  
### install  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
curl \  
git \  
g++ \  
libncurses5-dev \  
libssl-dev \  
libboost-all-dev \  
libbz2-dev \  
make \  
man \  
pkg-config \  
python \  
python-pip \  
python-dev \  
software-properties-common \  
screen \  
vim \  
wget \  
zip \  
zlibc \  
zlib1g \  
zlib1g-dev \  
r-base \  
r-base-dev  
  
  
  
RUN wget
https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2
&& \  
tar -xjvf htslib-1.3.2.tar.bz2 && \  
cd htslib-1.3.2 && \  
make && \  
make install  
  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar -xjvf samtools-1.3.1.tar.bz2 && \  
cd samtools-1.3.1 && \  
make && \  
make install  
  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2
&& \  
tar -xjvf bcftools-1.3.1.tar.bz2 && \  
cd bcftools-1.3.1 && \  
make && \  
make install  
  
  
RUN wget
https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz
&& \  
tar -xvzf bedtools-2.26.0.tar.gz && \  
cd bedtools2 && \  
make && \  
cp bin/* /usr/local/bin  
  
  
RUN wget
https://github.com/vcftools/vcftools/releases/download/v0.1.14/vcftools-0.1.14.tar.gz
&& \  
tar -xzvf vcftools-0.1.14.tar.gz && \  
cd vcftools-0.1.14 && \  
./configure && \  
make && \  
make install  
  
  
RUN pip install --upgrade pip && \  
pip install variant_tools \  
multiqc  
  
RUN wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip
&&\  
unzip fastqc_v0.11.5.zip &&\  
cp FastQC/fastqc /usr/local/bin  
  
RUN wget https://sourceforge.net/projects/bio-bwa/files/bwa-0.7.15.tar.bz2 &&
\  
tar -xjvf bwa-0.7.15.tar.bz2 && \  
cd bwa-0.7.15 && \  
make && \  
cp bwa /usr/local/bin  
  
  
RUN git clone --recursive https://github.com/vcflib/vcflib.git && \  
cd vcflib && \  
make &&\  
cp bin/* /usr/local/bin  
  
WORKDIR /opt  
  
RUN chmod a+x /usr/local/bin/*  
  
WORKDIR /scratch  
  
CMD ["/bin/bash"]  

