FROM ubuntu:14.04  
  
MAINTAINER Dmitriy Belyaev "dimabelyaev27@gmail.com"  
  
RUN echo "deb-src http://httpredir.debian.org/debian unstable main" >>
/etc/apt/sources.list && \  
apt-get update && apt-get -y install curl cmake g++ unzip python pkg-config
libgexiv2-dev libssl-dev  
  
RUN mkdir -p /tmp/opencv && cd /tmp/opencv && curl -O
http://iweb.dl.sourceforge.net/project/libjpeg-turbo/1.4.2/libjpeg-turbo-
official_1.4.2_amd64.deb && \  
dpkg -i libjpeg-turbo-official_1.4.2_amd64.deb && \  
curl -O https://codeload.github.com/Itseez/opencv/zip/2.4.12 && unzip 2.4.12
&& mkdir opencv-2.4.12/build && cd opencv-2.4.12/build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local
-DWITH_JPEG=ON -DBUILD_JPEG=OFF -DJPEG_INCLUDE_DIR=/opt/libjpeg-turbo/include/
-DJPEG_LIBRARY=/opt/libjpeg-turbo/lib64/libjpeg.a .. && \  
make && make install && pkg-config --cflags opencv && pkg-config --libs opencv
&& rm -rf /tmp/opencv  
  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh  
  
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib  

