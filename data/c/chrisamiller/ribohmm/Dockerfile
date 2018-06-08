FROM ubuntu:xenial  
MAINTAINER Chris Miller <c.a.miller@wustl.edu>  
  
LABEL Image for running ribohmm  
  
#some basic tools  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
build-essential \  
git \  
python-pip \  
python-dev \  
gfortran \  
libblas-dev \  
liblapack-dev \  
zlib1g-dev  
  
RUN pip install numpy==1.13.0 && \  
pip install scipy==0.19.0 && \  
pip install cython==0.25.2 && \  
pip install pysam==0.11.2.2 && \  
pip install cvxopt==1.2.0  
  
RUN cd /usr/src && \  
git clone https://github.com/rajanil/riboHMM && \  
cd riboHMM && \  
sed -i.bak 's/restrict/restrict1/g' ribohmm.pyx && \  
sed -i.bak 's/restrict/restrict1/g' ribohmm.pxd && \  
python setup.py build_ext --inplace  
  
  
# ##############  
# #HTSlib 1.3.2#  
# ##############  
# ENV HTSLIB_INSTALL_DIR=/opt/htslib  
  
# WORKDIR /tmp  
# RUN wget
https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2
&& \  
# tar --bzip2 -xvf htslib-1.3.2.tar.bz2 && \  
# cd /tmp/htslib-1.3.2 && \  
# ./configure --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \  
# make && \  
# make install && \  
# cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/  
# #&& \  
# # ln -s $HTSLIB_INSTALL_DIR/bin/tabix /usr/bin/tabix  
  
# ################  
# #Samtools 1.3.1#  
# ################  
# ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
  
# WORKDIR /tmp  
# RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
# tar --bzip2 -xf samtools-1.3.1.tar.bz2 && \  
# cd /tmp/samtools-1.3.1 && \  
# ./configure --with-htslib=$HTSLIB_INSTALL_DIR --prefix=$SAMTOOLS_INSTALL_DIR
&& \  
# make && \  
# make install && \  
# cd / && \  
# rm -rf /tmp/samtools-1.3.1 && \  
# ln -s /opt/samtools/bin/* /usr/bin/  
  
  
# needed for MGI data mounts and timezone  
RUN apt-get update && apt-get install -y libnss-sss tzdata && apt-get clean
all  
  
#set timezone to CDT  
#LSF: Java bug that need to change the /etc/timezone.  
#/etc/localtime is not enough.  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
echo "America/Chicago" > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  

