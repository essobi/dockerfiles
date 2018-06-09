FROM kaixhin/caffe  
MAINTAINER Tingting Lu <tingtinglu@buaa.edu.cn> #  
# Install git, python-dev, pip and other dependencies  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
python-nose \  
python-scipy \  
subversion \  
wget \  
bc \  
cmake \  
libatlas-dev \  
libboost-all-dev \  
libprotobuf-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
protobuf-compiler \  
libhdf5-dev \  
libleveldb-dev \  
liblmdb-dev \  
libsnappy-dev \  
python-pip \  
python-setuptools \  
emacs24-nox \  
graphviz \  
gfortran > /dev/null  
  
# Theano  
# ------  
# Install bleeding-edge Theano  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
  
# Install scikit-learn, jupyter, pydotplus for caffe visualization, seaborn  
RUN pip install scikit-learn jupyter lasagne keras pydotplus seaborn  
  
# MXNet  
# -----  
# Install mxnet  
RUN cd /root && git clone \--recursive https://github.com/dmlc/mxnet && cd
mxnet && \  
# Copy config.mk  
cp make/config.mk config.mk && \  
# Set OpenBLAS  
sed -i 's/USE_BLAS = atlas/USE_BLAS = openblas/g' config.mk && \  
# Make  
make -j"$(nproc)"  
RUN cd /root/mxnet/python && python setup.py install  
# Add R to apt sources  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
# Install latest version of R  
RUN apt-get update && apt-get install -y --force-yes r-base  
  
# Jupyter  
# -------  
# Configure jupyter, set up password  
RUN jupyter notebook --generate-config  
RUN echo "c.NotebookApp.password =
u'sha1:30d3f970641a:ab54d7ab6578d8543778848fe86227534109ba13'" >>
~/.jupyter/jupyter_notebook_config.py  
  
WORKDIR /root  
EXPOSE 8888  
ENTRYPOINT jupyter notebook --ip=0.0.0.0  

