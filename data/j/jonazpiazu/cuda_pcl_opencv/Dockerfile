FROM nvidia/cuda:8.0-devel-ubuntu14.04  
WORKDIR ${HOME}/src  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update -qq && \  
apt-get -qq install --no-install-recommends -y apt-utils wget ca-certificates
sudo build-essential cmake git software-properties-common  
  
RUN apt-get -qq install -y freeglut3-dev python-vtk libvtk-java libglew-dev
unzip  
  
RUN mkdir deps  
  
## PCL  
RUN add-apt-repository -y ppa:v-launchpad-jochen-sprickerhof-de/pcl && \  
apt-get update -qq && \  
apt-get -qq install -y libpcl-all  
  
#Building OpenCV from scratch without Qt and with nonfree  
RUN cd deps && \  
wget -q http://sourceforge.net/projects/opencvlibrary/files/opencv-
unix/2.4.9/opencv-2.4.9.zip && \  
unzip -q opencv-2.4.9.zip && \  
rm opencv-2.4.9.zip && \  
mkdir -p opencv-2.4.9/build && \  
cd opencv-2.4.9/build && \  
cmake -D BUILD_NEW_PYTHON_SUPPORT=OFF -D WITH_OPENCL=OFF -D WITH_OPENMP=ON -D
INSTALL_C_EXAMPLES=OFF -D BUILD_DOCS=OFF -D BUILD_EXAMPLES=OFF -D WITH_QT=OFF
-D WITH_OPENGL=OFF -D WITH_VTK=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_TESTS=OFF
-D WITH_CUDA=OFF -D BUILD_opencv_gpu=OFF .. && \  
make -j8 && \  
make install && \  
echo "/usr/local/lib" | tee -a /etc/ld.so.conf.d/opencv.conf && \  
ldconfig && \  
echo "PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig" | tee -a
/etc/bash.bashrc && \  
echo "export PKG_CONFIG_PATH" | tee -a /etc/bash.bashrc && \  
cd ../.. && \  
rm -rf opencv-2.4.9  
  
#cleanup  
RUN rm -rf deps && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

