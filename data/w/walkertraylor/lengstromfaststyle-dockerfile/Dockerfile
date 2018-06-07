# Start with cuDNN base image  
FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Kai Arulkumaran <design@kaixhin.com>  
  
# Install git, wget, bc and dependencies  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
bc \  
cmake \  
libatlas-base-dev \  
libatlas-dev \  
libboost-all-dev \  
libopencv-dev \  
libprotobuf-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
protobuf-compiler \  
libhdf5-dev \  
libleveldb-dev \  
liblmdb-dev \  
libsnappy-dev \  
python-dev \  
python-pip \  
python-numpy \  
gfortran \  
libyaml-dev \  
> /dev/null  
  
#Update so pip installs work  
RUN pip install --upgrade pip  
  
# Install NCCL for multi-GPU communication  
RUN wget
https://github.com/NVIDIA/nccl/releases/download/v1.2.3-1%2Bcuda8.0/libnccl1_1.2.3-1.cuda8.0_amd64.deb
&& \  
dpkg -i libnccl1_1.2.3-1.cuda8.0_amd64.deb && \  
rm libnccl1_1.2.3-1.cuda8.0_amd64.deb  
  
RUN wget
https://github.com/NVIDIA/nccl/releases/download/v1.2.3-1%2Bcuda8.0/libnccl-
dev_1.2.3-1.cuda8.0_amd64.deb && \  
dpkg -i libnccl-dev_1.2.3-1.cuda8.0_amd64.deb && \  
rm libnccl-dev_1.2.3-1.cuda8.0_amd64.deb  
  
# Clone Caffe repo and move into it  
RUN cd /root && git clone https://github.com/BVLC/caffe.git  
  
RUN pip install Cython>=0.19.2  
RUN pip install numpy>=1.7.1  
RUN pip install scipy>=0.13.2  
RUN pip install scikit-image>=0.9.3  
RUN pip install matplotlib>=1.3.1  
RUN pip install ipython>=3.0.0  
RUN pip install h5py>=2.2.0  
RUN pip install leveldb>=0.191  
RUN pip install networkx>=1.8.1  
RUN pip install nose>=1.3.0  
RUN pip install pandas>=0.12.0  
RUN pip install "python-dateutil>=1.4,<2"  
RUN pip install protobuf>=2.5.0  
RUN pip install python-gflags>=2.0  
RUN pip install pyyaml>=3.10  
RUN pip install Pillow>=2.3.0  
RUN pip install six>=1.1.0%  
  
# Install python dependencies (in case the change upstream before the
enumeration above is updated)  
RUN cd /root/caffe && cat python/requirements.txt | xargs -n1 pip install  
  
# Move into Caffe repo  
RUN cd /root/caffe && \  
# Make and move into build directory  
mkdir build && cd build && \  
# CMake  
cmake .. && \  
# Make  
make -j"$(nproc)" all && \  
make install  
  
# Add to Python path  
ENV PYTHONPATH=/root/caffe/python:$PYTHONPATH  
  
# Set ~/caffe as working directory  
WORKDIR /root/caffe  
  
# Install Ubuntu 16.04, CUDA 8 and cudnn 5, and miniconda3  
#FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04  
#FROM continuumio/miniconda3  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.1.11-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
  
RUN apt-get update && apt-get install -y sudo software-properties-common  
  
# Install wget and build-essential  
#RUN apt-get update && apt-get install -y \  
# build-essential \  
# wget  
# Install pip, python, and nano  
RUN sudo apt-get update && sudo apt-get -y upgrade  
RUN sudo apt-get install -y python-pip \  
nano \  
unzip  
  
# Install ffmpeg  
RUN apt-get update && \  
apt-get -y install \  
software-properties-common && \  
apt-add-repository -y ppa:mc3man/trusty-media && \  
apt-get update && \  
apt-get -y install ffmpeg && \  
rm -rf /var/lib/apt/lists/*  
  
# Install virtualenv  
#RUN pip install virtualenv  
# Clone fast-style-transfer GitHub repo  
RUN cd /root/ && git clone https://github.com/lengstrom/fast-style-
transfer.git  
  
# Set working directory to fast-style-transfer  
WORKDIR /root/fast-style-transfer  
  
# Download rain princess checkpoint  
RUN git clone https://github.com/thommiano/udlf_fst_checkpoints.git  
  
# Create a Python 2.7 environment in the style transfer directory  
# Note that this is not python 2.7.9, which was the version instructed to use.  
#RUN virtualenv -p python2.7 env  
#RUN /bin/bash -c "source env/bin/activate \  
# && pip install scipy pillow tensorflow-gpu ffmpeg-normalize"  
# Build Anaconda environment  
RUN conda create -n style-transfer python=2.7.9  
RUN /bin/bash -c "source activate style-transfer \  
&& conda install -c conda-forge tensorflow=0.11.0 \  
&& conda install scipy pillow"  
  
# Run setup.py to extract training code  
RUN cd /root/fast-style-transfer/ && sudo ./setup.sh  

