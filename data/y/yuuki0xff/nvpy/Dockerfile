FROM debian:sid as builder  
RUN echo "deb http://httpredir.debian.org/debian sid main"
>/etc/apt/sources.list  
RUN echo "deb-src http://httpredir.debian.org/debian sid main"
>>/etc/apt/sources.list  
  
# build settings  
ENV CFLAGS=-DTCL_UTF_MAX=6  
ENV MAKEFLAGS=-j5  
ENV TCL_VERSION=8.6.8  
ENV TK_VERSION=8.6.8  
ENV PY_BRANCH=2.7  
ENV PY_VERSION=2.7.14+  
  
# url  
ENV
TCL_URL=https://prdownloads.sourceforge.net/tcl/tcl${TCL_VERSION}-src.tar.gz  
ENV TK_URL=https://prdownloads.sourceforge.net/tcl/tk${TK_VERSION}-src.tar.gz  
ENV PY_URL=https://github.com/python/cpython/archive/${PY_BRANCH}.tar.gz  
  
# build options  
ENV PREFIX=/opt/nvpy  
ENV LD_LIBRARY_PATH=$PREFIX/lib  
RUN mkdir -p $PREFIX/bin $PREFIX/include $PREFIX/lib $PREFIX/share  
  
# install build dependencies.  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt update  
RUN apt -y upgrade  
RUN apt -y install build-essential checkinstall wget libx11-dev  
RUN apt -y build-dep -y tcl tk python2.7  
  
# download source codes.  
RUN mkdir /build/  
RUN wget "$TCL_URL" -O /build/tcl.tar.gz  
RUN tar xvf /build/tcl.tar.gz -C /build/  
RUN wget "$TK_URL" -O /build/tk.tar.gz  
RUN tar xvf /build/tk.tar.gz -C /build/  
RUN wget "$PY_URL" -O /build/cpython.tar.gz  
RUN tar xvf /build/cpython.tar.gz -C /build/  
  
# build TCL.  
WORKDIR /build/tcl${TCL_VERSION}/unix  
RUN ./configure --prefix=$PREFIX \--enable-threads --enable-shared --enable-
symbols --enable-64bit --enable-langinfo --enable-man-symlinks  
RUN make clean  
RUN make  
RUN make install  
  
# build TK.  
WORKDIR /build/tk${TK_VERSION}/unix  
RUN ./configure --prefix=$PREFIX \--enable-threads --enable-shared --enable-
symbols --enable-64bit --enable-man-symlinks  
RUN make clean  
RUN make  
RUN make install  
  
# build Cpython.  
WORKDIR /build/cpython-2.7  
RUN ./configure --prefix=$PREFIX \--enable-shared --enable-optimizations
--enable-ipv6 --enable-unicode=ucs4 --with-lto --with-signal-module --with-pth
--with-wctype-functions --with-tcltk-includes=/usr/local/include/ --with-
tcltk-libs=/usr/local/lib/  
RUN make clean  
RUN make  
RUN make install  
  
# install nvpy into container  
ADD https://github.com/cpbotha/nvpy/archive/master.tar.gz /tmp/nvpy.tar.gz  
RUN mkdir -p $PREFIX/lib/nvpy/  
RUN tar xf /tmp/nvpy.tar.gz -C $PREFIX/lib/nvpy/ --strip-components=1  
RUN \  
echo "#!/bin/sh" >/usr/local/bin/nvpy && \  
echo "export LD_LIBRARY_PATH=$PREFIX/lib" >>/usr/local/bin/nvpy && \  
echo "exec $PREFIX/bin/python2 $PREFIX/lib/nvpy/nvpy/nvpy.py"
>>/usr/local/bin/nvpy && \  
chmod +x /usr/local/bin/nvpy  
  
# make tarball  
RUN tar cv $PREFIX /usr/local/bin/nvpy |gzip --best >/output.tar.gz  
  
FROM busybox  
ENV PREFIX=/opt/nvpy  
COPY \--from=builder /output.tar.gz /output.tar.gz  
RUN \  
mkdir -p /usr/local/bin/ && \  
echo "#!/bin/sh" >/usr/local/bin/get-tarball && \  
echo "zcat /output.tar.gz" >>/usr/local/bin/get-tarball && \  
chmod +x /usr/local/bin/get-tarball  
  
CMD ["echo", "This image can not start nvPY.\nPlease execute \"sudo rm -rf
/opt/nvpy/ && docker run --rm yuuki0xff/nvpy get-tarball |sudo tar xvC /\" to
install nvPY."]  
  

