FROM m03geek/ffmpeg-opencv:alpine  
  
ARG RUNTIME_DEPS='libpng libjpeg-turbo giflib openblas libx11'  
ARG BUILD_DEPS='wget unzip cmake build-base linux-headers libpng-dev libjpeg-
turbo-dev giflib-dev openblas-dev libx11-dev'  
ARG LIB_PREFIX='/usr/local'  
ARG VERSION  
  
ENV DLIB_VERSION=${VERSION} \  
LIB_PREFIX=${LIB_PREFIX} \  
DLIB_INCLUDE_DIR='$LIB_PREFIX/include' \  
DLIB_LIB_DIR='$LIB_PREFIX/lib'  
RUN echo "Dlib: ${DLIB_VERSION}" \  
&& rm -rf /usr/local/lib && ln -s /usr/local/lib64 /usr/local/lib \  
&& apk add -u --no-cache $RUNTIME_DEPS \  
&& apk add -u --no-cache --virtual .build-dependencies $BUILD_DEPS \  
&& wget -q https://github.com/davisking/dlib/archive/v${DLIB_VERSION}.zip -O
dlib.zip \  
&& dlib_cmake_flags="-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=$LIB_PREFIX \  
-D DLIB_NO_GUI_SUPPORT=OFF \  
-D DLIB_USE_BLAS=ON \  
-D DLIB_GIF_SUPPORT=ON \  
-D DLIB_PNG_SUPPORT=ON \  
-D DLIB_JPEG_SUPPORT=ON \  
-D DLIB_USE_CUDA=OFF" \  
&& unzip -qq dlib.zip \  
&& mv dlib-${DLIB_VERSION} dlib \  
&& rm dlib.zip \  
&& cd dlib \  
&& mkdir -p build \  
&& cd build \  
&& cmake $dlib_cmake_flags .. \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& cd /dlib/build \  
&& make install \  
&& cp /dlib/dlib/*.txt $LIB_PREFIX/include/dlib/ \  
&& cd / \  
&& rm -rf /dlib \  
&& /usr/glibc-compat/sbin/ldconfig \  
&& apk del .build-dependencies \  
&& rm -rf /var/cache/apk/* /usr/share/man /usr/local/share/man /tmp/*  

