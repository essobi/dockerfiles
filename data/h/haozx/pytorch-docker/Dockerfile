FROM nvidia/cuda:9.1-cudnn7-runtime-ubuntu16.04  
  
LABEL maintainer="haozx"  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
software-properties-common \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
RUN pip3 \--no-cache-dir install \  
Pillow \  
h5py \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
scipy \  
sklearn \  
pyyaml \  
&& \  
python3 -m ipykernel.kernelspec  
  
# Install TensorFlow GPU version.  
RUN pip3 \--no-cache-dir install \  
http://download.pytorch.org/whl/cu91/torch-0.3.1-cp35-cp35m-linux_x86_64.whl
&& \  
pip3 \--no-cache-dir install torchvision  
  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
CMD ["/bin/bash"]  

