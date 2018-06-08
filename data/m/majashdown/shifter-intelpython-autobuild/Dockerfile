FROM ubuntu:17.10  
WORKDIR /root  
  
# Install Ubuntu packages:  
#  
# - curl and ca-certificates, for downloading software;  
# - gcc, gfortran, g++ and make, for compiling MPICH;  
# - bzip2, for installing Anaconda.  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
bzip2 ca-certificates curl gcc gfortran g++ make && \  
rm -rf /var/lib/apt/lists/*  
  
# Download, compile and install MPICH in /usr/local (the default  
# installation location). It has to be compiled like this to work  
# with Shifter.  
RUN curl -O https://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz &&
\  
tar -zxf mpich-3.2.1.tar.gz && \  
cd mpich-3.2.1 && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf mpich-3.2.1 && \  
rm -f mpich-3.2.1.tar.gz  
  
# Install Anaconda Python 3 distribution in /usr/local (using the  
# minimal Miniconda installer).  
RUN curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
/bin/bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local && \  
rm -f Miniconda3-latest-Linux-x86_64.sh  
  
# Configure Anaconda to use the Intel distribution for Python.  
# Installing the intelpython package replaces most of the other  
# packages with the Intel versions.  
RUN conda config --add channels intel && \  
conda install -y -q intelpython  
  
# Install mpi4py using pip. Doing it this way means it is compiled  
# from source using MPICH.  
RUN pip install mpi4py  

