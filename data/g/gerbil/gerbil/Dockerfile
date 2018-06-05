from gerbil/base:latest  
  
MAINTAINER gerbil@cons.io  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN cd / && git clone https://github.com/gambit/gambit  
RUN cd / && git clone https://github.com/vyzo/gerbil  
  
RUN cd /gambit && ./configure --prefix=/usr/local/gambit --enable-single-host
--enable-c-opt --enable-gcc-opts --enable-multiple-versions --enable-openssl
--enable-default-runtime-options=f8,-8,t8 --enable-poll  
RUN cd /gambit && make -j4  
RUN cd /gambit && make install  
  
#RUN find /usr/local/gambit/ -ls  
ENV PATH "/usr/local/gambit/current/bin:$PATH"  
RUN cd /gerbil/src && ./build.sh stage0  
RUN cd /gerbil/src && ./build.sh stage1  
RUN sed -i -e 's/mysql #f/mysql #t/g' /gerbil/src/std/build-features.ss  
RUN sed -i -e 's/leveldb #f/leveldb #t/g' /gerbil/src/std/build-features.ss  
RUN sed -i -e 's/lmdb #f/lmdb #t/g' /gerbil/src/std/build-features.ss  
RUN sed -i -e 's/libyaml #f/libyaml #t/g' /gerbil/src/std/build-features.ss  
RUN cd /gerbil/src && ./build.sh stdlib  
RUN cd /gerbil/src && ./build.sh lang  
RUN cd /gerbil/src && ./build.sh tools  
RUN cd /gerbil/src && ./build.sh tags  
  
CMD /gerbil/bin/gxi  

