# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
#  
# heavily modified by Charless Fowlkes <fowlkes@ics.uci.edu> (c) 2017  
#  
#  
# base container for BigDIPA short course that includes NVIDIA and OpenCL
configuration  
#  
# based on version of notebook image that includes start-singleuser.sh script  
FROM jupyter/scipy-notebook:ae885c0a6226  
  
# install nvidia environment for GPU access  
# based on 8.0-runtime-ubuntu16.04 + 8.0-devel + 8.0-cudnn6  
USER root  
RUN echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" >
/etc/apt/sources.list.d/cuda.list  
RUN echo "deb http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list  
RUN apt-key adv --fetch-keys
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub  
RUN NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \  
apt-key adv --export \--no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 >
cudasign.pub  
RUN rm cudasign.pub  
  
#RUN
NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
&& \  
# echo "$NVIDIA_GPGKEY_SUM cudasign.pub" | sha256sum -c --strict - && rm
cudasign.pub \  
# TODO: checksum is failing here, find out new checksum  
RUN apt-get update  
  
ENV CUDA_VERSION 8.0.61  
ENV CUDNN_VERSION 6.0.21  
ENV NVIDIA_CUDA_VERSION $CUDA_VERSION  
ENV NVIDIA_VISIBLE_DEVICES all  
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility  
ENV CUDA_PKG_VERSION 8-0=$CUDA_VERSION-1  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64  
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs:${LIBRARY_PATH}  
  
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"  
  
RUN apt-get install -y --no-install-recommends \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-nvgraph-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-8-0=8.0.61.2-1 \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-8.0 /usr/local/cuda  
  
RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && ldconfig  
  
# /usr/local/nvidia is volume provided by docker with all  
# the driver specific binaries culled from the container host  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
#  
# add in CUDA devel libraries  
#  
RUN apt-get install -y --no-install-recommends \  
cuda-core-$CUDA_PKG_VERSION \  
cuda-misc-headers-$CUDA_PKG_VERSION \  
cuda-command-line-tools-$CUDA_PKG_VERSION \  
cuda-nvrtc-dev-$CUDA_PKG_VERSION \  
cuda-nvml-dev-$CUDA_PKG_VERSION \  
cuda-nvgraph-dev-$CUDA_PKG_VERSION \  
cuda-cusolver-dev-$CUDA_PKG_VERSION \  
cuda-cublas-dev-8-0=8.0.61.2-1 \  
cuda-cufft-dev-$CUDA_PKG_VERSION \  
cuda-curand-dev-$CUDA_PKG_VERSION \  
cuda-cusparse-dev-$CUDA_PKG_VERSION \  
cuda-npp-dev-$CUDA_PKG_VERSION \  
cuda-cudart-dev-$CUDA_PKG_VERSION \  
cuda-driver-dev-$CUDA_PKG_VERSION  
  
#  
# install cudnn 6  
#  
RUN apt-get install -y --no-install-recommends \  
libcudnn6=$CUDNN_VERSION-1+cuda8.0 \  
libcudnn6-dev=$CUDNN_VERSION-1+cuda8.0  
  
#  
# install OpenCL  
#  
# remove nividia libOpenCL which isn't compatable with pyopencl  
RUN rm /usr/local/cuda-8.0/targets/x86_64-linux/lib/libOpenCL.so  
RUN rm /usr/local/cuda-8.0/targets/x86_64-linux/lib/libOpenCL.so.1  
RUN rm /usr/local/cuda-8.0/targets/x86_64-linux/lib/libOpenCL.so.1.0  
RUN rm /usr/local/cuda-8.0/targets/x86_64-linux/lib/libOpenCL.so.1.0.0  
  
# opencl for intel processor  
RUN apt-get install -y --no-install-recommends libffi-dev ocl-icd-opencl-dev
clinfo  
COPY opencl/opencl-1.2-intel-cpu_6.4.0.25-2_amd64.deb /tmp/  
COPY opencl/opencl-1.2-base_6.4.0.25-2_amd64.deb /tmp/  
RUN dpkg -i /tmp/opencl-1.2-base_6.4.0.25-2_amd64.deb &&\  
dpkg -i /tmp/opencl-1.2-intel-cpu_6.4.0.25-2_amd64.deb&&\  
rm -f /tmp/opencl-1.2-intel-cpu_6.4.0.25-2_amd64.deb &&\  
rm -f /tmp/opencl-1.2-base_6.4.0.25-2_amd64.deb&&\  
mkdir -p /etc/OpenCL/vendors &&\  
ln /opt/intel/opencl-1.2-6.4.0.25/etc/intel64.icd
/etc/OpenCL/vendors/intel64.icd &&\  
echo "libnvidia-opencl.so.1" >> /etc/OpenCL/vendors/nvidia.icd  
  
RUN echo "/opt/intel/opencl-1.2-6.4.0.25/lib64/clinfo" >>
/etc/ld.so.conf.d/intelOpenCL.conf &&\  
ldconfig  
  
# cleanup apt leftovers  
RUN rm -rf /var/lib/apt/lists/*  
  

