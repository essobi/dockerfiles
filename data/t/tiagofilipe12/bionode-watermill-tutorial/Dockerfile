# DOCKERFILE for bionode-watermill two-mappers example  
FROM ubuntu:16.04  
MAINTAINER Tiago F. Jesus, tiagojesus@medicina.ulisboa.pt  
  
# INSTALL DEPENDENCIES  
RUN apt-get update  
RUN apt-get -y install unzip gzip wget gcc g++ libtbb-dev bzip2 make
zlib1g-dev sudo curl zsh  
RUN apt-get -y install git npm  
  
# INSTALL node.js version 7  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
### BOWTIE2 INSTALL ###  
WORKDIR /bin/  
RUN wget https://downloads.sourceforge.net/project/bowtie-
bio/bowtie2/2.3.2/bowtie2-2.3.2-linux-x86_64.zip  
RUN unzip bowtie2-2.3.2-linux-x86_64.zip  
RUN rm -rf bowtie2-2.3.2-linux-x86_64.zip  
  
# ADD BOWTIE TO PATH  
ENV PATH="/bin/bowtie2-2.3.2:${PATH}"  
### BWA INSTALL ###  
RUN wget https://sourceforge.net/projects/bio-bwa/files/bwa-0.7.15.tar.bz2  
RUN tar jxf bwa-0.7.15.tar.bz2  
RUN rm -rf bwa-0.7.15.tar.bz2  
WORKDIR /bin/bwa-0.7.15/  
RUN make  
  
# ADD BWA TO PATH  
ENV PATH="/bin/bwa-0.7.15:${PATH}"  
### DOWNLOAD FASTQ-DUMP ###  
WORKDIR /bin/  
RUN wget https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-ubuntu64.tar.gz  
  
# EXTRACT THE FOLDER  
RUN tar -zxvf sratoolkit.2.8.2-1-ubuntu64.tar.gz  
RUN rm -rf sratoolkit.2.8.2-1-ubuntu64.tar.gz  
  
# PUT STA-TOOLKIT IN PATH  
ENV PATH="/bin/sratoolkit.2.8.2-1-ubuntu64/bin:${PATH}"  
### INSTALL SAMTOOLS ###  
RUN wget
https://sourceforge.net/projects/samtools/files/samtools/1.4.1/samtools-1.4.1.tar.bz2  
RUN tar jxf samtools-1.4.1.tar.bz2  
RUN rm -rf samtools-1.4.1.tar.bz2  
WORKDIR /bin/samtools-1.4.1/  
RUN ./configure --without-curses --disable-bz2 --disable-lzma  
RUN make  
ENV PATH="/bin/samtools-1.4.1:${PATH}"  
### FINAL BLOCK ###  
WORKDIR /bin/  
  
# CLONE BIONODE-WATERMILL FROM GIT HUB  
RUN git clone https://github.com/bionode/bionode-watermill.git  
  
# CHANGE DIRECTORY TO BIONODE-WATERMILL  
WORKDIR /bin/bionode-watermill  
RUN npm install  
RUN npm install bionode-ncbi -g  
  
# START zsh before using iteractive mode  
RUN zsh  

