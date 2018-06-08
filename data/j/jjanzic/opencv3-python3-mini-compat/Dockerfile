FROM alpine  
MAINTAINER Josip Janzic <josip.janzic@gmail.com>  
  
ENV CPUCOUNT 1  
RUN CPUCOUNT=$(cat /proc/cpuinfo | grep '^processor.*:' | wc -l)  
  
RUN echo -e '@edge http://nl.alpinelinux.org/alpine/edge/main\n@testing
http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories  
  
RUN apk update && apk upgrade && apk add --update \  
python3 \  
python3-dev \  
make \  
cmake \  
gcc \  
g++ \  
pkgconf \  
unzip \  
wget \  
build-base \  
gsl \  
ffmpeg-dev \  
libtbb@testing \  
libtbb-dev@testing \  
libjpeg \  
libjpeg-turbo-dev \  
libpng-dev \  
libjasper \  
clang \  
linux-headers  
  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O - | python3  
  
ENV CC /usr/bin/clang  
ENV CXX /usr/bin/clang++  
  
# install numpy from github to get:
https://github.com/numpy/numpy/commit/f189e2adcdd05596a6f65b4097e2f12f9c0d9ce9  
ADD numpy.patch /numpy.patch  
RUN pip install requests cython  
  
RUN curl --insecure
https://codeload.github.com/numpy/numpy/tar.gz/maintenance/1.10.x | tar xz \  
&& cd numpy-maintenance-1.10.x/numpy/core/src/private/ \  
&& patch < /numpy.patch \  
&& cd /numpy-maintenance-1.10.x \  
&& python3 setup.py install  
  
RUN wget https://github.com/Itseez/opencv/archive/3.1.0.zip \  
&& unzip 3.1.0.zip \  
&& mkdir /opencv-3.1.0/cmake_binary \  
&& cd /opencv-3.1.0/cmake_binary \  
&& cmake \  
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
-DCMAKE_INSTALL_PREFIX=/usr \  
-DPYTHON_EXECUTABLE=/usr/bin/python3.5 \  
-DPYTHON_INCLUDE_DIR=/usr/include/python3.5m \  
-DPYTHON_PACKAGES_PATH=/usr/lib/python3.5/site-packages \  
.. \  
&& make -j${CPUCOUNT} install \  
&& rm /3.1.0.zip \  
&& rm -r /opencv-3.1.0  
  
RUN apk add zlib-dev zlib  
RUN CFLAGS="$CFLAGS -L/lib" pip install pillow  
  
RUN rm -rf /var/cache/apk/*  
  
RUN mkdir -p /root  
  
WORKDIR /root  

