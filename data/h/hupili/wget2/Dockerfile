FROM ubuntu:16.04  
MAINTAINER e@hupili.net  
  
ADD ./ wget2-docker/  
WORKDIR /wget2-docker/wget2/  
  
RUN apt-get update  
  
RUN apt-get install -y \  
autotools-dev \  
libtool \  
autoconf \  
python-dev \  
pkg-config \  
doxygen \  
gettext \  
libc6-dev \  
libz-dev \  
liblzma-dev \  
libbz2-dev \  
libgnutls-dev \  
libidn2-0-dev \  
flex \  
libpsl-dev \  
libnghttp2-dev \  
libmicrohttpd-dev \  
autopoint \  
git  
  
# Not in the system dist repo.  
# libbrotlidec >= 1.0.0 (optional, if you want HTTP brotli decompression)  
RUN ./bootstrap  
RUN ./configure --prefix=/usr  
RUN make -j 4  
RUN make install  
  
RUN mkdir -p /data  
  
WORKDIR /data  
  
ENTRYPOINT ["stdbuf", "-o", "0", "wget2"]

