FROM ubuntu:precise  
  
# Install prerequisites  
RUN apt-get update  
RUN apt-get -y install mingw-w64 g++-mingw-w64 git-core bzip2 zip faketime
psmisc curl make unzip nsis autoconf2.13 libtool automake pkg-config
bsdmainutils libc6-dev python-dev  
  
# Create build and output directories  
RUN mkdir -p /buildroot/build /buildroot/out  
ENV HOME /buildroot  
ENV OUTDIR /buildroot/out  
WORKDIR /buildroot/build  
  
# Download sources for additional dependencies  
RUN curl -L -O http://www.openssl.org/source/openssl-1.0.1h.tar.gz \  
-O http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz \  
-O http://cznic.dl.sourceforge.net/project/libpng/zlib/1.2.8/zlib-1.2.8.tar.gz \  
-O http://garr.dl.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.bz2 && \  
curl https://svn.boost.org/trac/boost/raw-attachment/ticket/7262/boost-
mingw.patch >boost-mingw-gas-cross-compile-2013-03-03.patch  
  
# Build dependencies  
ENV REFERENCE_DATETIME "2011-01-30 00:00:00"  
ADD deps-win.sh /tmp/  
RUN /tmp/deps-win.sh  
  
# Build boost  
ADD boost-win.sh /tmp/  
RUN /tmp/boost-win.sh  
  
# Build Twister (with libtorrent)  
RUN git clone https://github.com/miguelfreitas/twister-core.git  
ENV REFERENCE_DATETIME "2013-06-01 00:00:00"  
ADD gitian-win.sh /tmp/  
RUN /tmp/gitian-win.sh  
  
# Copy output to target folder upon run  
CMD cp -a $OUTDIR/* /target/  

