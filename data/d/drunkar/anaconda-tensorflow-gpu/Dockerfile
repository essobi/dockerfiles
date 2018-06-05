# Trnsorflow r0.11  
# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5  
# Requires CUDA toolkit 7.5 and CuDNN v5.  
  
FROM ubuntu:16.04  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
# locale for tokyo  
RUN apt-get update && \  
apt-get -y install tzdata locales && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# enable apt multiverse repository  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository multiverse  
  
# Disable frontend  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install wget and build-essential  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
linux-generic \  
nvidia-cuda-toolkit \  
nvidia-361  
  
##############################################################################  
# cuDNN 7.5  
##############################################################################  
ADD cuDNN_path.txt ./  
RUN . ./cuDNN_path.txt && wget -q ${CUDNN_PATH} -O cudnn.tgz && \  
tar xzf cudnn.tgz && \  
cp -a cuda/lib64/* /usr/local/lib/ && \  
cp -a cuda/include/* /usr/local/include/ && \  
ldconfig && \  
rm -R -f cuda cudnn.tgz cuDNN_path.txt  
  
##############################################################################  
# anaconda python  
##############################################################################  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh && \  
/bin/bash Anaconda3-4.4.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda3-4.4.0-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
RUN pip install --upgrade pip  
  
# for jupyter notebook  
EXPOSE 8888  
  
##############################################################################  
# tensorflow  
##############################################################################  
ENV
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc0-cp35-cp35m-linux_x86_64.whl  
RUN pip install --upgrade -I setuptools  
RUN pip install --upgrade $TF_BINARY_URL  
  
EXPOSE 6006  
  
##############################################################################  
# settings  
##############################################################################  
RUN mkdir /notebook  
VOLUME ["/notebook"]  
  
ENTRYPOINT jupyter notebook --no-browser --ip="0.0.0.0" --port=8888
--notebook-dir="/notebook"  
WORKDIR /notebook  

