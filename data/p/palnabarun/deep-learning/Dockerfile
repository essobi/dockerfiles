FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
  
MAINTAINER Nabarun Pal <pal.nabarun95@gmail.com>  
  
RUN apt update && apt install -y \  
build-essential \  
cmake \  
curl \  
g++ \  
gcc \  
gfortran \  
vim \  
wget \  
unzip \  
libhdf5-dev \  
libjpeg-dev \  
libpng12-dev \  
libssl-dev \  
libtiff5-dev \  
libwebp-dev \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt update && apt install -y \  
python3 \  
python3-dev \  
python3-pip \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt update && apt install -y \  
python3-numpy \  
python3-scipy \  
python3-sklearn \  
python3-skimage \  
python3-matplotlib \  
python3-sympy \  
python3-pandas \  
python3-h5py \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 --no-cache-dir install --upgrade ipython && \  
pip3 --no-cache-dir install \  
Cython \  
ipykernel \  
jupyter \  
&& \  
python3 -m ipykernel.kernelspec  
  
RUN pip3 install tensorflow-gpu  
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64/:/usr/local/cuda-8.0/lib64/  
ENV CUDA_HOME=/usr/local/cuda  
# trick to help tensorflow find libcudnn. Probably not a good way to do this.
Will file a GH issue for this.  
RUN cp /usr/lib/x86_64-linux-gnu/libcudnn.so.6.0.21
/usr/local/cuda-8.0/lib64/libcudnn.so.5  
  
RUN pip3 install keras  
  
#COPY notebooks notebooks/  
COPY jupyter_notebook_config.py /root/.jupyter/  
# Jupyter has issues with being run directly:
https://github.com/ipython/ipython/issues/7062  
COPY run_jupyter.sh /  
  
EXPOSE 6006 8888  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh", "--allow-root"]  

