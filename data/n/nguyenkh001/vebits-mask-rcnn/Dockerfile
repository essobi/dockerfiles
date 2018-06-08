FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
# install debian packages  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Complete setup for nvidia-docker requirements  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
# install essentials and build dependencies  
build-essential \  
autotools-dev \  
cmake \  
curl \  
git \  
g++ \  
git \  
gfortran-multilib \  
libavcodec-dev \  
libavformat-dev \  
libjasper-dev \  
libjpeg-dev \  
libpng-dev \  
liblapacke-dev \  
libswscale-dev \  
libtiff-dev \  
pkg-config \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
rsync \  
software-properties-common \  
unzip \  
wget \  
zlib1g-dev \  
libffi-dev \  
# Protobuf  
ca-certificates \  
less \  
procps \  
vim-tiny \  
# install python 3  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
python3-virtualenv \  
python3-wheel \  
pkg-config \  
# requirements for numpy  
libopenblas-base \  
python3-numpy \  
python3-scipy \  
# requirements for keras  
python3-h5py \  
python3-yaml \  
python3-pydot \  
python3-tk \  
python3-matplotlib \  
python3-pillow \  
# For Kaldi  
automake \  
libtool \  
autoconf \  
subversion \  
# For Kaldi's dependencies  
libapr1 libaprutil1 libltdl-dev libltdl7 libserf-1-1 libsigsegv2 libsvn1 m4 \  
# For Java Bindings  
openjdk-8-jdk \  
# For SWIG  
libpcre3-dev \  
# For nano editor  
nano \  
&& apt-get install -y --allow-downgrades --no-install-recommends \  
libcudnn7=7.0.5.15-1+cuda9.0 \  
libcudnn7-dev=7.0.5.15-1+cuda9.0 \  
&& pip3 install --upgrade pip \  
&& pip --no-cache-dir install \  
Pillow==5.1.0 \  
h5py==2.7.1 \  
numpy==1.14.2 \  
pandas \  
cython==0.28.2 \  
opencv-python \  
tensorflow-gpu==1.5 \  
keras==2.1.6 \  
matplotlib \  
scipy \  
scikit-learn \  
imgaug \  
IPython[all] \  
&& ln -s /usr/bin/pip3 /usr/bin/pip \  
&& ln -s /usr/bin/python3 /usr/bin/python \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& jupyter-notebook --generate-config \  
&& echo "c = get_config()" >> /root/.jupyter/jupyter_notebook_config.py \  
&& echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py
\  
&& echo "c.NotebookApp.open_browser = False" >>
/root/.jupyter/jupyter_notebook_config.py \  
&& echo "c.NotebookApp.port = 8080" >>
/root/.jupyter/jupyter_notebook_config.py \  
&& echo "c.NotebookApp.password =
'sha1:d1a76026f118:82c006e5a506dd9c4c9f171050e3defaaca3a21e'" >>
/root/.jupyter/jupyter_notebook_config.py  
  
# For CUDA profiling, TensorFlow requires CUPTI  
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
ENV LD_LIBRARY_PATH /usr/local/cuda/bin:$LD_LIBRARY_PATH  
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:$LD_LIBRARY_PATH  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH  
  
  
# Allow UI display through host machine  
ENV QT_X11_NO_MITSHM 1  
# Expose port 8080 for Jupyter notebook  
EXPOSE 8080  

