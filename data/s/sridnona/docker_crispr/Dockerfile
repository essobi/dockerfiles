FROM ubuntu:xenial  
  
MAINTAINER sridhar <sridhar@wustl.edu>  
  
LABEL docker_image crispr_analysis  
  
ENV SHELL bash  
  
#dependencies  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
build-essential \  
bzip2 \  
curl \  
g++ \  
git \  
less \  
libcurl4-openssl-dev \  
libpng-dev \  
libssl-dev \  
libxml2-dev \  
make \  
pkg-config \  
rsync \  
unzip \  
wget \  
zip \  
zlib1g-dev \  
libbz2-dev \  
liblzma-dev \  
python \  
python-pip \  
python-dev \  
python2.7-dev \  
hdf5-tools \  
libhdf5-dev \  
hdf5-helpers \  
ncurses-dev \  
default-jre \  
samtools  
  
RUN pip install --upgrade pip && \  
pip install --upgrade setuptools && \  
pip install numpy && \  
pip install matplotlib && \  
pip install pandas && \  
pip install scipy && \  
pip install pysam && \  
pip install biopython && \  
pip install seaborn && \  
pip install scikit-learn  
  
#Create Working Directory  
WORKDIR /docker_main  
  
#install flash  
WORKDIR /docker_main  
RUN wget http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz &&
\  
tar -zxvf FLASH-1.2.11-Linux-x86_64.tar.gz && \  
cp -p FLASH-1.2.11-Linux-x86_64/flash /usr/bin  
  
#install EMBOSS  
WORKDIR /docker_main  
RUN wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz && \  
tar -xf EMBOSS-6.6.0.tar.gz && \  
cd EMBOSS-6.6.0 && ./configure --without-x && \  
make && \  
cp -p /docker_main/EMBOSS-6.6.0/emboss/needle /usr/bin  
  
# install crispresso  
# WORKDIR /docker_main  
# RUN wget https://github.com/lucapinello/CRISPResso/archive/master.zip && \  
# unzip master.zip && \  
# cd CRISPResso-master && python setup.py install && \  
# cp -p CRISPResso-master/* /usr/bin  
RUN wget https://github.com/lucapinello/CRISPResso/archive/master.zip  
  
RUN unzip master.zip  
  
RUN cd CRISPResso-master && python setup.py install  
  
ENV PATH /root/CRISPResso_dependencies/bin:$PATH  
  
# Clean up  
RUN cd /docker_main / && \  
rm -rf CRISPResso-master FLASH-1.2.11-Linux-x86_64 EMBOSS-6.6.0 && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
apt-get clean  
  
# needed for MGI data mounts  
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all  
  
# Set default working path  
WORKDIR /docker_main  

