FROM debian:7.9  
  
MAINTAINER Eric Dill <edill@bnl.gov>  
  
RUN apt-get update  
RUN apt-get install -y autoconf \  
build-essential \  
bzip2 \  
gcc \  
g++ \  
git \  
make \  
patch \  
tar \  
wget \  
zlib1g-dev \  
libreadline6-dev \  
libglib2.0-0 \  
libxext6 libxext-dev \  
libxrender1 libxrender-dev \  
libsm6 libsm-dev \  
tk-dev \  
libx11-6 libx11-dev \  
# gobject-introspection  
flex \  
# install extra packages for gobject-introspection package  
libffi-dev \  
libssl-dev \  
bison \  
# install packages for hkl  
gtk-doc-tools  
  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
--no-verbose && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && rm Miniconda*.sh &&
\  
export PATH=/opt/conda/bin:$PATH && \  
conda config --set show_channel_urls True && \  
conda config --set always_yes True && \  
conda update conda && \  
conda install conda-build anaconda-client && \  
conda clean -t -p  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales &&
locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  

