FROM zubnix/jni-cross-compilers:linux-source  
MAINTAINER Erik De Rijcke "derijcke.erik@gmail.com"  
ENV CROSS_TRIPLE aarch64-linux-gnu  
ENV CROSS_ROOT /usr/toolchain  
ENV SYS_ROOT ${CROSS_ROOT}/${CROSS_TRIPLE}/libc  
  
#we can not cross compile 'the right way' as libxcb can not properly find it's
headers & sources  
#ENV PREFIX /usr  
#RUN export PKG_CONFIG_DIR=  
#ENV PKG_CONFIG_LIBDIR
${SYS_ROOT}${PREFIX}/lib/pkgconfig:${SYS_ROOT}${PREFIX}/share/pkgconfig  
#ENV PKG_CONFIG_SYSROOT_DIR ${SYS_ROOT}  
#workaround PKG_CONFIG setup for libxcb:  
ENV PREFIX ${SYS_ROOT}/usr  
ENV PKG_CONFIG_PATH ${PREFIX}/lib/pkgconfig:${PREFIX}/share/pkgconfig  
  
#linaro armv8_64  
WORKDIR ${CROSS_ROOT}  
ENV CROSS_COMPILER gcc-linaro-4.8-2015.06-x86_64_aarch64-linux-gnu.tar.xz  
COPY ${CROSS_COMPILER} ${CROSS_ROOT}  
RUN tar xv -C ${CROSS_ROOT} \--strip-components 1 -f ${CROSS_COMPILER}  
  
ENV PATH ${CROSS_ROOT}/bin:${PATH}  
  
#setup cmake toolchain file  
COPY Toolchain.cmake ${CROSS_ROOT}/  
ENV CMAKE_TOOLCHAIN_FILE ${CROSS_ROOT}/Toolchain.cmake  
  
#build libffi cross (jdk cross dep)  
WORKDIR /usr/src/libffi  
RUN ./autogen.sh && \  
./configure --host=${CROSS_TRIPLE} \--with-sysroot=${SYS_ROOT}
\--prefix=${PREFIX} && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/libffi  
  
#build freetype cross (jkd cross dep)  
WORKDIR /usr/src/freetype  
RUN cmake -DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE} \  
-DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \  
-DBUILD_SHARED_LIBS:BOOL=true . && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/freetype  
  
#build alsa cross (jdk cross dep)  
WORKDIR /usr/src/alsa  
RUN CC=${CROSS_ROOT}/bin/${CROSS_TRIPLE}-gcc ./configure
--host=${CROSS_TRIPLE} \--prefix=${PREFIX} && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/alsa  
  
#build zlib cross (X cross dep)  
WORKDIR /usr/src/zlib  
RUN AR=${CROSS_TRIPLE}-ar CC=${CROSS_TRIPLE}-gcc RANLIB=${CROSS_TRIPLE}-ranlib
./configure --prefix=${PREFIX} && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/zlib  
  
#build libpng cross (X cross dep)  
WORKDIR /usr/src/png  
RUN ./configure --prefix=${PREFIX} \--host=${CROSS_TRIPLE} && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/png  
  
#build expat cross (X cross dep)  
WORKDIR /usr/src/expat/conftools  
RUN cp -f /usr/share/misc/config.sub config.sub  
RUN cp -f /usr/share/misc/config.guess config.guess  
WORKDIR /usr/src/expat  
RUN AR=${CROSS_TRIPLE}-ar CC=${CROSS_TRIPLE}-gcc ./configure
--prefix=${PREFIX} \--host=${CROSS_TRIPLE} && \  
make && \  
make install && \  
cd /usr/src && \  
rm -rf /usr/src/expat  
  
#build openssl cross (X cross dep)  
WORKDIR /usr/src/openssl  
RUN ./Configure dist --prefix=${PREFIX} && \  
make CC="${CROSS_TRIPLE}-gcc" AR="${CROSS_TRIPLE}-ar r"
RANLIB="${CROSS_TRIPLE}-ranlib" && \  
make CC="${CROSS_TRIPLE}-gcc" AR="${CROSS_TRIPLE}-ar r"
RANLIB="${CROSS_TRIPLE}-ranlib" install_sw && \  
cd /usr/src && \  
rm -rf /usr/src/openssl  
  
#build X cross (jdk cross dep)  
WORKDIR /usr/src/xorg  
RUN CONFFLAGS="--disable-static \  
\--enable-malloc0returnsnull \  
\--host=${CROSS_TRIPLE} \  
\--prefix=${PREFIX} \  
\--build=x86_64-unknown-linux-gnu" \  
CC_FOR_BUILD="/usr/bin/gcc" \  
ACLOCAL="aclocal -I ${PREFIX}/share/aclocal/" \  
./build.sh --clone \--modfile xorg-modules && \  
cd /usr/src && \  
rm -rf /usr/src/xorg  
  
#build openjdk cross  
WORKDIR /usr/src  
RUN rm -rf jdk/  
RUN hg clone http://hg.openjdk.java.net/aarch64-port/jdk8u/ /usr/src/jdk  
  
WORKDIR /usr/src/jdk  
RUN chmod +x get_source.sh && \  
sync && \  
./get_source.sh  
  
#BUG. BUILD_CC and BUILD_LD will resolve from the cross root path, thus
building for the wrong arch.  
#Therefore we must set an absolute path.  
ENV BUILD_CC /usr/bin/gcc  
#BUG. BUILD_LD is not correctly used. Therefore we must set gcc as ld to make
it work  
ENV BUILD_LD /usr/bin/gcc  
  
#BUG. configure only looks for gcc/g++ named binaries not ones that may be
prefixed with a the devkit names eg:  
#x86_64-buildroot-linux-gnu-gcc. A workaround is to create symlinks for
gcc/g++  
#  
RUN ln -s ${CROSS_ROOT}/bin/${CROSS_TRIPLE}-gcc ${CROSS_ROOT}/bin/gcc && \  
ln -s ${CROSS_ROOT}/bin/${CROSS_TRIPLE}-g++ ${CROSS_ROOT}/bin/g++ && \  
  
#BUG. --disable-headful is ignored during build (X still required for
compiling and linking) and simply disables any  
#X checks during config, --with-x include is also ignored during build so we
have to cross compile X into the sysroot.  
#http://mail.openjdk.java.net/pipermail/build-dev/2012-March/005710.html  
#BUG. --with-cups-include is only used during configuration and is not
propagated to make when compiling  
#Therefore we just link the cups headers into our sysroot so they can be
resolved  
ln -s /usr/include/cups/ ${SYS_ROOT}/usr/include/ && \  
chmod +x configure && \  
sync && \  
./configure --with-devkit=${CROSS_ROOT} --openjdk-target=${CROSS_TRIPLE}
--with-tools-dir=${SYS_ROOT} \  
\--disable-freetype-bundling \  
\--with-cups-include=/usr/include/cups/ \  
\--with-freetype-include=${SYS_ROOT}/usr/include/freetype2 \  
\--with-freetype-lib=${SYS_ROOT}/usr/lib \  
\--with-jvm-variants=zero \  
\--disable-debug-symbols \  
\--with-jvm-interpreter=cpp \  
\--prefix=${PREFIX}/lib \  
&& \  
make images && \  
make install && \  
cd /usr && \  
rm -rf /usr/src/*  
  
RUN apt-get remove -y mercurial unzip zip git curl && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove -y  
  
COPY entrypoint.sh dockcross /dockcross/  
  
ENTRYPOINT ["/dockcross/entrypoint.sh"]  
WORKDIR /build

