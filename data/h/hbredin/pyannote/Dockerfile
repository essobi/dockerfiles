FROM ubuntu:trusty  
MAINTAINER Hervé Bredin <bredin@limsi.fr>  
  
RUN apt-get update  
RUN apt-get install -y build-essential \  
wget \  
curl \  
git  
  
# Python  
RUN apt-get install -y python-pip \  
python-dev \  
python-numpy \  
python-scipy \  
python-numexpr  
RUN pip install ipython  
  
# OpenCV  
RUN apt-get install -y libav-tools \  
libavcodec-extra-54 \  
libopencv-dev \  
python-opencv  
  
# Yaafe  
RUN apt-get install -y cmake cmake-curses-gui \  
libargtable2-0 libargtable2-dev \  
libsndfile1 libsndfile1-dev \  
libmpg123-0 libmpg123-dev \  
libfftw3-3 libfftw3-dev \  
liblapack-dev \  
libhdf5-serial-dev  
  
RUN wget https://github.com/Yaafe/Yaafe/archive/v0.65.1.tar.gz && \  
tar xzvf v0.65.1.tar.gz && \  
cd Yaafe-0.65.1 && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_INSTALL_PYTHON_PACKAGES=/usr/local/lib/python2.7/dist-packages \  
-DCMAKE_INSTALL_YAAFE_EXTENSIONS=/usr/local/lib/python2.7/dist-packages \  
-DWITH_FFTW3=ON \  
-DWITH_HDF5=ON \  
-DWITH_LAPACK=ON \  
-DWITH_MATLAB_MEX=OFF \  
-DWITH_MPG123=ON \  
-DWITH_SNDFILE=ON \  
.. && \  
make && \  
make install && \  
cd ../.. && \  
rm -rf Yaafe-0.65.1 v0.65.1.tar.gz  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
ENV YAAFE_PATH /usr/local/lib/python2.7/dist-packages  
  
# pyannote  
ADD . /src  
RUN pip install /src  
  
CMD ["ipython"]  

