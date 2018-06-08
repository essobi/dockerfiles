FROM nvidia/cuda:8.0-cudnn5-devel  
  
#RUN echo -e "\n**********************\nNVIDIA Driver
Version\n**********************\n" && \  
# cat /proc/driver/nvidia/version && \  
# echo -e "\n**********************\nCUDA Version\n**********************\n"
&& \  
# nvcc -V && \  
# echo -e "\n\nBuilding your Deep Learning Docker Image...\n"  
  
# Install some dependencies  
RUN apt-get update && apt-get install -y \  
bc \  
build-essential \  
cmake \  
curl \  
g++ \  
gfortran \  
git \  
libffi-dev \  
libfreetype6-dev \  
libhdf5-dev \  
libjpeg-dev \  
liblcms2-dev \  
libopenblas-dev \  
liblapack-dev \  
libopenjpeg2 \  
libpng12-dev \  
libssl-dev \  
libtiff5-dev \  
libwebp-dev \  
libzmq3-dev \  
nano \  
pkg-config \  
python-dev \  
software-properties-common \  
unzip \  
vim \  
wget \  
zlib1g-dev \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
# Link BLAS library to use OpenBLAS using the alternatives mechanism
(https://www.scipy.org/scipylib/building/linux.html#debian-ubuntu)  
update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3  
  
##  
WORKDIR "/root"  
CMD ["/bin/bash"]  

