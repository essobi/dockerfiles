# Built from ContinuumIO's Anaconda 3 image, which in turn is built on Debian.  
FROM continuumio/anaconda3  
MAINTAINER Shannon Quinn "magsol@gmail.com"  
ENV OPENCV_VERSION "3.1.0"  
RUN apt-get -y update  
RUN apt-get -y install \  
build-essential vim cmake libgtk2.0-dev pkg-config libavcodec-dev tcl-vtk \  
libavformat-dev libswscale-dev libtbb2 libtbb-dev libtiff5-dev libjpeg-dev \  
libjasper-dev libdc1394-22-dev unzip libblas-dev liblapack-dev qt5-default \  
libvtk6-dev openjdk-7-jdk libpng12-dev libeigen3-dev libtheora-dev ant \  
libvorbis-dev libxvidcore-dev sphinx-common yasm libavutil-dev \  
libopencore-amrnb-dev libopencore-amrwb-dev libavfilter-dev libopenexr-dev \  
libgstreamer-plugins-base1.0-dev libx264-dev libavresample-dev  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
# Fixes a weird cv2 import error.  
RUN conda install libgcc  
  
# Install OpenCV!  
RUN wget https://github.com/Itseez/opencv/archive/$OPENCV_VERSION.zip && \  
unzip $OPENCV_VERSION.zip && rm $OPENCV_VERSION.zip && \  
mkdir opencv-$OPENCV_VERSION/build  
WORKDIR opencv-$OPENCV_VERSION/build/  
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=$(python -c "import sys; print(sys.prefix)") \  
-D PYTHON3_EXECUTABLE=$(which python3) \  
-D PYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-D PYTHON3_PACKAGES_PATH=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \  
-D PYTHON3_NUMPY_INCLUDE_DIRS=/opt/conda/lib/python3.5/site-packages/numpy/core/include \  
-D PYTHON_LIBRARY=/opt/conda/lib/libpython3.5m.so \  
..  
RUN make -j 8 && make install  
WORKDIR /  
RUN rm -rf opencv-$OPENCV_VERSION  
  
# Fixes a bizarre camera driver problem.  
RUN ln /dev/null /dev/raw1394  
  
CMD [ "/bin/bash" ]  

