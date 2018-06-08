FROM node:latest  
  
LABEL maintainer="John Murch <john@tomesoftware.com>, Mike Swierenga
<mike@tomesoftware.com>" description="Canon/Tome Paddle-API Dockfile"  
  
ENV NODE_ENV=development  
ENV PORT=3000  
COPY . /var/www  
WORKDIR /var/www  
  
RUN npm install nodemon -g  
RUN npm install knex -g  
RUN npm install --no-optional  
  
# RUN ONCE - @todo put in different build script  
#RUN knex migrate:latest  
#RUN knex seed:run  
EXPOSE $PORT  
  
# INSTALL dependencies  
RUN apt-get update  
RUN apt-get install -y zbar-tools  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y apt-file  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y --no-install-recommends apt-utils software-properties-
common python-software-properties  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
cmake \  
git \  
wget \  
unzip \  
yasm \  
pkg-config \  
libopenblas-dev \  
gfortran \  
libtbb2 \  
libjpeg62-turbo-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libgtk2.0-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libxvidcore-dev \  
libx264-dev \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libpq-dev \  
libatlas-base-dev \  
python-dev \  
python-pip \  
python3-pip \  
python-setuptools \  
python-wheel \  
python3-setuptools \  
python3-wheel \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
#  
RUN python --version  
RUN python3 --version  
  
##  
### INSTALL numpy / imutils  
RUN pip install numpy  
RUN pip install imutils  
##  
##python -m pip install --upgrade --force setuptools  
##python -m pip install --upgrade --force pip  
##RUN pip install --upgrade pip  
##RUN pip3 install --upgrade pip3  
##  
RUN mkdir opencv  
WORKDIR /opencv  
### INSTALL OpenCV  
ENV OPENCV_VERSION="3.4.0"  
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip  
RUN unzip ${OPENCV_VERSION}.zip  
RUN mkdir /opencv/opencv-${OPENCV_VERSION}/cmake_binary  
WORKDIR /opencv/opencv-${OPENCV_VERSION}/cmake_binary  
#  
RUN cmake -DBUILD_TIFF=ON \  
-DBUILD_opencv_java=OFF \  
-DWITH_CUDA=OFF \  
-DENABLE_AVX=ON \  
-DWITH_OPENGL=ON \  
-DWITH_OPENCL=ON \  
-DWITH_IPP=ON \  
-DWITH_TBB=ON \  
-DWITH_EIGEN=ON \  
-DWITH_V4L=ON \  
-DBUILD_TESTS=OFF \  
-DBUILD_PERF_TESTS=OFF \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DCMAKE_INSTALL_PREFIX=$(python3.4 -c "import sys; print(sys.prefix)") \  
-DPYTHON_EXECUTABLE=$(which python3.4) \  
-DPYTHON_INCLUDE_DIR=$(python3.4 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-DPYTHON_PACKAGES_PATH=$(python3.4 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..  
  
RUN make install  
  
#RUN rm /opencv/${OPENCV_VERSION}.zip \  
#RUN rm -r /opencv  
ENTRYPOINT ["npm","start"]  

