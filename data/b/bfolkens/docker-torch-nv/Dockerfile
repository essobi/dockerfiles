FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
# Install some dep packages  
RUN apt-get update && \  
apt-get install -y git wget zip build-essential m4 libtool autoconf cmake && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install CUDA repo (needed for cuDNN)  
ENV CUDA_REPO_PKG=cuda-repo-ubuntu1404_8.0.61-1_amd64.deb  
RUN wget
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/$CUDA_REPO_PKG
&& \  
dpkg -i $CUDA_REPO_PKG  
  
# Install ML repo  
ENV ML_REPO_PKG=nvidia-machine-learning-repo-ubuntu1404_4.0-2_amd64.deb  
RUN wget http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1404/x86_64/$ML_REPO_PKG && \  
dpkg -i $ML_REPO_PKG  
  
# Install the nv packages  
RUN apt-get update && \  
apt-get install -y libcudnn5 libcudnn5-dev torch7-nv && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install NCCL for multi-GPU communication  
RUN cd /root && git clone https://github.com/NVIDIA/nccl.git && cd nccl && \  
make CUDA_HOME=/usr/local/cuda -j"$(nproc)" && \  
make PREFIX=/root/nccl install  
ENV LD_LIBRARY_PATH=/root/nccl/lib:$LD_LIBRARY_PATH  
RUN luarocks install nccl  
  
# Install more dev libs  
RUN luarocks install torch && \  
luarocks install nn && \  
luarocks install cutorch && \  
luarocks install cunn  

