FROM nvidia/cuda:9.0-devel-ubuntu16.04  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
# Installing dependencies  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update  
  
RUN apt-get update && \  
apt-get install -y \  
ocl-icd-libopencl1 \  
clinfo \  
python-software-properties \  
wget \  
git \  
python3-pip \  
python3 \  
xvfb \  
libxtst6 \  
openjdk-9-jre \  
cmake \  
libboost*  
  
RUN pip3 install snakemake pyyaml drmaa  
  
# Just in case installing OpenCL support  
RUN mkdir -p /etc/OpenCL/vendors && \  
echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \  
echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
# Defining ENV variables  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH /usr/local/cuda-9.0/lib64:/usr/lib/x86_64-linux-
gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
ENV NUM_JOBS 1  
# Downloading FIJI and scripts  
WORKDIR /opt/multiview  
RUN mkdir /data && \  
git clone https://github.com/mpicbg-scicomp/snakemake-workflows.git && \  
wget http://tomancak-srv1.mpi-
cbg.de/~schmied/workflow/2015-06-30_Fiji.app.tar.gz && \  
tar zxvf 2015-06-30_Fiji.app.tar.gz  
RUN git clone https://github.com/obmarg/libsysconfcpus.git  
RUN cd libsysconfcpus && \  
CFLAGS=-ansi ./configure && \  
make && \  
make install  
  
# Adding CUDA Fourier Library (not building inside the container as this is
not working, if someone finds a fix for this please make pull request !!!)  
ADD CUDA /opt/multiview/CUDA  
ADD FourierConvolutionCUDALib /opt/multiview/FourierConvolutionCUDALib  
  
# Going to the snakemake directory  
WORKDIR /opt/multiview/snakemake-workflows/spim_registration/timelapse/  
  
# SnakeMake command to launch the processing  
CMD snakemake -j $NUM_JOBS -d /data --verbose --cluster-config
/opt/multiview/snakemake-workflows/spim_registration/timelapse/cluster.json
--cluster ""  

