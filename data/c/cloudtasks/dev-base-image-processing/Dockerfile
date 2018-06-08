FROM mhart/alpine-node:latest  
  
ENV CC /usr/bin/clang  
ENV CXX /usr/bin/clang++  
  
RUN echo -e '@edge http://nl.alpinelinux.org/alpine/edge/main\n@testing
http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories \  
&& apk add \--update python3 python3-dev make cmake gcc g++ git pkgconf unzip
wget py-pip build-base gsl libavc1394-dev libtbb@testing libtbb-dev@testing
libjpeg libjpeg-turbo-dev libpng-dev libjasper libdc1394-dev clang tiff-dev
libwebp-dev py-numpy-dev@testing py-scipy-dev@testing linux-headers
imagemagick \  
&& mkdir /opt && cd /opt \  
&& wget --no-check-certificate
https://github.com/Itseez/opencv/archive/3.1.0.zip \  
&& unzip 3.1.0.zip \  
&& rm 3.1.0.zip \  
&& cd /opt/opencv-3.1.0 \  
&& mkdir build \  
&& cd build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=NO -D
CMAKE_INSTALL_PREFIX=~/opencv -D WITH_FFMPEG=NO -D WITH_IPP=NO -D
WITH_OPENEXR=NO .. \  
&& make VERBOSE=1 \  
&& make \  
&& make install \  
&& mkdir /src \  
&& cd /src \  
&& PKG_CONFIG_PATH=~/opencv/lib/pkgconfig/ npm install opencv \  
&& npm install nodemon cwebp-bin -g \  
&& apk del python3 python3-dev make cmake gcc g++ git pkgconf unzip wget py-
pip build-base gsl libavc1394-dev libtbb libtbb-dev libjasper libdc1394-dev
clang py-numpy-dev py-scipy-dev linux-headers \  
&& rm -rf /opt/opencv-3.1.0  
# && rm -rf ~/opencv \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /src  
  
ENV NODE_ENV=development  
  
CMD nodemon -L

