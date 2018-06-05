FROM avalverde/cross-compiler-windows-x86  
# fork of thewtex/cross-compiler-windows-x86 which enables POSIX threads  
WORKDIR /tmp  
  
#  
# Prepare the cross-compilation environment  
#  
RUN : "Install i386 libs and some deps " \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get -y install \  
gcc-multilib \  
libc6:i386 \  
ncurses-dev:i386 \  
libgmp-dev:i386 \  
libbz2-dev:i386 \  
libz-dev:i386 \  
&& : "Install libgmp-mingw32" && cd /usr/src/mxe && make gmp \  
&& : "Clean up to keep the image small" && apt-get clean  
  
RUN : "Add non-root user" \  
&& adduser --disabled-password --shell /bin/bash --uid 1000 xghc  
  
#  
# Install a i386-linux GHC to create the cross-compiler. Is is very important  
# that the word sizes match for GHC's external interpreter to work  
#  
ENV GHC_VERSION=8.0.1 \  
STACK_RESOLVER=nightly-2016-07-01  
COPY wrappers/ /usr/src/mxe/usr/bin/  
# We bundle stack because hub.docker.com says it cannot resolve stackage.org  
COPY stack.xz /tmp/  
RUN : "Download and unpack i386-linux GHC from binary distribution" \  
&& curl -L
https://downloads.haskell.org/~ghc/${GHC_VERSION}/ghc-${GHC_VERSION}-i386-deb8-linux.tar.xz
| tar xvJ \  
&& cd /tmp/ghc-${GHC_VERSION} \  
  
&& : "Configure and install i386-linux GHC from binary distribution" \  
&& ./configure --prefix=/usr/src/mxe/usr/i386-unknown-linux \  
\--with-gcc=/usr/src/mxe/usr/bin/i386-unknown-linux-gcc \  
\--with-as=/usr/src/mxe/usr/bin/i386-unknown-linux-as \  
\--with-ld=/usr/src/mxe/usr/bin/i386-unknown-linux-ld \  
&& make install \  
  
&& : "link to prefixed versions in PATH" \  
&& for bin in /usr/src/mxe/usr/i386-unknown-linux/bin/*; do \  
ln -s ${bin} /usr/src/mxe/usr/bin/i386-unknown-linux-$(basename ${bin}); done
\  
  
&& : "Install i386-unknown-linux-stack" \  
&& xz -d /tmp/stack.xz \  
&& chmod +x /tmp/stack \  
&& mv /tmp/stack /usr/local/bin \  
# | tar xz --wildcards --strip-components=1 \  
# -C /usr/src/mxe/usr/i386-unknown-linux/bin \  
# '*/stack' \  
&& : "Install i386-unknown-linux-cabal" \  
&& chown root /home/xghc \  
&& STACK_ROOT=/home/xghc/.stack i386-unknown-linux-stack \  
\--local-bin-path=/usr/local/bin \  
install cabal-install happy alex \  
&& chown -R xghc /home/xghc \  
&& : "Clean up to keep the image small" && rm -rf /tmp/*  
  
#  
# Build and install the GHC cross-compiler  
#  
ENV HOST_TRIPLE=i686-w64-mingw32 \  
WINDRES=/usr/src/mxe/usr/bin/${CROSS_TRIPLE}-windres  
RUN : "Prepare mingw32 cross-compiling env" \  
&& : "link to a CROSS_TRIPLE versions to HOST_TRIPLE versions because some " \  
"configure scripts choke on it" \  
&& for src in /usr/src/mxe/usr/bin/${CROSS_TRIPLE}-*; do \  
ln -s ${src} $(src=${src} bash -c 'echo
${src/${CROSS_TRIPLE}/${HOST_TRIPLE}}'); \  
done \  
&& : "Wrap windres so it gets the path to the cross system includes" \  
&& echo '#!/bin/bash' >> /usr/local/bin/windres \  
&& echo 'exec $WINDRES -I/usr/src/mxe/usr/i686-w64-mingw32.static/include
"$@"' >> /usr/local/bin/windres \  
&& chmod +x /usr/local/bin/windres \  
&& : "Symlink header since some step expects it with a different case" \  
&& ln -s /usr/src/mxe/usr/${CROSS_TRIPLE}/include/shlobj.h \  
/usr/src/mxe/usr/${CROSS_TRIPLE}/include/Shlobj.h  
  
COPY patches/ /tmp/patches/  
COPY build.mk /tmp/  
RUN : "Download source to build cross-compiler" \  
&& curl -L
https://www.haskell.org/ghc/dist/${GHC_VERSION}/ghc-${GHC_VERSION}-src.tar.xz
\  
| tar xvJ \  
&& cd /tmp/ghc-${GHC_VERSION} \  
&& : "Apply patches for cross-compiling, copy configuration file and
configure" \  
&& for p in /tmp/patches/ghc/*.patch; do patch -p1 -i ${p}; done \  
&& for p in /tmp/patches/hsc2hs/*.patch; do patch -p1 -d utils/hsc2hs -i ${p};
done \  
&& autoreconf \  
&& cp /tmp/build.mk mk/build.mk \  
&& ./configure --target=${HOST_TRIPLE} \  
\--prefix=/usr/src/mxe/usr \  
\--with-ghc=i386-unknown-linux-ghc \  
\--with-emulator=$(which wine) \  
\--with-gmp-includes=/usr/src/mxe/usr/include \  
\--with-gmp-libraries=/usr/src/mxe/usr/lib \  
&& : "Build and install cross-compiler" \  
&& make -j8 \  
&& make install \  
&& : "Clean up to keep the image small" && rm -rf /tmp/*  
  
COPY TestTH.hs /tmp/  
RUN : "Test that we can cross-compile TemplateHaskell" \  
&& ${HOST_TRIPLE}-ghc --make TestTH.hs -fexternal-interpreter \  
&& wine TestTH.exe \  
&& : "Clean up to keep the image small" && rm -rf /tmp/*  
  
USER xghc  
ENV PATH /home/xghc/.local/bin:${PATH}  
WORKDIR /home/xghc  
  
CMD ["bash"]  

