FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
MAINTAINER A.Rajagopal <rajagopal.abhejit@gmail.com>  
  
RUN apt-get -y update --fix-missing && \  
apt-get -y install --no-install-recommends --fix-missing \  
apt-utils \  
autoconf \  
automake \  
build-essential \  
ca-certificates \  
cmake \  
cpio \  
curl \  
dialog \  
gcc \  
gfortran \  
git \  
gpp \  
htop \  
libatlas-base-dev \  
libav-tools \  
libboost-all-dev \  
libncurses5-dev \  
libreadline-dev \  
locate \  
make \  
npm \  
pkg-config \  
python-dev \  
python-software-properties \  
sed \  
software-properties-common \  
tmux \  
unzip \  
vim \  
wget \  
zsh && \  
rm -rf /var/lib/apt/lists/*  
  
# a minimal anaconda installation  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /root/.bashrc && \  
curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN /opt/conda/bin/conda update -y conda && \  
/opt/conda/bin/conda config --prepend channels intel && \  
/opt/conda/bin/conda config --append channels conda-forge && \  
/opt/conda/bin/conda install -y intelpython3_core python=3 \  
beautifulsoup4 \  
bokeh \  
caffe-gpu \  
cython \  
gdal \  
geopandas \  
h5py \  
imageio \  
ipyparallel \  
ipython \  
jupyter \  
jupyter_contrib_nbextensions \  
jupyterhub \  
jupyterlab \  
jupyter_nbextensions_configurator \  
keras-gpu \  
lasagne \  
libiconv \  
mathjax \  
matplotlib \  
msgpack-python \  
nbpresent \  
networkx \  
numpy \  
opencv=3 \  
pandas \  
pillow \  
plotly \  
pyproj \  
pytorch-gpu \  
pyyaml \  
readline \  
requests \  
scikit-bio \  
scikit-image \  
scikit-learn \  
scikit-rf \  
scipy \  
scrapy \  
setuptools \  
six \  
sympy \  
tensorflow-gpu \  
theano \  
torchvision-gpu && \  
/opt/conda/bin/conda clean -tipsy  
  
# new packages usually make it to pip before conda, they can go here in that
case  
RUN /opt/conda/bin/pip install \  
overpass \  
pyrtl \  
sk-video  
  
RUN /opt/conda/bin/jupyter nbextension enable nbpresent --py && \  
/opt/conda/bin/jupyter serverextension enable nbpresent --py && \  
/opt/conda/bin/jupyter contrib nbextension install --symlink && \  
/opt/conda/bin/ipcluster nbextension enable && \  
/opt/conda/bin/jupyter serverextension enable --py jupyterlab  
  
ADD build_tensorflow.sh /root  
ADD test_tensorflow.py /root  

