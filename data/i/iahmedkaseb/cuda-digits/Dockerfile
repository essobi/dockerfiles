# Start with the CUDA base image.  
FROM iahmedkaseb/cuda  
MAINTAINER Ahmed S. Kaseb <akaseb@purdue.edu>  
  
# Update and install dependencies.  
RUN apt-get update && apt-get install -y \  
git \  
# Caffe Dependencies:  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libhdf5-serial-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
liblmdb-dev \  
protobuf-compiler \  
libatlas-base-dev \  
libboost-all-dev \  
python-pip \  
gfortran \  
# DIGITS Dependencies:  
graphviz  
  
# Build NVIDIA's Caffe.  
RUN cd /root && \  
# Clone NVIDIA's Caffe.  
git clone --branch v0.11.0 https://github.com/NVIDIA/caffe.git && \  
cd caffe && \  
# Install python dependencies.  
for req in $(cat python/requirements.txt); do pip install $req; done && \  
# Prepare the configuration and disable cuDNN.  
cp Makefile.config.example Makefile.config && \  
sed -i 's/USE_CUDNN/# USE_CUDNN/g' Makefile.config && \  
# Build NVIDIA's Caffe.  
make -j"$(nproc)" all && \  
make -j"$(nproc)" py  
  
# Set the Caffe environment variable.  
ENV CAFFE_HOME /root/caffe  
  
# Clone DIGITS and install python dependencies.  
RUN cd /root && \  
git clone https://github.com/NVIDIA/DIGITS.git digits && \  
for req in $(cat digits/requirements.txt); do pip install $req; done  
  
# Expose the server port.  
EXPOSE 8080  
# Set the working directory.  
WORKDIR /root/digits  
  
# Start the server.  
CMD ["/root/digits/digits-server"]  

