# Use images provided by Nvida with CUDA and CUDNN preinstalled  
FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04  
# These are apparently tensorflow deps  
RUN apt-get update && apt-get install -y --no-install-recommends \  
netbase \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
python3-pip \  
libcupti-dev \  
rsync \  
software-properties-common \  
unzip \  
libgtk2.0-0 \  
git \  
tcl-dev \  
tk-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Upgrade pip and install setuptools  
RUN pip3 install --upgrade pip setuptools  
  
# Install scipy packages and some utils  
RUN pip3 install --no-cache-dir numpy \  
sklearn \  
Pillow \  
eventlet \  
Flask \  
python-socketio \  
moviepy \  
scipy \  
opencv-python \  
matplotlib \  
ipython \  
jupyter \  
pandas \  
sympy \  
nose \  
h5py  
  
# Install tensorflow with GPU support and keras  
RUN pip3 install --no-cache-dir tensorflow-gpu keras  
  
# Setup our workdir  
RUN mkdir /src  
WORKDIR "/src"  
# For CUDA profiling, TensorFlow requires CUPTI.  
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
# TensorBoard  
EXPOSE 6006  
# Flask Server  
EXPOSE 4567  
# Jupyter notebook  
EXPOSE 8888  

