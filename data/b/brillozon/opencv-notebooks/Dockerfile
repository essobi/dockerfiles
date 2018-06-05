  
FROM jupyter/datascience-notebook:37af02395694  
  
USER root  
  
RUN \  
apt-get -qq update && apt-get -qq upgrade -y \  
&& apt-get -qq install -y \  
build-essential \  
libtbb-dev \  
&& apt-get -qq install -y \  
cmake \  
pkg-config \  
libjpeg8-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libxvidcore-dev \  
libx264-dev \  
libgtk-3-dev \  
libatlas-base-dev \  
gfortran \  
libhdf5-dev \  
python2.7-dev \  
python3.5-dev \  
python3-pip \  
&& pip3 install --upgrade pip \  
&& apt-get autoclean && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
cd /home/jovyan \  
&& curl https://codeload.github.com/opencv/opencv/tar.gz/3.3.0 | tar xz \  
&& mv /home/jovyan/opencv-3.3.0/ /home/jovyan/opencv/ \  
  
&& cd /home/jovyan \  
&& curl https://codeload.github.com/opencv/opencv_contrib/tar.gz/3.3.0 | tar
xz \  
&& mv opencv_contrib-3.3.0 opencv_contrib \  
# HACK add conda lib to library search locations  
&& export LD_LIBRARY_PATH=/opt/conda/lib \  
# make the makefiles  
&& cd /home/jovyan/opencv \  
&& mkdir build \  
&& cd build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=OFF \  
-D PYTHON_EXECUTABLE=/opt/conda/bin/python \  
-D PYTHON_LIBRARY=/opt/conda/lib \  
-D PYTHON_INCLUDE_DIR=/opt/conda/include/python3.6m \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D OPENCV_EXTRA_MODULES_PATH=/home/jovyan/opencv_contrib/modules \  
-D BUILD_EXAMPLES=ON .. \  
# build the libraries  
&& cd /home/jovyan/opencv/build \  
&& make -j `expr 2 \\* $(nproc)` -l $(nproc) \  
&& make install \  
&& ldconfig \  
# clean opencv build artifacts and documentation  
&& rm -rf /home/jovyan/opencv/build \  
&& rm -rf /home/jovyan/opencv/3rdparty \  
&& rm -rf /home/jovyan/opencv/doc \  
&& rm -rf /home/jovyan/opencv/include \  
&& rm -rf /home/jovyan/opencv/platforms \  
&& rm -rf /home/jovyan/opencv/modules \  
&& rm -rf /home/jovyan/opencv_contrib/build \  
&& rm -rf /home/jovyan/opencv_contrib/doc  
  
# HACK!  
RUN ln -s \  
/usr/local/lib/python3.6/site-packages/cv2.cpython-36m-x86_64-linux-gnu.so \  
/opt/conda/lib/python3.6/site-packages/  
  
RUN conda install -y theano tensorflow  
  
RUN chown -R jovyan.users /home/jovyan/opencv /home/jovyan/opencv_contrib  
  
COPY simple-opencv-window.ipynb \  
image-colors-display.ipynb \  
channel-mixing-technicolor.ipynb \  
curves-bending-colorspace.ipynb \  
edged.ipynb \  
convoluted.ipynb /home/jovyan/notebooks/  
  
RUN \  
chown -R jovyan.users /home/jovyan/notebooks \  
&& chmod -R 0775 /home/jovyan/notebooks  
  
USER jovyan  
  
RUN \  
jupyter trust /home/jovyan/notebooks/simple-opencv-window.ipynb \  
&& jupyter trust /home/jovyan/notebooks/image-colors-display.ipynb \  
&& jupyter trust /home/jovyan/notebooks/channel-mixing-technicolor.ipynb \  
&& jupyter trust /home/jovyan/notebooks/curves-bending-colorspace.ipynb \  
&& jupyter trust /home/jovyan/notebooks/edged.ipynb \  
&& jupyter trust /home/jovyan/notebooks/convoluted.ipynb  
  

