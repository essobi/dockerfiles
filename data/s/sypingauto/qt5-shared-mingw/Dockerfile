# Debian Stretch is recommended  
FROM debian:stretch-slim  
  
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
ENV LIBRESSL_VERSION 2.7.2  
  
# Exclude Static Qt  
ENV BUILD_QT32_STATIC NO  
ENV BUILD_QT64_STATIC NO  
##############################  
# DON'T EDIT BELOW THIS LINE #  
##############################  
  
COPY rootfs /  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y bash clang cmake coreutils gzip make nasm ninja-build perl
qtchooser tar wget xz-utils && \  
apt-get install -y binutils-mingw-w64-x86-64 mingw-w64-x86-64-dev
g++-mingw-w64-x86-64 gcc-mingw-w64-x86-64 binutils-mingw-w64-i686
mingw-w64-i686-dev g++-mingw-w64-i686 gcc-mingw-w64-i686 && \  
/opt/windev/bin/qt_build && \  
rm -rf /temp && \  
apt-get remove -y clang cmake nasm ninja-build perl wget && \  
apt-get autoremove -y && \  
apt-get autoclean  
  
RUN qtchooser -install -f qt5-x86_64-w64-mingw32
${WDEVPREFIX}/qt64d_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f qt5-i686-w64-mingw32
${WDEVPREFIX}/qt32d_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f 5 ${WDEVPREFIX}/qt32d_${QT_SERIES}.${QT_BUILD}/bin/qmake
&& \  
qtchooser -install -f qt5
${WDEVPREFIX}/qt32d_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
qtchooser -install -f default
${WDEVPREFIX}/qt32d_${QT_SERIES}.${QT_BUILD}/bin/qmake && \  
ln -s ${WDEVPREFIX}/libjpeg-turbo-${LIBJPEGTURBO_VERSION}_qt32d
${WDEVPREFIX}/libjpeg-turbo-latest_qt32d && \  
ln -s ${WDEVPREFIX}/libjpeg-turbo-${LIBJPEGTURBO_VERSION}_qt64d
${WDEVPREFIX}/libjpeg-turbo-latest_qt64d && \  
ln -s ${WDEVPREFIX}/libressl-${LIBRESSL_VERSION}_qt32d ${WDEVPREFIX}/libressl-
latest_qt32d && \  
ln -s ${WDEVPREFIX}/libressl-${LIBRESSL_VERSION}_qt64d ${WDEVPREFIX}/libressl-
latest_qt64d && \  
ln -s ${WDEVPREFIX}/qt32d_${QT_SERIES}.${QT_BUILD} ${WDEVPREFIX}/qt32d-latest
&& \  
ln -s ${WDEVPREFIX}/qt64d_${QT_SERIES}.${QT_BUILD} ${WDEVPREFIX}/qt64d-latest  
  
CMD ["/bin/bash"]  

