FROM fedora:27  
MAINTAINER Georg Sauthoff <mail@georg.so>  
  
# For now, we just use some core wine packages instead  
# of the meta package, to reduce the number of installed  
# packages.  
# wine \  
RUN dnf -y install \  
findutils \  
git \  
mingw64-boost \  
mingw64-gcc \  
mingw64-gcc-c++ \  
mingw64-libxml2 \  
mingw64-qt5-qtbase \  
mingw64-qt5-qtsvg \  
mingw64-qt5-qttools \  
procps-ng \  
wine-core \  
wine-common \  
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

