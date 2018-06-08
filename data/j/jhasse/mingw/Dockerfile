FROM fedora:25  
RUN dnf update -y && dnf install -y \  
mingw64-libgomp \  
mingw64-bzip2-static \  
mingw64-zlib-static \  
mingw64-libpng-static \  
mingw64-libjpeg-turbo-static \  
mingw64-libtiff-static \  
mingw64-expat-static \  
mingw64-freetype-static \  
mingw64-dlfcn \  
mingw64-boost \  
mingw64-gcc-gfortran \  
mingw64-openssl-static \  
mingw64-winpthreads-static \  
git \  
sshpass \  
wine-core \  
autogen \  
p7zip-plugins && dnf clean all  
  
RUN ln -s /usr/bin/x86_64-w64-mingw32-ar /usr/local/bin/ar  
RUN ln -s /usr/bin/x86_64-w64-mingw32-strip /usr/local/bin/strip  
  
ENV CC x86_64-w64-mingw32-gcc  
ENV CXX x86_64-w64-mingw32-c++  
ENV FC x86_64-w64-mingw32-gfortran  
ENV RC x86_64-w64-mingw32-windres  
  
ENV LANG C.UTF-8  
COPY wxWidgets.sh /tmp  
RUN cd /tmp && /tmp/wxWidgets.sh && rm /tmp/wxWidgets.sh  

