FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
  
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
python3 get-pip.py && \  
rm get-pip.py  
  
# Install other useful Python packages using pip  
RUN pip3 --no-cache-dir install --upgrade ipython && \  
pip3 --no-cache-dir install \  
cycler==0.10.0 \  
decorator==4.0.11 \  
h5py==2.7.0 \  
joblib==0.11 \  
matplotlib==2.0.0 \  
networkx==1.11 \  
numpy==1.12.1 \  
olefile==0.44 \  
Pillow==4.1.0 \  
protobuf==3.2.0 \  
pyparsing==2.2.0 \  
python-dateutil==2.6.0 \  
pytz==2017.2 \  
PyWavelets==0.5.2 \  
scikit-image==0.13.0 \  
scikit-learn==0.18.1 \  
scipy==0.19.0 \  
six==1.10.0 \  
sklearn==0.0 \  
tensorflow==1.1.0 \  
Werkzeug==0.12.1  
  

