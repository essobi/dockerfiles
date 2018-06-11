FROM wangjianyong/jupyter  
MAINTAINER Jianyong Wang <wangjianyongscu@gmail.com>  
ENV REFRESHED_AT 2016-05-05  
  
#############  
RUN apt-get update && apt-get install -y \  
git \  
libopenblas-dev \  
libopencv-dev \  
python-dev \  
python-numpy \  
python-setuptools  
  
# install the core library  
# Clone MXNet repo and move into it  
RUN cd /root && git clone --recursive https://github.com/dmlc/mxnet && cd
mxnet && \  
# Copy config.mk  
cp make/config.mk config.mk && \  
# Set OpenBLAS  
sed -i 's/USE_BLAS = atlas/USE_BLAS = openblas/g' config.mk && \  
# Make  
make -j"$(nproc)"  
# Install Python package  
RUN cd /root/mxnet/python && python setup.py install  
#############  
  
# graphviz ensures the visualization of mx.viz.plot_network in ipython
notebook  
RUN apt-get install -y python-numpy wget unzip graphviz  
ENV MXNET_EXEC_INPLACE_GRAD_SUM_CAP 512000000  
RUN pip install graphviz

