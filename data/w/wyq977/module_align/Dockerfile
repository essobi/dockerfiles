# Set the base image to Ubuntu  
FROM google/cloud-sdk:latest  
  
# File Author / Maintainer  
MAINTAINER Yongqi WANG <yongqi.wang.cn@gmail.com>  
  
# The archive software SOFTWARE_NAME are downloaded into the dir  
# /tmp/SOFTWARE_NAME/, decompressed and move to /tools/  
# Other executable software are directly downloaded to dir  
# /tools/SOFTWARE_NAME/  
# Create a symbolic linke in the $PATH by the following command  
# ln -s /tools/SOFTWARE_NAME/EXE /usr/local/bin/EXE  
# Granting access to certain users is still unclear  
#---------------------------------------------------------------------  
# PRE-INSTALLATION  
#---------------------------------------------------------------------  
# Install python and dependencies, as well  
# as a few extras for helpful debugging and testing.  
# Install default-jre for fastqc  
  
RUN apt-get update && \  
apt-get install -y --force-yes \  
git \  
gzip \  
default-jre \  
libffi-dev \  
libssl-dev \  
make \  
openjdk-7-jre \  
perl \  
parallel \  
python \  
python-dev \  
python-numpy \  
python-distribute \  
python-pip \  
unzip \  
wget  
  
# Create the folder for all the tools needed  
RUN mkdir -p /tools  
  
# Install the required Python packages. May also install these via
requirements.txt  
RUN pip install --upgrade pip  
  
# Install software: BWA  
RUN mkdir -p /tools/bwa/ && \  
wget -O /tmp/bwa-0.7.15.tar.bz2 https://sourceforge.net/projects/bio-
bwa/files/bwa-0.7.15.tar.bz2/download && \  
tar xjf /tmp/bwa-0.7.15.tar.bz2 -C /tools/bwa/ && \  
cd /tools/bwa/bwa-0.7.15/ && \  
make && \  
ln -s /tools/bwa/bwa-0.7.15/bwa /usr/local/bin/bwa  
  
# Install software: Bowtie  
RUN apt-get install -y --force-yes \  
bowtie  
  
# Install software: Bowtie2  
RUN apt-get install -y --force-yes \  
libtbb2 \  
bowtie2  
  
# Install software: samtools  
RUN apt-get install -y --force-yes samtools  
  
# Install software: bedtools  
RUN apt-get install -y --force-yes bedtools  
  
# Install software: deepTools  
RUN git clone https://github.com/fidelram/deepTools && \  
cd deepTools && \  
python setup.py install  
  
# Install software: samblaster  
RUN git clone git://github.com/GregoryFaust/samblaster.git && \  
cd samblaster && \  
make && \  
cp samblaster /usr/local/bin/.  
  
  
# Clean-up  
RUN apt-get clean && \  
rm -rf /tmp/*

