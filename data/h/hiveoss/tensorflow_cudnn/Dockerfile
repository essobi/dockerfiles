FROM ubuntu:14.04  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
ENV NVIDIA_GPGKEY_SUM
bd841d59a27a406e513db7d405550894188a4c1cd96bf8aa4f82f1b39e0b5c1c  
ENV NVIDIA_GPGKEY_FPR 889bee522da690103c4b085ed88c3d385c37d3be  
  
RUN apt-key adv --fetch-keys
http://developer.download.nvidia.com/compute/cuda/repos/GPGKEY && \  
apt-key adv --export \--no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +2 >
cudasign.pub && \  
echo "$NVIDIA_GPGKEY_SUM cudasign.pub" | sha256sum -c --strict - && rm
cudasign.pub && \  
echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64 /" >
/etc/apt/sources.list.d/cuda.list  
  
ENV CUDA_VERSION 7.5  
LABEL com.nvidia.cuda.version="7.5"  
  
ENV CUDA_PKG_VERSION 7-5=7.5-18  
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes \  
curl \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
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
  
# Set up our notebook config.  
WORKDIR /usr/local/  
RUN curl
http://developer.download.nvidia.com/compute/redist/cudnn/v4/cudnn-7.0-linux-x64-v4.0-prod.tgz
-O  
RUN tar xvzf cudnn-7.0-linux-x64-v4.0-prod.tgz  
RUN chmod a+r /usr/local/cuda/lib64/libcudnn*  
RUN export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"  
RUN export CUDA_HOME=/usr/local/cuda  
  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python-numpy \  
python-pip \  
python-scipy \  
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
sklearn \  
&& \  
python -m ipykernel.kernelspec  
  
# Install TensorFlow GPU version.  
ENV TENSORFLOW_VERSION 0.8.0  
RUN pip --no-cache-dir install \  
http://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
RUN rm -rf /notebooks/*  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh"]  

