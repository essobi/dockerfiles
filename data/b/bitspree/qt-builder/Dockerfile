FROM ubuntu:17.10  
LABEL authors="garaone@co3.de"  
  
ARG QT=5.10.0  
ARG QTM=5.10  
ENV DEBIAN_FRONTEND noninteractive  
ENV QT_PATH /opt/qt  
ENV QT_BASE_DIR=$QT_PATH  
  
ENV QT_ARCH ${QT_PATH}/${QT}/gcc_64  
ENV LD_LIBRARY_PATH=$QT_PATH/lib/x86_64-linux-
gnu:$QT_PATH/lib:$LD_LIBRARY_PATH  
ENV PKG_CONFIG_PATH=$QT_BAQT_PATHSE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH  
ENV PATH=${PATH}:${QT_ARCH}/bin  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update -q && \  
apt-get install -q -y --no-install-recommends \  
ant \  
build-essential \  
ca-certificates \  
curl \  
git \  
libfontconfig1 \  
libglib2.0-dev \  
libglu1-mesa-dev \  
libice6 \  
libpulse-dev \  
libsm6 \  
libxext6 \  
libxrender1 \  
locales \  
mesa-common-dev \  
openssh-client \  
p7zip-full \  
xvfb \  
unzip \  
wget  
  
# download & install qt  
ADD qt-installer-noninteractive.qs /tmp/qt/script.qs  
# ADD ./qt-opensource-linux-x64-${QT}.run /tmp/qt/installer.run  
ADD http://download.qt.io/official_releases/qt/${QTM}/${QT}/qt-opensource-
linux-x64-${QT}.run /tmp/qt/installer.run  
  
RUN chmod +x /tmp/qt/installer.run \  
&& xvfb-run /tmp/qt/installer.run --script /tmp/qt/script.qs \  
| egrep -v '\\[[0-9]+\\] Warning: (Unsupported screen
format)|((QPainter|QWidget))' \  
&& rm -rf /tmp/qt  
  
RUN locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales  
  
###################  
# FIREBASE_CPP_SDK  
ADD https://dl.google.com/firebase/sdk/cpp/firebase_cpp_sdk_4.4.0.zip
/install/firebase_cpp_sdk.zip  
  
###################  
# CLEAN UP  
RUN apt-get clean autoclean \  
&& apt-get autoremove -y  
# && rm -rf \  
# /var/lib/apt/lists/* \  
# /tmp/* \  
# /var/tmp/* \  
# /var/lib/dpkg/* \  
# /var/lib/cache/* \  
# /var/lib/log/*  
CMD ["/bin/bash"]  

