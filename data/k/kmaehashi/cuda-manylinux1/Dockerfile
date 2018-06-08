FROM quay.io/pypa/manylinux1_x86_64  
  
###  
### https://gitlab.com/nvidia/cuda/raw/centos6/8.0/runtime/Dockerfile  
###  
RUN
NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
&& \  
curl -fsSL
https://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/7fa2af80.pub
| sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \  
echo "$NVIDIA_GPGKEY_SUM /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c -  
  
COPY cuda.repo /etc/yum.repos.d/cuda.repo  
  
ENV CUDA_VERSION 8.0.61  
ENV CUDA_PKG_VERSION 8-0-$CUDA_VERSION-1  
RUN yum install -y \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-nvgraph-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-8-0-8.0.61.2-1 \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-8.0 /usr/local/cuda && \  
rm -rf /var/cache/yum/*  
  
# nvidia-docker 1.0  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64  
  
# nvidia-container-runtime  
ENV NVIDIA_VISIBLE_DEVICES all  
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility  
ENV NVIDIA_REQUIRE_CUDA "cuda>=8.0"  
###  
### https://gitlab.com/nvidia/cuda/raw/centos6/8.0/devel/Dockerfile  
###  
RUN yum install -y \  
cuda-core-$CUDA_PKG_VERSION \  
cuda-misc-headers-$CUDA_PKG_VERSION \  
cuda-command-line-tools-$CUDA_PKG_VERSION \  
cuda-license-$CUDA_PKG_VERSION \  
cuda-nvrtc-dev-$CUDA_PKG_VERSION \  
cuda-nvml-dev-$CUDA_PKG_VERSION \  
cuda-nvgraph-dev-$CUDA_PKG_VERSION \  
cuda-cusolver-dev-$CUDA_PKG_VERSION \  
cuda-cublas-dev-8-0-8.0.61.2-1 \  
cuda-cufft-dev-$CUDA_PKG_VERSION \  
cuda-curand-dev-$CUDA_PKG_VERSION \  
cuda-cusparse-dev-$CUDA_PKG_VERSION \  
cuda-npp-dev-$CUDA_PKG_VERSION \  
cuda-cudart-dev-$CUDA_PKG_VERSION \  
cuda-driver-dev-$CUDA_PKG_VERSION && \  
rm -rf /var/cache/yum/*  
  
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs:${LIBRARY_PATH}  
  
###  
### https://gitlab.com/nvidia/cuda/raw/centos6/8.0/devel/cudnn7/Dockerfile  
###  
ENV CUDNN_VERSION 7.0.5.15  
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"  
  
# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement  
RUN
CUDNN_DOWNLOAD_SUM=9e0b31735918fe33a79c4b3e612143d33f48f61c095a3b993023cdab46f6d66e
&& \  
curl -fsSL
http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-8.0-linux-x64-v7.tgz
-O && \  
echo "$CUDNN_DOWNLOAD_SUM cudnn-8.0-linux-x64-v7.tgz" | sha256sum -c - && \  
tar --no-same-owner -xzf cudnn-8.0-linux-x64-v7.tgz -C /usr/local && \  
rm cudnn-8.0-linux-x64-v7.tgz && \  
ldconfig  

