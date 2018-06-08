FROM debian:9  
  
LABEL maintainer "Mats Rynge <rynge@isi.edu>"  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
gfortran \  
locales \  
locales-all \  
pkg-config \  
python \  
python-astropy \  
python-dev \  
python-pip \  
unzip \  
vim \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install Montage  
RUN cd /opt && \  
wget -nv http://montage.ipac.caltech.edu/download/Montage_v5.0.tar.gz && \  
tar xzf Montage_v5.0.tar.gz && \  
rm -f Montage_v5.0.tar.gz && \  
cd Montage && \  
make  
  
RUN mkdir /opt/montage-workflow-v2  
  
ADD * /opt/montage-workflow-v2/  
  
  

