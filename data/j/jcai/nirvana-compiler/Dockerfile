FROM ubuntu:trusty  
MAINTAINER Jun Tsai <jcai@ganshane.com>  
  
ENV TEMPDIR /tmp  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.sohu.com/g' /etc/apt/sources.list &&
\  
apt-get -qq update && \  
apt-get install -qqy mingw-w64 g++-mingw-w64 git-core make wget cmake swig
openjdk-7-jdk  
  
#ssh_config  
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
RUN echo "UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config  
  
WORKDIR /build  
  
ADD Toolchain-cross-mingw32-linux.cmake /build/Toolchain-cross-
mingw32-linux.cmake  
RUN git clone \--depth=1 --branch=bitcoin-fork
https://github.com/bitcoin/leveldb.git  
  
RUN mkdir /build/mingw  
RUN mkdir /build/w32  
RUN mkdir /build/w64  
  
#build =============> 64bit  
ENV HOST x86_64-w64-mingw32  
ENV ARCH w64  
ENV CROSSPREFIX x86_64-w64-mingw32-  
  
#compile leveldb  
RUN { \  
cd /build/leveldb \  
&& CC=/usr/bin/${CROSSPREFIX}gcc CXX=${CROSSPREFIX}g++
TARGET_OS=OS_WINDOWS_CROSSCOMPILE make clean all \  
&& cp libleveldb.a /build/${ARCH} \  
&& cp -rp include/leveldb /build/mingw/ ;\  
}  
RUN { \  
wget http://lichen.egfit.com/nirvana/dll/${ARCH}/matchdll64.dll -O
/build/${ARCH}/matchdll64.dll \  
&& wget http://lichen.egfit.com/nirvana/dll/${ARCH}/tcprdll64.dll -O
/build/${ARCH}/tcprdll64.dll \  
&& wget http://lichen.egfit.com/nirvana/dll/${ARCH}/texfdll64.dll -O
/build/${ARCH}/texfdll64.dll ;\  
}  
  
#build =============> 32bit  
ENV HOST i686-w64-mingw32  
ENV ARCH w32  
ENV CROSSPREFIX i686-w64-mingw32-  
  
#compile leveldb  
RUN { \  
cd /build/leveldb \  
&& CC=/usr/bin/${CROSSPREFIX}gcc CXX=${CROSSPREFIX}g++
TARGET_OS=OS_WINDOWS_CROSSCOMPILE make clean all \  
&& cp libleveldb.a /build/${ARCH} \  
&& cp -rp include/leveldb /build/mingw/ ;\  
}  
RUN { \  
wget http://lichen.egfit.com/nirvana/dll/${ARCH}/matchdll.dll -O
/build/${ARCH}/matchdll.dll \  
&& wget http://lichen.egfit.com/nirvana/dll/${ARCH}/texfdll.dll -O
/build/${ARCH}/texfdll.dll \  
&& wget http://lichen.egfit.com/nirvana/dll/${ARCH}/tcprdll.dll -O
/build/${ARCH}/tcprdll.dll ;\  
}  
  
#clean some file  
RUN { \  
rm -rf /build/leveldb* ;\  
}  
  
#add header file  
RUN {\  
wget http://lichen.egfit.com/nirvana/kernel-header.tar.gz -O - |tar xvz -C
/build/mingw ; \  
}  
  
#remove libpwinthread  
RUN {\  
rm -rf /usr/i686-w64-mingw32/lib/libpthread.dll.a \  
&& rm -rf /usr/i686-w64-mingw32/lib/libwinpthread.dll.a \  
&& rm -rf /usr/i686-w64-ming32/lib/libwinpthread-1.dll \  
&& rm -rf /usr/x86_64-w64-mingw32/lib/libpthread.dll.a \  
&& rm -rf /usr/x86_64-w64-mingw32/lib/libwinpthread.dll.a \  
&& rm -rf /usr/x86_64-w64-ming32/lib/libwinpthread-1.dll ;\  
}  
  
VOLUME /dist  
WORKDIR /build/nirvana  
ADD compile.sh /compile.sh  
  
CMD ["sh","/compile.sh"]  
  

