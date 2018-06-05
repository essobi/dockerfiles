FROM nvidia/cuda:7.5-cudnn4-devel  
  
MAINTAINER Zsolt Pasztori <zspasztori@gmail.com>  
  
ARG THEANO_VERSION=rel-0.8.2  
ARG TENSORFLOW_VERSION=0.8.0  
ARG TENSORFLOW_ARCH=gpu  
ARG KERAS_VERSION=1.0.3  
  
# Install some dependencies  
RUN apt-get update && apt-get install -y \  
bc \  
build-essential \  
cmake \  
curl \  
g++ \  
gfortran \  
git \  
libffi-dev \  
libfreetype6-dev \  
libhdf5-dev \  
libjpeg-dev \  
liblcms2-dev \  
libopenblas-dev \  
liblapack-dev \  
libopenjpeg2 \  
libpng12-dev \  
libssl-dev \  
libtiff5-dev \  
libwebp-dev \  
libzmq3-dev \  
nano \  
pkg-config \  
python-dev \  
software-properties-common \  
unzip \  
vim \  
wget \  
zlib1g-dev \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
# Link BLAS library to use OpenBLAS using the alternatives mechanism
(https://www.scipy.org/scipylib/building/linux.html#debian-ubuntu)  
update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3  
  
# Install pip  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
# Add SNI support to Python  
RUN pip --no-cache-dir install \  
pyopenssl \  
ndg-httpsclient \  
pyasn1  
  
# Install useful Python packages using apt-get to avoid version
incompatibilities with Tensorflow binary  
# especially numpy, scipy, skimage and sklearn (see
https://github.com/tensorflow/tensorflow/issues/2034)  
RUN apt-get update && apt-get install -y \  
python-numpy \  
python-scipy \  
python-nose \  
python-h5py \  
python-skimage \  
python-matplotlib \  
python-pandas \  
python-sklearn \  
python-sympy \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
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
  
# Install Theano and set up Theano config (.theanorc) for CUDA and OpenBLAS  
RUN pip --no-cache-dir install
git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \  
\  
echo
"[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN
\  
\n[lib]\ncnmem=0.95 \  
\n[nvcc]\nfastmath=True \  
\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \  
\n[DebugMode]\ncheck_finite=1" \  
> /root/.theanorc  
  
  
# Install Keras  
RUN pip --no-cache-dir install
git+git://github.com/fchollet/keras.git@${KERAS_VERSION}  
  
# Expose Ports for TensorBoard (6006), Ipython (8888)  
EXPOSE 6006 8888  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

