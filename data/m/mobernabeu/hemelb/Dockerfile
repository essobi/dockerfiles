# Taking as base image a Ubuntu Desktop container with web-based noVNC
connection enabled  
FROM dorowu/ubuntu-desktop-lxde-vnc  
MAINTAINER Miguel O. Bernabeu (miguel.bernabeu@ed.ac.uk)  
  
##  
# Dependencies  
##  
# Ubuntu's OpenMPI is in Universe. Our base container runs Ubuntu 14.04, which
doesn't provide cmake 3.2, add PPA repo  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe"
&& \  
add-apt-repository ppa:george-edison55/cmake-3.x && \  
apt-get update  
  
# CppUnit fails to compile if downloaded by HemeLB's CMake, install it system-
wide  
RUN apt-get install -y git cmake libcppunit-dev libcgal-dev python-wxtools
python-wxversion swig openmpi-bin libopenmpi-dev freeglut3-dev  
RUN pip install cython numpy PyYAML  
  
##  
# Download and install VMTK  
##  
WORKDIR /tmp  
RUN git clone https://github.com/vmtk/vmtk.git  
RUN mkdir vmtk-build && \  
cd vmtk-build && \  
cmake ../vmtk && \  
make  
# The following two ENV statements are NOT concatenated as the setting of
VMTKHOME isn't visible until the end of the command.  
ENV VMTKHOME=/tmp/vmtk-build/Install  
ENV PATH=$VMTKHOME/bin:$PATH \  
LD_LIBRARY_PATH=$VMTKHOME/lib:$LD_LIBRARY_PATH \  
PYTHONPATH=$VMTKHOME/lib/python2.7/site-packages:$PYTHONPATH  
  
##  
# Download and install HemeLB  
##  
WORKDIR /tmp  
RUN git clone https://github.com/UCL/hemelb.git  
RUN mkdir hemelb/build && \  
cd hemelb/build && \  
cmake .. -DHEMELB_STEERING_LIB=none -DHEMELB_USE_SSE3=ON && \  
make  
  
##  
# Configure the setup tool  
##  
# Build the required python components  
WORKDIR /tmp  
RUN cd hemelb/Tools && \  
python setup.py build_ext --inplace && \  
cd setuptool && \  
python setup.py build_ext --inplace  
  
# Install the setup tool scripts and set environment variables  
ENV PYTHONPATH="/tmp/hemelb/Tools:/tmp/hemelb/Tools/setuptool:$PYTHONPATH"  
RUN cp /tmp/hemelb/Tools/setuptool/scripts/* /usr/local/bin  
  
# Create a mount point for data  
VOLUME /data  

