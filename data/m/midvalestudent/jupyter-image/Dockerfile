FROM midvalestudent/jupyter-scipy:latest  
  
USER root  
ENV HOME /root  
  
ADD requirements.txt /usr/local/share/requirements.txt  
RUN pip install --upgrade pip && pip install -r
/usr/local/share/requirements.txt  
  
# Download/build/install ffmpeg  
ARG FFMPEG_VERSION  
ENV FFMPEG_VERSION ${FFMPEG_VERSION:-"3.2"}  
RUN DEBIAN_FRONTEND=noninteractive \  
&& REPO=http://www.deb-multimedia.org \  
&& echo "deb $REPO jessie main non-free\ndeb-src $REPO jessie main non-free"
>> /etc/apt/sources.list \  
&& apt-get update && apt-get install -y --force-yes deb-multimedia-keyring &&
apt-get update \  
&& apt-get remove ffmpeg \  
&& apt-get install -yq --no-install-recommends \  
build-essential \  
libmp3lame-dev \  
libvorbis-dev \  
libtheora-dev \  
libspeex-dev \  
yasm \  
pkg-config \  
libfaac-dev \  
libopenjpeg-dev \  
libx264-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/build && cd /usr/src/build \  
&& wget http://ffmpeg.org/releases/ffmpeg-$FFMPEG_VERSION.tar.gz \  
&& tar xzf ffmpeg-$FFMPEG_VERSION.tar.gz && cd ffmpeg-$FFMPEG_VERSION \  
&& ./configure \  
\--prefix=/usr/local \  
\--enable-gpl \  
\--enable-postproc \  
\--enable-swscale \  
\--enable-avfilter \  
\--enable-libmp3lame \  
\--enable-libvorbis \  
\--enable-libtheora \  
\--enable-libx264 \  
\--enable-libspeex \  
\--enable-shared \  
\--enable-pthreads \  
\--enable-libopenjpeg \  
\--enable-nonfree \  
&& make -j$(nproc) install && ldconfig \  
&& cd /usr/src/build && rm -rf ffmpeg-$FFMPEG_VERSION* \  
&& apt-get purge -y cmake && apt-get autoremove -y --purge  
  
# Download/build/install components for opencv  
ARG OPENCV_VERSION  
ENV OPENCV_VERSION ${OPENCV_VERSION:-"3.2.0"}  
RUN DEBIAN_FRONTEND=noninteractive \  
&& REPO=http://cdn-fastly.deb.debian.org \  
&& echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security
jessie/updates main" > /etc/apt/sources.list \  
&& apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
build-essential \  
cmake \  
git-core \  
pkg-config \  
libjpeg62-turbo-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libatlas-base-dev \  
gfortran \  
tesseract-ocr \  
tesseract-ocr-eng \  
libtesseract-dev \  
libleptonica-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/build && cd /usr/src/build \  
&& git clone -b $OPENCV_VERSION --depth 1 --recursive
https://github.com/opencv/opencv.git \  
&& git clone -b $OPENCV_VERSION --depth 1 --recursive
https://github.com/opencv/opencv_contrib.git \  
&& cd opencv && mkdir build && cd build \  
&& cmake \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/usr/src/build/opencv_contrib/modules \  
-D BUILD_EXAMPLES=OFF \  
-D FFMPEG_INCLUDE_DIR=/usr/local/include \  
-D FFMPEG_LIB_DIR=/usr/local/lib \  
.. \  
&& make -j4 install && ldconfig \  
&& cd /usr/src/build && rm -rf opencv && rm -rf opencv_contrib \  
&& apt-get purge -y cmake && apt-get autoremove -y --purge  
  
# back to unpriviliged user  
ENV HOME /home/$NB_USER  

