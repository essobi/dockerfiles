FROM ubuntu:14.10  
MAINTAINER Soonwoong Lee <soonwoong.lee@gmail.com>  
  
RUN apt-get update && apt-get install -y git unzip openssh-server python-
software-properties software-properties-common protobuf-compiler build-
essential python-dev python-pip  
  
# Install wget and build-essential  
RUN apt-get update && apt-get install -y build-essential wget  
  
# Install sshd  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# CUDA version - as the kernel is shared the host and container must
correspond  
ENV CUDA_MAJOR=7.0 \  
CUDA_VERSION=7.0.28 \  
CUDA_MAJOR_U=7_0  
  
# Change to the /tmp directory  
RUN \  
cd /tmp && \  
# Download run file  
wget
http://developer.download.nvidia.com/compute/cuda/${CUDA_MAJOR_U}/Prod/local_installers/cuda_${CUDA_VERSION}_linux.run
&& \  
# Make the run file executable and extract  
chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \  
# Install CUDA drivers (silent, no kernel)  
./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
# Install toolkit (silent)  
./cuda-linux64-rel-*.run -noprompt && \  
# Clean up  
rm -rf *  
  
# Add to path  
ENV PATH /usr/local/cuda/bin:${PATH}  
  
# Configure dynamic link  
RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf && ldconfig  
  
# Install git, bc and dependencies  
RUN \  
apt-get update && apt-get install -y \  
git \  
bc \  
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
gfortran \  
python-numpy \  
python-scipy  
  
# Clone Caffe repo and move into it  
RUN \  
cd root && git clone https://github.com/BVLC/caffe.git && cd caffe && \  
# Copy Makefile  
cp Makefile.config.example Makefile.config && \  
# Make  
make -j"$(nproc)" all  
# Set ~/caffe as working directory  
# Make pycaffe  
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
RUN pip install python-dateutil>=1.4  
RUN pip install protobuf>=2.5.0  
RUN pip install python-gflags>=2.0  
RUN pip install pyyaml>=3.10  
RUN pip install Pillow>=2.3.0  
  
RUN cd /root/caffe && \  
make pycaffe && \  
make distribute  
  
# Set ~/caffe as working directory  
WORKDIR /root/caffe  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

