FROM ubuntu:xenial as build  
RUN apt-get update  
# try w w/o libc-dev to see differences  
RUN apt-get install -y build-essential gcc g++ flex subversion libgmp-dev
libmpfr-dev libmpc-dev  
WORKDIR /src  
RUN svn co svn://gcc.gnu.org/svn/gcc/branches/gccgo  
WORKDIR /build  
RUN ../src/gccgo/configure --enable-languages=c,c++,go --disable-multilib
--disable-bootstrap --prefix=/usr/local/gccgo  
RUN make -j 4  
# todo: run tests  
RUN make install  
  
FROM ubuntu:xenial  
COPY \--from=build /usr/local/gccgo /usr/local/gccgo  
ENV PATH /usr/local/gccgo/bin:$PATH  
RUN echo /usr/local/gccgo/lib64 > /etc/ld.so.conf.d/gccgo.conf  
RUN ldconfig  

