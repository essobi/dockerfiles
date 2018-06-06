#  
FROM debian:jessie  
MAINTAINER Mateusz Juda <mateusz.juda@gmail.com>  
  
RUN echo "deb http://pkg.mxe.cc/repos/apt/debian/ jessie main" >
/etc/apt/sources.list.d/mxe.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
D43A795B73B16ABE9643FE1AFD8FFF16DB45C6AB  
  
# because of docker cache we have to update/upgrade just before install  
RUN apt-get update -y && apt-get upgrade -yy && DEBIAN_FRONTEND=noninteractive
apt-get install -yy mxe-x86-64-w64-mingw32.static-gcc
mxe-x86-64-w64-mingw32.static-gcc mxe-x86-64-unknown-linux-gnu-pkgconf
mxe-x86-64-unknown-linux-gnu-automake mxe-x86-64-unknown-linux-gnu-autoconf
mxe-x86-64-unknown-linux-gnu-libtool  
RUN apt-get update -y && apt-get upgrade -yy && DEBIAN_FRONTEND=noninteractive
apt-get install -yy mxe-x86-64-w64-mingw32.static-gcc
mxe-x86-64-w64-mingw32.static-gcc mxe-x86-64-unknown-linux-gnu-pkgconf
mxe-x86-64-unknown-linux-gnu-automake mxe-x86-64-unknown-linux-gnu-autoconf
mxe-x86-64-unknown-linux-gnu-libtool mxe-x86-64-w64-mingw32.static-wxwidgets
mxe-x86-64-w64-mingw32.static-mpfr mxe-x86-64-w64-mingw32.static-boost
mxe-x86-64-w64-mingw32.static-log4cxx  
RUN apt-get update -y && apt-get upgrade -yy && DEBIAN_FRONTEND=noninteractive
apt-get install -yy mxe-x86-64-w64-mingw32.static-gcc
mxe-x86-64-w64-mingw32.static-gcc mxe-x86-64-unknown-linux-gnu-pkgconf
mxe-x86-64-unknown-linux-gnu-automake mxe-x86-64-unknown-linux-gnu-autoconf
mxe-x86-64-unknown-linux-gnu-libtool mxe-x86-64-w64-mingw32.static-wxwidgets
mxe-x86-64-w64-mingw32.static-mpfr mxe-x86-64-w64-mingw32.static-boost
mxe-x86-64-w64-mingw32.static-log4cxx subversion  
  
  
  
ADD https://bitbucket.org/phat-code/phat/get/v1.4.1.tar.gz
/usr/local/src/phat.tar.gz  
# Copy PHAT to mxe compiler!!  
RUN cd /usr/local/src/ && tar xzf phat.tar.gz && \  
cp -fr /usr/local/src/phat*/include/phat
/usr/lib/mxe/usr/x86_64-w64-mingw32.static/include && rm -fr
/usr/local/src/phat*  
  
ENV MXE_VER=x86-64-w64-mingw32.static
CROSS_TARGET_HOST=x86_64-w64-mingw32.static
MXE_PKG_CONFIG_PATH_NAME=PKG_CONFIG_PATH_x86_64_w64_mingw32_static  
ENV PATH=/usr/lib/mxe/usr/bin/:"$PATH"  
# We need to pack archives  
RUN apt-get update -y && apt-get upgrade -yy && DEBIAN_FRONTEND=noninteractive
apt-get install -yy zip  

