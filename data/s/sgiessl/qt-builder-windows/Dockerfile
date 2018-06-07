FROM ubuntu:xenial  
  
# Increment in order to enforce rebuilding the build-environment (invalidating
cached docker layers).  
ENV REFRESHED_AT 2018-06-01  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
#########################  
### Update repository & install dependencies  
#########################  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y --force-yes \  
software-properties-common \  
runit \  
build-essential \  
ccache \  
cmake \  
git \  
vim \  
ninja-build \  
wget \  
gcc \  
g++ \  
&& apt-get clean  
  
#########################  
### QT win32 dev modules  
### Adapted from https://github.com/bboehmke/docker-mxe/blob/master/Dockerfile  
#########################  
WORKDIR /opt  
RUN git clone https://github.com/mxe/mxe.git  
RUN apt-get install --no-install-recommends -y --force-yes \  
autoconf automake autopoint bash bison bzip2 cmake flex \  
gettext git g++ gperf intltool libffi-dev libgdk-pixbuf2.0-dev \  
libtool libltdl-dev libssl-dev libxml-parser-perl make openssl \  
p7zip-full patch perl pkg-config python ruby scons sed \  
unzip wget xz-utils g++-multilib libc6-dev-i386 libtool-bin \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
WORKDIR /opt/mxe  
RUN make -j4 JOBS=4 MXE_TARGETS='i686-w64-mingw32.static' qtbase  
RUN make -j4 JOBS=4 MXE_TARGETS='i686-w64-mingw32.static' qtdeclarative  
RUN ln -s /opt/mxe/usr/bin/i686-w64-mingw32.static-qmake-qt5 /opt/mxe/usr/bin/  
  
#########################  
### Custom project dependencies....  
#########################  
RUN make -j4 JOBS=4 MXE_TARGETS='i686-w64-mingw32.static' libssh  
  
#########################  
### Convenience wrappers  
#########################  
ADD files/init files/wrap-user files/wrap-build-env /  
  
ENTRYPOINT ["/init"]  

