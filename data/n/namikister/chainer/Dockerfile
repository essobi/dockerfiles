FROM nvidia/cuda:8.0-cudnn5-devel  
LABEL maintainer "Yuta Namiki <namikister@gmail.com>"  
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -yq \  
python3.4 \  
python3.4-minimal  
  
# Python binary and source dependencies  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq \--no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
language-pack-en \  
libcurl4-openssl-dev \  
libffi-dev \  
libssl-dev \  
python \  
python3 \  
python-dev \  
python3-dev \  
libhdf5-dev \  
zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install the recent pip release  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python2 get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py && \  
pip2 \--no-cache-dir install requests[security] && \  
pip3 \--no-cache-dir install requests[security] && \  
rm -rf /root/.cache  
  
RUN pip2 \--no-cache-dir install numpy==1.11 && \  
pip3 \--no-cache-dir install numpy==1.11  
  
RUN pip2 \--no-cache-dir install h5py && \  
pip3 \--no-cache-dir install h5py  
  
ENV CUDA_PATH /usr/local/cuda  
  
RUN pip2 \--no-cache-dir install chainer==1.19 && \  
pip3 \--no-cache-dir install chainer==1.19  
  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH  
  
# ENTRYPOINT ["/bin/bash"]  

