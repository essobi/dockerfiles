# copyright 2017-2018 Regents of the University of California and the Broad
Institute. All rights reserved.  
FROM ubuntu:14.04  
  
RUN \  
sed -Ei 's/^# (deb.*xenial-backports.*)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y autoconf automake byobu bzip2 curl gfortran git htop lzma
man sudo unzip vim wget && \  
apt-get install -y libbz2-dev libcurl4-openssl-dev libgsl0-dev liblzma-dev
libncurses5-dev libpcre3-dev \  
libreadline6-dev libssl-dev python-dev python-pip zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && \  
wget http://ftp-trace.ncbi.nlm.nih.gov/sra/ngs/1.3.0/ngs-
sdk.1.3.0-linux.tar.gz && \  
tar xzvf ngs-sdk.1.3.0-linux.tar.gz && \  
git clone https://github.com/infphilo/hisat2.git  
  
WORKDIR /tmp/hisat2  
RUN git checkout master && \  
make USE_SRA=1 NCBI_NGS_DIR=/tmp/ngs-sdk.1.3.0-linux NCBI_VDB_DIR=/tmp/ngs-
sdk.1.3.0-linux  
  
COPY common/container_scripts/* /usr/local/bin/  
COPY *.sh *.py /usr/local/bin/  
  
RUN cp -p hisat2 hisat2-* /usr/local/bin && \  
pip install awscli && \  
apt-get update && \  
apt-get -y install samtools=0.1.19-1 && \  
apt-get install zip --yes && \  
apt-get clean && \  
cp -p /tmp/hisat2/hisat2_* /usr/local/bin && \  
cp -p /tmp/hisat2/extract*.py /usr/local/bin && \  
chmod ugo+x /usr/local/bin/*.sh && \  
cd / && \  
wget http://ftp-trace.ncbi.nlm.nih.gov/sra/ngs/1.3.0/ngs-
sdk.1.3.0-linux.tar.gz && \  
tar xzvf ngs-sdk.1.3.0-linux.tar.gz && \  
export LD_LIBRARY_PATH=/ngs-sdk.1.3.0-linux/lib64:$LD_LIBRARY_PATH  
  
ENV HISAT2_HOME /hisat2-2.1.0  
  
  
CMD ["/usr/local/bin/runS3OnBatch.sh" ]  
  

