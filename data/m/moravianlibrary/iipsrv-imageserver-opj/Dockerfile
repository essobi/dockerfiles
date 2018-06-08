FROM debian:jessie  
  
ENV OPJ_DOWNLOAD_URL
https://github.com/uclouvain/openjpeg/archive/v2.3.0.tar.gz  
ENV IIPIMAGE_URL https://github.com/ruven/iipsrv.git  
  
RUN apt-get update && \  
apt-get install -y \  
libjpeg-turbo-progs \  
libpng-dev \  
libtiff-dev \  
libgomp1 \  
libmemcached-dev \  
liblcms2-dev \  
libtool \  
autoconf \  
pkg-config \  
cmake \  
build-essential \  
spawn-fcgi \  
wget \  
git \  
nano && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /openjpeg && \  
wget -qO- "$OPJ_DOWNLOAD_URL" | tar xz -C /openjpeg --strip-components 1 && \  
git clone https://github.com/ruven/iipsrv.git  
  
WORKDIR /openjpeg  
  
RUN cmake . -DCMAKE_BUILD_TYPE=Release && \  
make && \  
make install  
  
WORKDIR /iipsrv  
  
RUN ./autogen.sh && \  
./configure --with-openjpeg=/openjpeg && \  
make  
  
WORKDIR /  
  
RUN mkdir -p /usr/lib/cgi-bin/ && \  
cp /iipsrv/src/iipsrv.fcgi /usr/lib/cgi-bin/ && \  
rm -r /openjpeg /iipsrv && \  
ldconfig  
  
ENV LOGFILE=/tmp/iipsrv.log  
ENV CHILDREN=6  
ENV PORT=9000  
ENV FILESYSTEM_PREFIX=/data/  
ENV VERBOSITY=2  
ENV JPEG_QUALITY=90  
ENV MAX_IMAGE_CACHE_SIZE=10  
ENV MAX_CVT=30000  
ENV MAX_LAYERS=10  
ENV MEMCACHED_SERVERS=memcached  
  
RUN mkfifo /tmp/iipsrv.log  
COPY init.sh /init.sh  
CMD /init.sh  

