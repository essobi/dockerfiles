# Run GoldenCheetah in a container  
FROM ubuntu:16.04  
# Install updates & dependencies:  
RUN apt-get update && apt-get -qq dist-upgrade && apt-get install -y --no-
install-recommends \  
sudo \  
git \  
curl \  
build-essential \  
\  
`# GC mandatory build dependencies` \  
bison \  
flex \  
mesa-common-dev \  
freeglut3-dev \  
\  
`# SRMIO build dependencies` \  
automake \  
libtool \  
\  
`# GC optional build dependencies` \  
r-base \  
\  
`# Qt build dependencies` \  
`# From: https://wiki.qt.io/QtWebEngine/How_to_Try` \  
openssh-client \  
ca-certificates \  
locales \  
pkg-config \  
libgl1-mesa-dev \  
libsm6 \  
libice6 \  
libxext6 \  
libxrender1 \  
libfontconfig1-dev \  
libdbus-1-3 \  
\  
`# QtWebengine build dependencies` \  
gperf ruby python libasound2-dev libbz2-dev libcap-dev libcups2-dev \  
libdrm-dev libegl1-mesa-dev libgcrypt11-dev libnss3-dev libpci-dev \  
libpulse-dev libudev-dev libxtst-dev gyp ninja-build libssl-dev \  
libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libxss-dev \  
libsrtp0-dev libwebp-dev libjsoncpp-dev libopus-dev libminizip-dev \  
libavutil-dev libavformat-dev libavcodec-dev libevent-dev \  
\  
&& apt-get clean  
  
# Install SRMIO  
RUN git clone git://github.com/rclasen/srmio /opt/srmio \  
&& cd /opt/srmio \  
&& sh genautomake.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Install Qt5.9  
ENV QT_PATH /opt/Qt  
ENV QT_DESKTOP $QT_PATH/5.9.1/gcc_64  
COPY extract-qt-installer.sh /tmp/qt/  
RUN curl -Lo /tmp/qt/installer.run 'http://download.qt-
project.org/official_releases/qt/5.9/5.9.1/qt-opensource-linux-x64-5.9.1.run'
\  
&& QT_CI_PACKAGES=qt.591.gcc_64,qt.591.qtwebengine /tmp/qt/extract-qt-
installer.sh /tmp/qt/installer.run "$QT_PATH" \  
&& find "$QT_PATH" -mindepth 1 -maxdepth 1 ! -name '5.*' -exec echo 'Cleaning
Qt SDK: {}' \; -exec rm -r '{}' \; \  
&& rm -rf /tmp/qt  
ENV PATH $QT_DESKTOP/bin:$PATH  
  
# Build GoldenCheetah with included config files  
ENV GC_PATH /opt/GoldenCheetah  
RUN git clone \--branch release_3.4.0
git://github.com/GoldenCheetah/GoldenCheetah "$GC_PATH"  
COPY gcconfig.pri /opt/GoldenCheetah/src/gcconfig.pri  
COPY qwtconfig.pri /opt/GoldenCheetah/qwt/qwtconfig.pri  
RUN cd "$GC_PATH" \  
&& qmake -recursive \  
&& make \  
&& cp ./src/GoldenCheetah /usr/local/bin  
  
# Finalise the container environment  
ENV HOME /data  
WORKDIR $HOME  
VOLUME ["/data/.goldencheetah", "/files"]  
  
ENTRYPOINT ["GoldenCheetah"]  
  

