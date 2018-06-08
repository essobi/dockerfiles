FROM fedora:27  
MAINTAINER Georg Sauthoff <mail@georg.so>  
  
# note that mingw64-cmake/make implicitly depends on cmake/make  
RUN dnf -y install \  
bison \  
cmake \  
findutils \  
flex \  
git \  
make \  
mingw64-boost \  
mingw64-gcc \  
mingw64-gcc-c++ \  
mingw64-libxml2 \  
mingw64-qt5-qtbase-devel \  
mingw64-qt5-qtsvg \  
mingw64-qt5-qttools-tools \  
procps-ng \  
ragel \  
&& dnf clean all  
  
# mount points for mapping source code and  
# build directories  
RUN mkdir /srv/{src,build}  
  
# on fedora should reliable get uid/gid 1000  
RUN useradd -m compile-user  
USER compile-user  
WORKDIR /home/compile-user  
ENTRYPOINT [ "/usr/bin/sleep"]  
# default argument to entrypoint - possible values: 1h, 1d, inf, infinity, ...  
CMD [ "infinity" ]  

