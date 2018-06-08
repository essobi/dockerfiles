### forked from NCBI-Hackathons/MetagenomicAntibioticResistance  
FROM ubuntu:latest  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>  
  
RUN apt-get update && apt-get install --yes \  
build-essential \  
gcc-multilib \  
apt-utils \  
zlib1g-dev \  
vim-common \  
wget \  
libncurses5-dev \  
autotools-dev \  
autoconf \  
git \  
perl \  
r-base \  
python \  
libbz2-dev \  
liblzma-dev \  
apt-utils \  
libz-dev \  
ncurses-dev \  
zlib1g-dev \  
libcurl3 \  
libcurl4-openssl-dev \  
libxml2-dev  
  
WORKDIR /opt  
RUN git clone https://github.com/samtools/htslib.git  
WORKDIR /opt/htslib  
RUN autoheader  
RUN autoconf  
RUN ./configure  
RUN make  
RUN make install  
ENV PATH "$PATH:/opt/htslib/"  
WORKDIR /opt  
RUN git clone https://github.com/samtools/samtools.git  
WORKDIR /opt/samtools  
RUN autoheader  
RUN autoconf -Wno-syntax  
RUN ./configure # Optional, needed for choosing optional functionality  
RUN make  
RUN make install  
ENV PATH "$PATH:/opt/samtools/"  
WORKDIR /opt/  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-
blast-2.7.1+-x64-linux.tar.gz  
RUN tar xvzf ncbi-blast-2.7.1+-x64-linux.tar.gz  
WORKDIR /opt/ncbi-blast-2.7.1+  
ENV PATH "$PATH:/opt/ncbi-blast-2.7.1+/"  
WORKDIR /opt/  
RUN wget https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz  
RUN tar xvzf sratoolkit.current-ubuntu64.tar.gz  
WORKDIR /opt/sratoolkit.2.9.0-ubuntu64  
ENV PATH "$PATH: /opt/sratoolkit.2.9.0-ubuntu64/bin/"  
RUN apt-get install -y unzip  
  
WORKDIR /opt/  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/1.3.0/ncbi-
magicblast-1.3.0-x64-linux.tar.gz  
RUN tar xvzf ncbi-magicblast-1.3.0-x64-linux.tar.gz  
WORKDIR /opt/ncbi-magicblast-1.3.0  
ENV PATH "$PATH:/opt/ncbi-magicblast-1.3.0/bin/"  
RUN apt-get install -y libtool pkg-config libgd-gd2-perl  
  
WORKDIR /opt/  
RUN git clone https://github.com/agordon/fastx_toolkit.git  
WORKDIR /opt/fastx_toolkit  
###  
RUN git clone https://github.com/agordon/libgtextutils.git  
WORKDIR /opt/fastx_toolkit/libgtextutils  
RUN ./reconf  
RUN ./configure  
RUN make  
RUN make install  
###  
WORKDIR /opt/fastx_toolkit  
RUN ./reconf  
RUN ./configure  
RUN make  
RUN make install  
RUN cpan 'PerlIO::gzip'  
RUN cpan 'GD::Graph::bars'  
  
WORKDIR /  
RUN git clone https://github.com/stevetsa/MetagenomicAntibioticResistance.git  

