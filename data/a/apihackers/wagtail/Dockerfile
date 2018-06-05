FROM alpine:edge  
  
MAINTAINER API Hackers  
  
# Add Edge and bleeding repos  
RUN echo -e '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& echo -e '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories  
  
# Install permanent system depdencies  
RUN apk add --update --no-cache \  
bash \  
ca-certificates \  
gettext \  
gsl \  
gzip \  
imagemagick \  
libavc1394 \  
libdc1394 \  
libjpeg \  
libpng \  
libpq \  
libtbb@testing \  
libwebp \  
python3 \  
tiff \  
yaml \  
python3-dev \  
build-base \  
libjpeg-turbo-dev \  
libpng-dev \  
tiff-dev \  
libwebp-dev \  
imagemagick-dev \  
zlib-dev \  
postgresql-dev \  
zlib &&\  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
# Define some versions  
ENV OPENCV_VERSION 3.3.0  
ENV WAGTAIL_VERSION 1.12.2  
ENV DJANGO_VERSION 1.11.6  
# Define compilers  
ENV CC /usr/bin/clang  
ENV CXX /usr/bin/clang++  
  
# Alpine store some headers into /lib/  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
# Compile and install OpenCV for Python 3 and wagtail  
# Temporary install build dependencies  
RUN apk add --no-cache --virtual .build-deps@testing \  
curl \  
cmake \  
pkgconf \  
unzip \  
libavc1394-dev \  
libdc1394-dev \  
clang \  
clang-dev \  
libtbb@testing \  
libtbb-dev@testing \  
linux-headers \  
# Fix numpy compilation  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
# Enable some numpy optimization  
&& pip3 install cython \  
&& pip3 install numpy \  
# Build OpenCV  
&& mkdir /opt && cd /opt \  
&& curl -OsSL https://github.com/Itseez/opencv/archive/${OPENCV_VERSION}.zip \  
&& unzip ${OPENCV_VERSION}.zip \  
&& cd /opt/opencv-${OPENCV_VERSION} \  
&& mkdir build && cd build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
# Gain some space and time by disabling some features  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D BUILD_EXAMPLES=OFF \  
-D WITH_FFMPEG=NO \  
-D WITH_IPP=NO \  
-D WITH_OPENEXR=NO \  
.. \  
&& VERBOSE=1 make && make install \  
&& cd && rm -fr /opt \  
# Install Wagtail and some depdencies  
&& pip3 install django==$DJANGO_VERSION wagtail==$WAGTAIL_VERSION django-redis
psycopg2 wand \  
# Cleanup  
&& apk del .build-deps && rm -r /root/.cache  

