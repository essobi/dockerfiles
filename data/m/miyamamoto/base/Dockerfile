#FROM ubuntu:16.04  
#FROM nvidia/7.5-cudnn4-devel  
FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER miyamamoto <mitsuo.yamamoto@gmail.com>  
  
# Install dependent packages via apt-get  
RUN apt-get -y update &&\  
echo ">>>>> packages for building python" &&\  
apt-get --no-install-recommends -y install \  
g++ \  
libsqlite3-dev \  
libssl-dev \  
libreadline-dev \  
libncurses5-dev \  
lzma-dev \  
liblzma-dev \  
libbz2-dev \  
libz-dev \  
libgdbm-dev \  
build-essential \  
cmake \  
make \  
wget \  
unzip \  
curl \  
&&\  
echo ">>>>> packages for building python packages" &&\  
apt-get --no-install-recommends -y install \  
libblas-dev \  
liblapack-dev \  
libpng-dev \  
libfreetype6-dev \  
pkg-config \  
ca-certificates \  
libhdf5-serial-dev \  
postgresql \  
libpq-dev \  
&&\  
echo ">>>>> packages for building OpenCV3" &&\  
apt-get --no-install-recommends -y install \  
git \  
libjpeg8-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libatlas-base-dev \  
gfortran \  
libxtst6 \  
emacs \  
&&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
  
# -=-=-=- Anaconda -=-=-=-  
RUN
ANACONDA_URL="https://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh"
&&\  
ANACONDA_FILE="anaconda.sh" &&\  
mkdir -p /opt &&\  
cd /opt &&\  
wget -q --no-check-certificate $ANACONDA_URL -O $ANACONDA_FILE &&\  
echo "9413b1d3ca9498ba6f53913df9c43d685dd973440ff10b7fe0c45b1cbdcb582e
${ANACONDA_FILE}" | sha256sum -c - &&\  
bash $ANACONDA_FILE -b -p /opt/conda &&\  
rm $ANACONDA_FILE  
ENV PATH "$PATH:/opt/conda/bin"  
  
  
# -=-=-=- Python packages (py35 env) -=-=-=-  
COPY py35.yml /opt/  
RUN cd /opt &&\  
conda env create -f py35.yml  
  
  
# -=-=-=- Google Cloud SDK (root env) -=-=-=-  
#ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
#RUN CLOUDSDK_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/google-
cloud-sdk.zip" &&\  
# CLOUDSDK_PATH="/opt/google-cloud-sdk.zip" &&\  
# cd /opt &&\  
# wget -q $CLOUDSDK_URL -O $CLOUDSDK_PATH &&\  
# unzip google-cloud-sdk.zip &&\  
# rm google-cloud-sdk.zip &&\  
# \  
# google-cloud-sdk/install.sh \  
# \--usage-reporting=true \  
# \--path-update=true \  
# \--bash-completion=true \  
# \--rc-path=/.bashrc \  
# \--additional-components \  
# app-engine-python app kubectl alpha beta gcd-emulator pubsub-emulator cloud-
datastore-emulator  
  
#ENV CLOUDSDK_PYTHON /opt/conda/bin/python2  
#ENV PATH "$PATH:/opt/google-cloud-sdk/bin"  
  
# XGBoost  
RUN cd /opt && \  
git clone --recursive https://github.com/dmlc/xgboost xgboost &&\  
cd xgboost &&\  
git checkout v0.60 &&\  
git submodule init &&\  
git submodule update &&\  
bash build.sh &&\  
cd python-package &&\  
bash -c "source activate py35 && python setup.py install" &&\  
ln -s $XGBOOST_PATH/xgboost /opt/conda/bin/xgboost  
  
# LightGBM  
#RUN git clone \--recursive https://github.com/Microsoft/LightGBM ; cd
LightGBM &&\  
# mkdir build ; cd build &&\  
# cmake .. &&\  
# make -j  
  
# OpenCV3  
#RUN OPENCV_URL="https://github.com/opencv/opencv/archive/3.1.0.tar.gz" &&\  
#
OPENCV_CONTRIB_URL="https://github.com/opencv/opencv_contrib/archive/3.1.0.tar.gz"
&&\  
# cd /opt &&\  
# /bin/bash -c "source activate py35" &&\  
# wget -q --no-check-certificate $OPENCV_URL -O opencv.tgz &&\  
# wget -q --no-check-certificate $OPENCV_CONTRIB_URL -O opencv_contrib.tgz &&\  
# tar zxf opencv.tgz &&\  
# tar zxf opencv_contrib.tgz &&\  
# rm opencv.tgz opencv_contrib.tgz &&\  
# mkdir /opt/opencv-3.1.0/build &&\  
# cd /opt/opencv-3.1.0/build &&\  
# cmake -D CMAKE_BUILD_TYPE=RELEASE \  
# -D CMAKE_INSTALL_PREFIX=/opt/conda/envs/py35 \  
# -D WITH_TBB=ON \  
# -D PYTHON_EXECUTABLE=/opt/conda/envs/py35/bin/python \  
# -D PYTHON_INCLUDE_DIR=/opt/conda/envs/py35/include/python3.5m/ \  
# -D PYTHON_PACKAGES_PATH=/opt/conda/envs/py35/lib/python3.5/site-packages/ \  
# -D INSTALL_C_EXAMPLES=OFF \  
# -D INSTALL_PYTHON_EXAMPLES=ON \  
# -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib-3.1.0/modules \  
# -D BUILD_EXAMPLES=ON .. &&\  
# echo 'find_package(HDF5)' >> ../modules/python/common.cmake &&\  
# echo 'include_directories(${HDF5_INCLUDE_DIRS})' >>
../modules/python/common.cmake &&\  
# make -j4 &&\  
# make install &&\  
# ldconfig  
  
# RGF  
#RUN RGF_URL="http://stat.rutgers.edu/home/tzhang/software/rgf/rgf1.2.zip" &&\  
# RGF_FILE="rgf1.2.zip" &&\  
# cd /opt &&\  
# wget -q --no-check-certificate $RGF_URL -O $RGF_FILE &&\  
# echo "753237be5e2ec97f5627c1a0efeb5562caf4f455b3c0114d44bc5bf12595f0a5
rgf1.2.zip" | sha256sum -c - &&\  
# unzip $RGF_FILE &&\  
# cd rgf1.2 &&\  
# \  
# make -j4 &&\  
# ln -s /opt/rgf1.2/bin/rgf /opt/conda/bin/rgf  
  
# LibFM  
#RUN LIBFM_URL="http://www.libfm.org/libfm-1.42.src.tar.gz" &&\  
# LIBFM_FILE="libfm-1.42.src.tar.gz" &&\  
# cd /opt &&\  
# wget -q --no-check-certificate $LIBFM_URL -O $LIBFM_FILE &&\  
# echo "6aaa2503aa1e6da7d08dd86bcf0907ee480f223547ca3b3d08c8f404f7f31695
libfm-1.42.src.tar.gz" | sha256sum -c - &&\  
# tar zxf $LIBFM_FILE &&\  
# cd libfm-1.42.src &&\  
# \  
# make &&\  
# ln -s /opt/bin/libFM /opt/conda/bin/libFM

