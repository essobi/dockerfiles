# modified from tleyden5iwx/caffe-gpu-master  
# https://registry.hub.docker.com/u/tleyden5iwx/caffe-gpu-master/  
FROM delta2323/ubuntu-cuda  
  
ENV PYTHONPATH /opt/caffe/python  
  
# Add caffe binaries to path  
ENV PATH $PATH:/opt/caffe/.build_release/tools  
  
# Get dependencies  
RUN apt-get update && apt-get install -y \  
bc \  
cmake \  
curl \  
gcc-4.6 \  
g++-4.6 \  
gcc-4.6-multilib \  
g++-4.6-multilib \  
gfortran \  
git \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libboost-all-dev \  
libhdf5-serial-dev \  
liblmdb-dev \  
libjpeg62 \  
libfreeimage-dev \  
libatlas-base-dev \  
pkgconf \  
protobuf-compiler \  
python-dev \  
python-pip \  
unzip \  
wget  
  
# Use gcc 4.6  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.6 30 && \  
update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.6 30 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 30 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.6 30  
# Allow it to find CUDA libs  
RUN echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
# Clone the Caffe repo  
RUN cd /opt && git clone https://github.com/BVLC/caffe.git  
  
# Glog  
RUN cd /opt && wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz
&& \  
tar zxvf glog-0.3.3.tar.gz && \  
cd /opt/glog-0.3.3 && \  
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
RUN cd /opt/caffe && \  
cp Makefile.config.example Makefile.config && \  
\  
echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \  
sed -i 's/CXX :=/CXX ?=/' Makefile && \  
make all  
  
# Add ld-so.conf so it can find libcaffe.so  
ADD caffe-ld-so.conf /etc/ld.so.conf.d/  
  
# Run ldconfig again (not sure if needed)  
RUN ldconfig  
  
# Install python deps  
RUN cd /opt/caffe && \  
(for req in $(cat python/requirements.txt); do pip install $req; done) &&\  
easy_install numpy && \  
(for req in $(cat python/requirements.txt); do pip install $req; done) &&\  
easy_install pillow  
  
# Numpy include path hack - github.com/BVLC/caffe/wiki/Setting-up-Caffe-on-
Ubuntu-14.04  
RUN ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy
/usr/include/python2.7/numpy  
  
# Build Caffe python bindings  
RUN cd /opt/caffe && make pycaffe  
  
# Disable driver. This is workarou for error on libdc1394  
# This error happen when creating mnist data  
# See: http://stackoverflow.com/questions/12689304/ctypes-error-
libdc1394-error-failed-to-initialize-libdc1394/26028597#26028597  
RUN ln /dev/null /dev/raw1394  
  
# add caffe user  
RUN useradd -m -d /home/caffe -s /bin/bash caffe \  
&& echo "caffe:caffe" | chpasswd \  
&& mkdir /home/caffe/.ssh \  
&& chmod 700 /home/caffe/.ssh \  
&& chown -R caffe:caffe /home/caffe/.ssh  
RUN echo "caffe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN echo 'export PATH=$PATH:/opt/caffe/.build_release/tools' >>
/home/caffe/.bashrc  
RUN echo 'PYTHONPATH=$PYTHONPATH/opt/caffe/python' >> /home/caffe/.bashrc  
  
# various files are created by root. Change ownership  
RUN chown caffe:caffe -R /opt/caffe/  

