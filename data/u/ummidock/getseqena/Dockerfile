# DOCKERFILE for getSeqEna https://github.com/B-UMMI/getSeqENA  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
gawk \  
bc \  
bzip2 \  
gcc \  
gzip \  
git \  
make \  
wget \  
unzip \  
python \  
python3 \  
zlib1g-dev  
  
RUN ln -sf /usr/bin/gawk /usr/bin/awk  
  
WORKDIR /NGStools  
  
RUN wget
https://sourceforge.net/projects/samtools/files/samtools/1.3.1/samtools-1.3.1.tar.bz2  
RUN mkdir samtools && tar jxf samtools-1.3.1.tar.bz2 -C samtools --strip-
components=1  
  
WORKDIR /NGStools/samtools/  
  
RUN ./configure --without-curses --disable-bz2 --disable-lzma  
RUN make  
ENV PATH="/NGStools/samtools:$PATH"  
WORKDIR /NGStools/  
  
RUN rm -rf samtools-1.4.1.tar.bz2  
  
# Install aspera connect  
RUN useradd -ms /bin/bash ubuntu  
# Needs to be installed as a user  
USER ubuntu  
WORKDIR /home/ubuntu/  
  
RUN wget https://download.asperasoft.com/download/sw/connect/3.7.4/aspera-
connect-3.7.4.147727-linux-64.tar.gz && \  
tar -zxvf aspera-connect-3.7.4.147727-linux-64.tar.gz && \  
chmod +x aspera-connect-3.7.4.147727-linux-64.sh && \  
./aspera-connect-3.7.4.147727-linux-64.sh  
  
# Move the user data to NGStools using root  
USER root  
WORKDIR /NGStools/  
RUN mkdir aspera && mv /home/ubuntu/.aspera/connect aspera  
ENV PATH="/NGStools/aspera/connect/bin:$PATH"  
# Install SRA tools  
RUN wget https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz && \  
tar xf sratoolkit.current-ubuntu64.tar.gz  
ENV PATH="/NGStools/sratoolkit.2.9.0-ubuntu64/bin:$PATH"  
# Install getseqena  
RUN git clone https://github.com/B-UMMI/getSeqENA.git  
ENV PATH="/NGStools/getSeqENA/:$PATH"  

