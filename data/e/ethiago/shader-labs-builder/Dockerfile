FROM ubuntu:xenial as packages  
  
RUN apt-get update -q && apt-get install -y \  
build-essential \  
git \  
libfontconfig1-dev \  
libfreetype6-dev \  
libglib2.0-dev \  
libglu1-mesa-dev \  
libgtk2.0-dev \  
libx11-dev \  
libx11-xcb-dev \  
libxcb-glx0-dev \  
libxcb1-dev \  
libxcursor-dev \  
libxext-dev \  
libxi-dev \  
make \  
mesa-common-dev  
  
FROM packages as source  
  
RUN git clone \  
--depth=1 \  
--recurse-submodules \  
--single-branch \  
-b v4.8.6 \  
https://github.com/qt/qt.git \  
/qt-src  
  
FROM source as library  
  
WORKDIR /qt-src  
  
RUN mkdir /qt && \  
./configure \  
-static \  
-release \  
-confirm-license \  
-platform linux-g++-64 \  
-silent \  
-prefix /qt \  
-opensource \  
-nomake demos \  
-nomake examples \  
-nomake tests \  
-nomake docs \  
-nomake translations \  
-no-fast \  
-no-exceptions \  
-no-qt3support \  
-opengl desktop \  
-qt-libpng \  
-qt-libmng \  
-qt-libtiff \  
-qt-libjpeg && \  
make && make install  
  
FROM packages  
  
RUN mkdir /qt /workspace  
  
COPY --from=library /qt /qt  
  
ENV PATH=/qt/bin:$PATH  
  
WORKDIR /workspace  
  
CMD ["/bin/bash"]  

