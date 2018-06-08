FROM ubuntu:14.04  
ENV CUDA_RUN
http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-
repo-ubuntu1404-7-5-local_7.5-18_amd64.deb  
#RUN ping 8.8.8.8  
RUN apt-get install -y \  
wget  
  
RUN apt-get -y install dialog apt-utils  
  
RUN cd /opt && \  
wget $CUDA_RUN && \  
dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb && \  
apt-get update  
  
  
ENV LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-7.5/lib64  
ENV PATH=$PATH:/usr/local/cuda-7.5/bin  
  
  
#ENV MATLAB_INSTALLER http://www.ru  
#RUN cd ~ && \  
# wget $MATLAB_INSTALLER && \\#  
# unzip matlab.zip && \  
# cd matlab && \  
# ./linux_install && \  
# cd .. && rm -rf matlab*  
RUN apt-get install -y -q --no-install-recommends\  
bc \  
cmake \  
curl \  
gcc\  
g++ \  
gcc-multilib \  
g++-multilib \  
gfortran \  
git \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libboost-all-dev \  
libhdf5-serial-dev \  
libjpeg62 \  
libfreeimage-dev \  
libatlas-base-dev \  
libboost-all-dev \  
pkgconf \  
protobuf-compiler \  
python-dev \  
python-pip \  
unzip \  
wget \  
libgflags-dev \  
libgoogle-glog-dev \  
liblmdb-dev\  
libhdf5-dev \  
python-pip \  
python-dev \  
build-essential \  
nginx \  
cuda \  
python-numpy  
  
RUN pip install tornado  
RUN pip install flask  
RUN pip install supervisor  
RUN pip install pillow  
  
RUN update-rc.d nginx defaults  
  
#RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 30 && \  
# update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++ 30 && \  
# update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc 30 && \  
# update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++ 30  
RUN echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
  
RUN apt-get install -y -q make  
#RUN cd /tmp && \  
# wget http://github.com/xianyi/OpenBLAS/archive/v0.2.14.tar.gz && \  
# tar -xzf v0.2.14.tar.gz && cd OpenBLAS-0.2.14/ && \  
# make FC=gfortran USE_OPENMP=1 && \  
# make PREFIX=/opt/openblas install  
#RUN cd /tmp && \  
# wget http://deepdocker.cloudapp.net/cudnn-7.0-linux-x64-v3.0-prod.tgz &&\  
# tar -xzf cudnn-7.0-linux-x64-v3.0-prod.tgz && \  
# cp cuda/include/* /usr/local/cuda/include && \  
# cp cuda/lib64/* /usr/local/cuda/lib64  
RUN cd /opt && git clone https://github.com/BVLC/caffe.git && cd caffe  
ADD Makefile.config /opt/caffe/  
#RUN cd /opt/caffe && ls -laX  
#RUN cd /opt/caffe && make -j"$(nproc)" all #\  
# make -j"$(nproc)" matcaffe  
RUN cd /opt/caffe/python && \  
for req in $(cat requirements.txt); do pip install $req; done && \  
cd ..  
  
ENV PYTHONPATH /opt/caffe/python  
ENV PATH $PATH:/opt/caffe/.build_release/tools  
ADD caffe-ld-so.conf /etc/ld.so.conf.d/  
RUN ldconfig  
  
RUN cd /opt/caffe && \  
(pip install -r python/requirements.txt; easy_install numpy; pip install -r
python/requirements.txt) && easy_install pillow  
  
  
#RUN NUMPY_EGG=`ls /usr/local/lib/python2.7/dist-packages | grep -i numpy` &&
\ ln -s /usr/local/lib/python2.7/dist-
packages/$NUMPY_EGG/numpy/core/include/numpy /usr/include/python2.7/numpy  
RUN cd /tmp && \  
wget http://deepdocker.cloudapp.net/cudnn-7.0-linux-x64-v3.0-prod.tgz &&\  
tar -xzf cudnn-7.0-linux-x64-v3.0-prod.tgz && \  
cp cuda/include/* /usr/local/cuda/include && \  
cp cuda/lib64/* /usr/local/cuda/lib64 &&\  
rm -rf cuda && rm cudnn-7.0-linux-x64-v3.0-prod.tgz  
  
RUN cd /opt/caffe && make -j"$(nproc)" pycaffe && make -j"$(nproc)" all  
RUN rm /opt/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb  

