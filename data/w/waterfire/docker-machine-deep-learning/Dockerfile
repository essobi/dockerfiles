FROM ubuntu:16.04  
MAINTAINER VAN TIEN <to tienhoangvan@gmail.com>  
  
ARG THEANO_VERSION=rel-0.8.2  
ARG TENSORFLOW_VERSION=0.12.1  
ARG TENSORFLOW_ARCH=cpu  
ARG KERAS_VERSION=1.2.0  
ARG LASAGNE_VERSION=v0.1  
ARG TORCH_VERSION=latest  
ARG CAFFE_VERSION=master  
  
# Install some dependencies  
RUN apt-get update && apt-get install wget -y && wget
https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  
RUN apt install bzip2 -y # for decompress miniconda  
  
RUN bash Miniconda2-latest-Linux-x86_64.sh —b f -p ~/miniconda  
RUN echo 'export PATH=“~/miniconda/bin:$PATH"' >> ~/.bashrc  
RUN source .bashrc  
RUN rm Miniconda2-latest-Linux-x86_64.sh  
  
# tensorflow  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN conda install -y \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
pandas \  
Pillow \  
&& \  
python -m ipykernel.kernelspec  
RUN pip --no-cache-dir install tensorflow  
  
# install caffee: https://yangcha.github.io/Caffe-Conda/  
RUN conda install -c menpo opencv3  
  
RUN apt-get install -y build-essential cmake git pkg-config  
  
RUN apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev protobuf-
compiler  
  
RUN apt-get install -y libatlas-base-dev  
  
RUN apt-get install -y --no-install-recommends libboost-all-dev  
  
RUN apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev  
  
RUN conda install cython scikit-image ipython h5py nose pandas protobuf pyyaml
jupyter -y  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
wget \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
rm -rf /var/lib/apt/lists/*  
  
#  
RUN conda install -y numpy scipy nose h5py skimage matplotlib pandas sklearn
sympy  
  
############  
# Add SNI support to Python  
RUN pip --no-cache-dir install \  
pyopenssl \  
ndg-httpsclient \  
pyasn1  
  
# Install other useful Python packages using pip  
RUN pip --no-cache-dir install --upgrade ipython && \  
pip --no-cache-dir install \  
Cython \  
ipykernel \  
jupyter \  
path.py \  
Pillow \  
pygments \  
six \  
sphinx \  
wheel \  
zmq \  
&& \  
python -m ipykernel.kernelspec  
  
# Install TensorFlow  
RUN pip --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_ARCH}/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
  
# Install dependencies for Caffe  
RUN apt-get update && apt-get install -y \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Caffe  
RUN git clone -b ${CAFFE_VERSION} \--depth 1 https://github.com/BVLC/caffe.git
/root/caffe && \  
cd /root/caffe && \  
cat python/requirements.txt | xargs -n1 pip install && \  
mkdir build && cd build && \  
cmake -DCPU_ONLY=1 -DBLAS=Open .. && \  
make -j"$(nproc)" all && \  
make install  
  
# Set up Caffe environment variables  
ENV CAFFE_ROOT=/root/caffe  
ENV PYCAFFE_ROOT=$CAFFE_ROOT/python  
ENV PYTHONPATH=$PYCAFFE_ROOT:$PYTHONPATH \  
PATH=$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
# Install Theano and set up Theano config (.theanorc) OpenBLAS  
RUN pip --no-cache-dir install
git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \  
\  
echo "[global]\ndevice=cpu\nfloatX=float32\nmode=FAST_RUN \  
\n[lib]\ncnmem=0.95 \  
\n[nvcc]\nfastmath=True \  
\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \  
\n[DebugMode]\ncheck_finite=1" \  
> /root/.theanorc  
  
# Install Keras  
RUN pip --no-cache-dir install
git+git://github.com/fchollet/keras.git@${KERAS_VERSION}  
  
# Install Lasagne  
RUN pip --no-cache-dir install
git+git://github.com/Lasagne/Lasagne.git@${LASAGNE_VERSION}  
  
# Install Torch  
RUN git clone https://github.com/torch/distro.git /root/torch --recursive && \  
cd /root/torch && \  
bash install-deps && \  
yes no | ./install.sh  
  
# Export the LUA evironment variables manually  
ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
\  
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
\  
PATH=/root/torch/install/bin:$PATH \  
LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH \  
DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
  
# Install the latest versions of nn, and iTorch  
RUN luarocks install nn && \  
luarocks install loadcaffe && \  
\  
cd /root && git clone https://github.com/facebook/iTorch.git && \  
cd iTorch && \  
luarocks make  
  
# Install OpenCV  
RUN git clone \--depth 1 https://github.com/opencv/opencv.git /root/opencv &&
\  
cd /root/opencv && \  
mkdir build && \  
cd build && \  
cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON
-DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. && \  
make -j"$(nproc)" && \  
make install && \  
ldconfig && \  
echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc  
  
RUN conda clean -a -y  
# Set up notebook config  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:
https://github.com/ipython/ipython/issues/7062  
COPY run_jupyter.sh /root/  
  
# Expose Ports for TensorBoard (6006), Ipython (8888)  
EXPOSE 6006 8888  
WORKDIR "/root"  
CMD ["/bin/bash"]  

