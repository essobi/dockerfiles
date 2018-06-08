FROM nvidia/cuda:8.0-cudnn6-runtime-centos7  
RUN yum update -y \  
&& yum install -y \  
https://centos7.iuscommunity.org/ius-release.rpm \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
RUN yum install -y \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
rsync \  
software-properties-common \  
unzip \  
libcupti-dev \  
python36u \  
python36u-devel \  
python36u-pip \  
cuda-command-line-tools-8-0 \  
&& yum update -y \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
RUN pip3.6 install --no-cache-dir -U ipython pip setuptools  
RUN pip3.6 install --no-cache-dir tensorflow-gpu tensorflow  
  
ENV LD_LIBRARY_PATH
/usr/local/cuda-8.0/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
ENV CUDA_HOME /usr/local/cuda-8.0  

