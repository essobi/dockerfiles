FROM apiaryio/emcc:1.36  
run apt-get update; apt-get install -y \  
autoconf \  
automake \  
build-essential \  
curl \  
git \  
libtool \  
pkg-config  
  
run mkdir /fractal /fractal/prefix /fractal/source  
  
WORKDIR /fractal/source  
  
# ZLIB  
RUN curl -SL http://zlib.net/zlib-1.2.8.tar.gz | tar zxv && \  
cd zlib* && \  
emconfigure bash -c "CFLAGS=-O3 ./configure --prefix /fractal/prefix" && \  
emmake make -j $(nproc) && \  
emmake make install && \  
cd .. && \  
rm -rf zlib*  
  
# LIBPNG  
RUN curl -SL https://download.sourceforge.net/libpng/libpng-1.6.21.tar.gz |
tar zxv && \  
cd libpng* && \  
emconfigure bash -c "CPPFLAGS='-I/fractal/prefix/include/'
LDFLAGS='-L/fractal/prefix/lib' CFLAGS=-O3 ./configure
--prefix=/fractal/prefix --enable-shared=yes" && \  
emmake bash -c "CFLAGS='-L/fractal/prefix/lib/ -I/fractal/prefix/include' make
-j $(nproc)" && \  
emmake make install && \  
cd .. && \  
rm -rf libpng*  
  
# LIBJPEG  
RUN curl -SL https://download.sourceforge.net/libjpeg/jpegsrc.v6b.tar.gz | tar
zxv && \  
cd jpeg-6b && \  
cp /usr/share/automake-1.14/config.* . && \  
emconfigure bash -c "CFLAGS=-O3 ./configure --prefix=/fractal/prefix --enable-
shared" && \  
emmake make -j $(nproc) && \  
mkdir -p /fractal/prefix/man/man1 && \  
emmake make install && \  
cd .. && \  
rm -rf jpeg-6b  
  
# LIBGD2  
RUN curl -SL
https://github.com/libgd/libgd/releases/download/gd-2.2.3/libgd-2.2.3.tar.gz |
tar xzv && \  
cd libgd* && \  
emconfigure bash -c "CFLAGS='-Wno-error -O3'
PKG_CONFIG_LIBDIR=/fractal/prefix/lib/pkgconfig:$PKG_CONFIG_LIBDIR ./configure
--prefix /fractal/prefix --with-zlib --with-png --with-jpeg --enable-
shared=yes" && \  
emmake make -j $(nproc) && \  
emmake make install && \  
cd .. && \  
rm -rf libgd*  
  
# Fractal  
ARG branch=master  
  
RUN git clone http://github.com/allanlw/fractal.git && \  
cd fractal && \  
git checkout $branch && \  
autoreconf -i && \  
emconfigure bash -c "CPPFLAGS='-I/fractal/prefix/include'
LDFLAGS='-L/fractal/prefix/lib' CFLAGS=-O3 ./configure
--prefix=/fractal/prefix" && \  
emmake make -j $(nproc) && \  
cd .. && \  
mv fractal/src/fractal ./fractal.bc && \  
rm -rf fractal  
  
# Build output javascript  
ADD fractal-js/pre-js.js fractal-js/pre-js.js  
  
RUN cd fractal-js && \  
emcc -o fractal.js ../fractal.bc -L/fractal/prefix/lib/ \  
/fractal/prefix/lib/libz.so -lpng -ljpeg -lgd \  
\--pre-js pre-js.js -v -O3 --closure 1 \  
-s FORCE_FILESYSTEM=1 \  
-s EXPORTED_RUNTIME_METHODS="[]" \  
-s ALLOW_MEMORY_GROWTH=1 \  
-s DOUBLE_MODE=0 \  
-s DISABLE_EXCEPTION_CATCHING=1 \  
-s AGGRESSIVE_VARIABLE_ELIMINATION=1  
  
ADD fractal-js fractal-js  
WORKDIR fractal-js  
  
EXPOSE 8080  
CMD python -m SimpleHTTPServer 8080  

