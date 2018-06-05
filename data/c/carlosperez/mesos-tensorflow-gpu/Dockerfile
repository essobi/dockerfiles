FROM ubuntu:16.04  
MAINTAINER Carlos Perez <carlos.perez@epfl.ch>  
  
####### SSH Daemon  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN mkdir ~/.ssh  
  
RUN echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAxP8lr3suohvNqTZyzqIud0YTAj9Z7vpqanAUy0EfGv3oeFmEaYPWr7psTyH7Zqo/wt/py/+XejmobextPSFUrPTgmrj7q9a2kEMXb9QIuhp9w4p0ARgOb3WHV6ulo37G/f4v3QOidCkYSJ0osOvVR9DTa2t32NtqKIy0q9FmKdxD8bUx1BxUdv1rzokzzQh6XNsGJRhtnTPc6FgIt9ClLRcgZDYx5MXUv6kRc0HuS5mGO6Py0GQEz50P3YB3vJEoejOuNykme+Vuj0R/kt/Sik8yR9Mev+pRpxViJAfCOIBnAyHzSIOmB7qQED1Q+nZruRHPXwDDq9grugjlf8Vi5Q==
carlos.perez@epfl.ch" >> ~/.ssh/authorized_keys  
  
RUN chmod 600 ~/.ssh/authorized_keys && chmod 700 ~/.ssh/  
####### SSH Daemon  
####### CUDA / CUDNN / GPU STUFF  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
RUN
NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
&& \  
NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \  
apt-key adv --fetch-keys
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
&& \  
apt-key adv --export \--no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 >
cudasign.pub && \  
echo "$NVIDIA_GPGKEY_SUM cudasign.pub" | sha256sum -c --strict - && rm
cudasign.pub && \  
echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" >
/etc/apt/sources.list.d/cuda.list  
  
ENV CUDA_VERSION 8.0  
LABEL com.nvidia.cuda.version="8.0"  
  
ENV CUDA_PKG_VERSION 8-0=8.0.44-1  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-nvgraph-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-$CUDA_PKG_VERSION \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-$CUDA_VERSION /usr/local/cuda && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/cuda/lib" >> /etc/ld.so.conf.d/cuda.conf && \  
echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cuda-core-$CUDA_PKG_VERSION \  
cuda-misc-headers-$CUDA_PKG_VERSION \  
cuda-command-line-tools-$CUDA_PKG_VERSION \  
cuda-nvrtc-dev-$CUDA_PKG_VERSION \  
cuda-nvml-dev-$CUDA_PKG_VERSION \  
cuda-nvgraph-dev-$CUDA_PKG_VERSION \  
cuda-cusolver-dev-$CUDA_PKG_VERSION \  
cuda-cublas-dev-$CUDA_PKG_VERSION \  
cuda-cufft-dev-$CUDA_PKG_VERSION \  
cuda-curand-dev-$CUDA_PKG_VERSION \  
cuda-cusparse-dev-$CUDA_PKG_VERSION \  
cuda-npp-dev-$CUDA_PKG_VERSION \  
cuda-cudart-dev-$CUDA_PKG_VERSION \  
cuda-driver-dev-$CUDA_PKG_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs:${LIBRARY_PATH}  
  
####### CUDA / CUDNN / GPU STUFF  
####### TENSORFLOW  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
Pillow \  
&& \  
python -m ipykernel.kernelspec  
  
ENV TENSORFLOW_VERSION 0.12.0-rc0  
  
# Install TensorFlow GPU version.  
RUN pip --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp27-none-
linux_x86_64.whl  
####### TENSORFLOW  
####### JUPYTER CONFIG + SAMPLES  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY /run_jupyter.sh /  
  
# Copy sample notebooks.  
COPY notebooks /notebooks  
  
WORKDIR "/notebooks"  
####### JUPYTER CONFIG + SAMPLES  

