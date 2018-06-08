FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
lsb-release \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
module-init-tools \  
openjdk-8-jdk \  
pkg-config \  
python \  
python-dev \  
python-numpy \  
rsync \  
unzip \  
vim \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# use CA certs from CVMFS  
RUN mkdir -p /etc/grid-security && \  
ln -f -s /cvmfs/oasis.opensciencegrid.org/mis/certificates /etc/grid-
security/certificates  
  
# required directories  
RUN mkdir -p /cvmfs  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  
  

