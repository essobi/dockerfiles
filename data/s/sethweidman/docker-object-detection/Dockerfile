FROM ubuntu:16.04  
  
MAINTAINER Sai Soundararaj <saip@outlook.com>  
  
ARG TENSORFLOW_VERSION=1.4.0  
ARG TENSORFLOW_ARCH=cpu  
ARG KERAS_VERSION=1.2.0  
  
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
qt5-default \  
libvtk6-dev \  
zlib1g-dev \  
libjpeg-dev \  
libwebp-dev \  
libpng-dev \  
libtiff5-dev \  
libjasper-dev \  
libopenexr-dev \  
libgdal-dev \  
libdc1394-22-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libtheora-dev \  
libvorbis-dev \  
libxvidcore-dev \  
libx264-dev \  
yasm \  
libopencore-amrnb-dev \  
libopencore-amrwb-dev \  
libv4l-dev \  
libxine2-dev \  
libtbb-dev \  
libeigen3-dev \  
python-dev \  
python-tk \  
python-numpy \  
python3-dev \  
python3-tk \  
python3-numpy \  
ant \  
default-jdk \  
doxygen \  
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
  
# Install OpenCV  
RUN git clone --depth 1 https://github.com/opencv/opencv.git /root/opencv && \  
cd /root/opencv && \  
mkdir build && \  
cd build && \  
cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON
-DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. && \  
make -j"$(nproc)" && \  
make install && \  
ldconfig && \  
echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc  
  
# Set up notebook config  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:
https://github.com/ipython/ipython/issues/7062  
COPY run_jupyter.sh /root/  
  
# Copy object detection files  
RUN apt-get update && \  
apt-get install protobuf-compiler python-pil python-lxml -y  
  
RUN git clone https://github.com/tensorflow/models.git /root/models && \  
cd /root/models/research && \  
protoc object_detection/protos/*.proto --python_out=. && \  
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slims  
  
# Install Flask  
RUN pip install flask  
  
# Copy detection files  
COPY detect_objects.py /root/  
  
COPY detection_app.py /root/  
  
# Export password as environment variable  
ENV PASSWORD="12345"  
  
WORKDIR "/root"  
  
ENTRYPOINT [ "python" ]  
  
CMD [ "detection_app.py" ]  

