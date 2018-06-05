FROM ubuntu:14.04  
MAINTAINER yookuda <yookuda@nig.ac.jp>  
WORKDIR /tmp  
RUN apt-get update && \  
apt-get -y install wget && \  
apt-get clean  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.29/ncbi-
blast-2.2.29+-x64-linux.tar.gz && \  
tar xzvf ncbi-blast-2.2.29+-x64-linux.tar.gz && \  
mv ncbi-blast-2.2.29+/bin/* /usr/local/bin && \  
rm -r /tmp/*  
RUN mkdir /data && \  
mkdir /db  
  

