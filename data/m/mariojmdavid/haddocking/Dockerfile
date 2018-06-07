# docker build -t haddocking .  
FROM ubuntu:16.04  
LABEL maintainer "Mario David <mariojmdavid@gmail.com>"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
gcc \  
git \  
libclfft-bin \  
libclfft-dev \  
libclfft2 \  
libffi-dev \  
libfftw3-double3 \  
libfftw3-single3 \  
libfftw3-long3 \  
libfftw3-dev \  
libxml2-dev \  
libxslt1-dev \  
module-init-tools \  
python \  
python-dev \  
python-pip \  
software-properties-common \  
tar \  
time \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip  
RUN pip install setuptools  
RUN pip install mako  
RUN pip install Cython  
RUN pip install matplotlib  
RUN pip install numpy  
RUN pip install scipy  
RUN pip install pyfftw  
RUN pip install pyopencl  
RUN cd /usr/include && \  
wget http://www.lip.pt/people/david/cl_include.tgz && \  
tar zxvf cl_include.tgz && \  
cd /tmp && \  
git clone https://github.com/geggo/gpyfft.git && \  
git clone https://github.com/haddocking/disvis.git && \  
git clone https://github.com/haddocking/powerfit.git  
  
RUN cd /tmp/gpyfft && \  
python setup.py install  
  
RUN cd /tmp/disvis && \  
python setup.py install  
  
RUN cd /tmp/powerfit && \  
python setup.py install  
  

