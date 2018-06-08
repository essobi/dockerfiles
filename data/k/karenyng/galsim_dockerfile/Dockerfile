# Should update the base image ubuntu version to 16.04 LTS when it comes out  
FROM ubuntu:14.04  
RUN echo "\n\n---------- Downloading and building all OS level tools-----\n\n"  
RUN apt update  
# -y flag bypasses all questions  
RUN apt install -y \  
build-essential \  
software-properties-common \  
python-dev \  
git \  
libatlas-base-dev \  
gfortran \  
wget  
RUN echo "\n\n---------- Finished building all OS level tools----------- \n\n"  
  
# ---- Get the Galsim repository -----------  
WORKDIR /usr/src  
RUN git clone https://github.com/GalSim-developers/GalSim.git  
  
RUN echo "\n\n---------- Downloading and building Python 2.7 packages
-------\n\n"  
RUN apt install -y python2.7 python-pip  
# Should specify the versions of the Python packages  
RUN pip install numpy \  
scipy \  
astropy  
# Have to install starlink_pyast on a separate command for Numpy to be
recognized  
RUN pip install starlink_pyast  
RUN echo "\n\n---------- Finished building Python 2.7 --------------------
\n\n"  
  
RUN echo "\n\n---- Installing other Galsim dependencies: SCONS FFTW3
Boost-------\n\n"  
RUN apt install -y \  
scons \  
libfftw3-dev \  
libboost-all-dev  
  
RUN echo "\n\n---------- Installing TMV-cpp -------\n\n"  
RUN wget https://github.com/rmjarvis/tmv/archive/v0.73.tar.gz  
RUN tar xzvf v0.73.tar.gz  
RUN rm v0.73.tar.gz  
WORKDIR /usr/src/tmv-0.73  
RUN scons && scons install && rm -rf /usr/src/tmv-0.73  
  
# Fix bash error according to  
# https://github.com/GalSim-developers/GalSim/wiki/Installation%20FAQ#why-is-
scons-unable-to-get-python-include-path-python-executable-on-ubuntu  
ENV SHELL /bin/bash  
RUN mv /bin/sh /bin/sh.orig && ln -s /bin/bash /bin/sh  
  
RUN echo "\n\n---------- Installing Galsim -------\n\n"  
WORKDIR /usr/src/GalSim  
RUN git checkout v1.3.0  
RUN scons && scons install && rm -rf /usr/src/GalSim  
  

