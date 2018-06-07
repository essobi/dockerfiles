FROM ubuntu:trusty  
  
MAINTAINER GaRaOne  
  
ARG QT=5.8.0  
ARG QTM=5.8  
ENV DEBIAN_FRONTEND noninteractive  
ENV QT_PATH /opt/qt  
ENV QT_BASE_DIR=$QT_PATH  
  
ENV QT_ARCH ${QT_PATH}/${QTM}/gcc_64  
ENV LD_LIBRARY_PATH=$QT_PATH/lib/x86_64-linux-
gnu:$QT_PATH/lib:$LD_LIBRARY_PATH  
ENV PKG_CONFIG_PATH=$QT_BAQT_PATHSE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH  
ENV PATH=${PATH}:${QT_ARCH}/bin  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN sudo dpkg --add-architecture i386 && \  
apt-get update -q && \  
apt-get install -q -y --no-install-recommends \  
ant \  
build-essential \  
ca-certificates \  
curl \  
default-jdk \  
git \  
libavahi-client-dev \  
libavahi-common-dev \  
libc6:i386 \  
libfontconfig1 \  
libglib2.0-dev \  
libglu1-mesa-dev \  
libice6 \  
libpulse-dev \  
libncurses5:i386 \  
libsm6 \  
libstdc++6:i386 \  
libX11-xcb1 \  
libxext6 \  
libxrender1 \  
libz1:i386 \  
mesa-common-dev \  
openssh-client \  
p7zip-full \  
xvfb \  
&& apt-get clean  
  
# download & install qt  
ADD qt-installer-noninteractive.qs /tmp/qt/script.qs  
ADD http://download.qt.io/official_releases/qt/${QTM}/${QT}/qt-opensource-
linux-x64-${QT}.run /tmp/qt/installer.run  
  
RUN chmod +x /tmp/qt/installer.run \  
&& xvfb-run /tmp/qt/installer.run --script /tmp/qt/script.qs \  
| egrep -v '\\[[0-9]+\\] Warning: (Unsupported screen
format)|((QPainter|QWidget))' \  
&& rm -rf /tmp/qt  
  
RUN locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales  
  
# CLEAN CACHE  
RUN rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

