# Debian Stretch is recommended  
FROM ubuntu:xenial  
  
# Custom Compiler  
ENV CC clang  
ENV CXX clang++  
  
# Custom Directory  
ENV CUSTOM_DIRECTORY YES  
ENV WDEVBUILD /temp/build  
ENV WDEVSOURCE /temp/src  
ENV WDEVPREFIX /opt/windev  
  
# Custom Version  
ENV CUSTOM_VERSION YES  
ENV QT_SERIES 5.6  
ENV QT_BUILD 3  
ENV LIBJPEGTURBO_VERSION 1.5.3  
ENV LIBRESSL_VERSION 2.6.4  
ENV UPX_VERSION 3.94  
  
# Exclude Static Qt  
ENV BUILD_QT32_SHARED NO  
ENV BUILD_QT64_SHARED NO  
##############################  
# DON'T EDIT BELOW THIS LINE #  
##############################  
  
COPY rootfs /  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y bash clang cmake coreutils gzip libucl1 libucl-dev make
nasm ninja-build perl qtchooser tar wget xz-utils zlib1g zlib1g-dev && \  
apt-get install -y binutils-mingw-w64-x86-64 mingw-w64-x86-64-dev
g++-mingw-w64-x86-64 gcc-mingw-w64-x86-64 binutils-mingw-w64-i686
mingw-w64-i686-dev g++-mingw-w64-i686 gcc-mingw-w64-i686 && \  
/opt/windev/bin/upx_build && \  
ln -s /opt/windev/bin/upx /usr/local/bin/upx && \  
rm -rf /temp && \  
/opt/windev/bin/qt_build && \  
rm -rf /temp && \  
apt-get remove -y clang cmake libucl-dev nasm ninja-build perl wget zlib1g-dev
&& \  
apt-get autoremove -y && \  
apt-get autoclean  
  
RUN qtchooser -install -f qt5-x86_64-w64-mingw32
${WDEVPREFIX}/qt64s_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f qt5-i686-w64-mingw32
${WDEVPREFIX}/qt32s_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f 5 ${WDEVPREFIX}/qt32s_${QT_SERIES}.${QT_BUILD}/bin/qmake
&& \  
qtchooser -install -f qt5
${WDEVPREFIX}/qt32s_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f default
${WDEVPREFIX}/qt32s_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
ln -s ${WDEVPREFIX}/libjpeg-turbo-${LIBJPEGTURBO_VERSION}_qt32s
${WDEVPREFIX}/libjpeg-turbo-latest_qt32s && \  
ln -s ${WDEVPREFIX}/libjpeg-turbo-${LIBJPEGTURBO_VERSION}_qt64s
${WDEVPREFIX}/libjpeg-turbo-latest_qt64s && \  
ln -s ${WDEVPREFIX}/libressl-${LIBRESSL_VERSION}_qt32s ${WDEVPREFIX}/libressl-
latest_qt32s && \  
ln -s ${WDEVPREFIX}/libressl-${LIBRESSL_VERSION}_qt64s ${WDEVPREFIX}/libressl-
latest_qt64s && \  
ln -s ${WDEVPREFIX}/qt32s_${QT_SERIES}.${QT_BUILD} ${WDEVPREFIX}/qt32s-latest
&& \  
ln -s ${WDEVPREFIX}/qt64s_${QT_SERIES}.${QT_BUILD} ${WDEVPREFIX}/qt64s-latest  
  
CMD ["/bin/bash"]  

