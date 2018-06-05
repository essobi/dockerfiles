FROM ubuntu:14.04  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
# locale for tokyo  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install wget and build-essential  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
doxygen doxygen-gui graphviz  
  
##############################################################################  
# anaconda python  
##############################################################################  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh && \  
/bin/bash Anaconda2-4.4.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda2-4.4.0-Linux-x86_64.sh && \  
/opt/conda/bin/conda install --yes conda==3.10.1  
  
ENV PATH /opt/conda/bin:$PATH  
  
# change default encoding  
RUN echo "import sys\n\  
sys.setdefaultencoding('utf-8')" >> /opt/conda/lib/python2.7/sitecustomize.py  
  
RUN pip install --default-timeout 6000 tornado pycrypto elasticsearch mysql-
python pydot graphviz  
  
##############################################################################  
# caffe-gpu lstm  
##############################################################################  
# Get dependencies  
RUN apt-get update && apt-get install -y \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libboost-all-dev \  
libhdf5-serial-dev \  
protobuf-compiler \  
gcc-4.8 \  
g++-4.8 \  
gcc-4.8-multilib \  
g++-4.8-multilib \  
gfortran \  
libjpeg62 \  
libfreeimage-dev \  
libatlas-base-dev \  
libopenblas-dev \  
git \  
bc \  
wget \  
curl \  
unzip \  
cmake \  
liblmdb-dev \  
pkgconf  
  
# Use gcc 4.8  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.8 30 && \  
update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.8 30 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 30 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 30  
  
# Clone the Caffe repo  
RUN cd /opt && git clone https://github.com/jeffdonahue/caffe.git  
RUN cd /opt/caffe && git checkout -b recurrent-rebase-cleanup
origin/recurrent-rebase-cleanup  
  
# Glog  
RUN cd /opt && wget https://github.com/google/glog/archive/v0.3.4.tar.gz -O
glog-0.3.4.tar.gz && \  
tar zxvf glog-0.3.4.tar.gz && \  
cd /opt/glog-0.3.4 && \  
./configure && \  
make && \  
make install  
  
# Workaround for error loading libglog:  
# error while loading shared libraries: libglog.so.0: cannot open shared
object file  
# The system already has /usr/local/lib listed in /etc/ld.so.conf.d/libc.conf,
so  
# running `ldconfig` fixes the problem (which is simpler than using
$LD_LIBRARY_PATH)  
# TODO: looks like this needs to be run _every_ time a new docker instance is
run,  
# so maybe LD_LIBRARY_PATh is a better approach (or add call to ldconfig in
~/.bashrc)  
RUN ldconfig  
  
# Gflags  
RUN cd /opt && \  
wget https://github.com/schuhschuh/gflags/archive/master.zip && \  
unzip master.zip && \  
cd /opt/gflags-master && \  
mkdir build && \  
cd /opt/gflags-master/build && \  
export CXXFLAGS="-fPIC" && \  
cmake .. && \  
make VERBOSE=1 && \  
make && \  
make install  
  
# Build Caffe core  
RUN cd /opt/caffe && cp Makefile.config.example Makefile.config  
RUN cd /opt/caffe && echo "CPU_ONLY := 1" >> Makefile.config  
RUN cd /opt/caffe && echo "CXX := /usr/bin/g++-4.8" >> Makefile.config  
RUN cd /opt/caffe && sed -i 's/CXX :=/CXX ?=/' Makefile  
RUN cd /opt/caffe && make all  
  
##############################################################################  
# pycaffe  
##############################################################################  
RUN pip install -r /opt/caffe/python/requirements.txt  
RUN echo "ANACONDA_HOME := /opt/conda" >> /opt/caffe/Makefile.config  
RUN echo 'PYTHON_INCLUDE := $(ANACONDA_HOME)/include
$(ANACONDA_HOME)/include/python2.7 $(ANACONDA_HOME)/lib/python2.7/site-
packages/numpy/core/include' >> /opt/caffe/Makefile.config  
RUN echo 'PYTHON_LIB := $(ANACONDA_HOME)/lib' >> /opt/caffe/Makefile.config  
RUN echo 'INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include' >>
/opt/caffe/Makefile.config  
RUN echo 'LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib' >>
/opt/caffe/Makefile.config  
RUN cd /opt/caffe && make pycaffe  
  
ENV PYTHONPATH /opt/caffe/python/:${PYTHONPATH}  
RUN echo "ln /dev/null /dev/raw1394" >> /etc/profile.d/caffeenv.sh  
  
##############################################################################  
# ipython notebook  
##############################################################################  
RUN ipython profile create nbserver  
# Configure "nbserver" profile  
RUN sed -i \  
-e "s/^# c.NotebookApp.ip = 'localhost'$/c.NotebookApp.ip = '0.0.0.0'/" \  
-e "s/^# c.NotebookApp.port = 8888$/c.NotebookApp.port = 8888/" \  
-e "s;^# c.NotebookApp.notebook_dir = '/.*'$;c.NotebookApp.notebook_dir = '/notebook';" \  
-e "s/^# c.NotebookApp.open_browser = True$/c.NotebookApp.open_browser = False/" \  
-e "s/^# c.IPKernelApp.matplotlib = None$/c.IPKernelApp.matplotlib = 'inline'/" \  
-e "s/^# c.IPKernelApp.extensions = \\[\\]$/c.IPKernelApp.extensions = ['version_information']/" \  
/root/.ipython/profile_nbserver/ipython_notebook_config.py  
  
EXPOSE 8888  
##############################################################################  
# settings  
##############################################################################  
# copy caffe example notebook  
RUN mkdir /notebook  
RUN mkdir /workspace  
VOLUME ["/workspace", "/notebook"]  
  
ENTRYPOINT bash /etc/profile.d/caffeenv.sh && ipython notebook
--profile=nbserver  
RUN cp /opt/caffe/examples/*ipynb /notebook/  
  
WORKDIR /notebook  

