###########################################################  
# MXNET compilation on official nvidia/cuda:7.5-cudnn4-devel image.  
# cuDNN is enabled  
###########################################################  
  
FROM nvidia/cuda:7.5-cudnn4-devel  
MAINTAINER Pankaj Goyal <pankajgoyal3010@gmail.com>  
  
# Install project dependencies  
RUN apt-get update &&\  
apt-get install -y \  
libopenblas-dev \  
libatlas-base-dev \  
libopencv-dev \  
python-dev \  
python-numpy \  
python-setuptools \  
git &&\  
# cleanup of package manager  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/lib/libcuda.so  
  
# MXNET build and install  
RUN git clone --recursive https://github.com/dmlc/mxnet &&\  
cd mxnet &&\  
# Copy config.mk  
cp make/config.mk config.mk &&\  
# Set CUDA flag  
sed -i 's/USE_CUDA = 0/USE_CUDA = 1/g' config.mk &&\  
sed -i 's/USE_CUDA_PATH = NONE/USE_CUDA_PATH = \/usr\/local\/cuda/g' config.mk
&&\  
# Make  
make -j"$(nproc)"  
  
# Install  
ENV PYTHONPATH=/mxnet/python:/usr/local/lib/python2.7/site-packages  

