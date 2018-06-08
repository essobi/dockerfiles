FROM ubuntu:16.04  
MAINTAINER Peter Mescalchin <peter@magnetikonline.com>  
  
ENV VERSION 3.3.1  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes autoconf checkinstall libpng12-dev libtool make nasm
pkg-config && \  
apt-get clean  
  
ADD https://github.com/mozilla/mozjpeg/archive/v$VERSION.tar.gz /root/build/  
WORKDIR /root/build  
RUN tar --extract --file v$VERSION.tar.gz  
  
WORKDIR /root/build/mozjpeg-$VERSION  
RUN autoreconf -fiv  
RUN mkdir build  
WORKDIR /root/build/mozjpeg-$VERSION/build  
RUN ../configure && make  
  
RUN echo "magnetikonline: mozjpeg" >description-pak && \  
checkinstall \  
\--default \  
\--install=no \  
\--nodoc \  
\--pkgname=mozjpeg \  
\--pkgversion=$VERSION \  
\--type=debian \  
make --ignore-errors install  
  
CMD ["/bin/bash"]  

