# vim: ft=dockerfile tw=78 ts=4 sw=4 et  
FROM sebgod/mercury-stable:14.01.1  
MAINTAINER Sebastian Godelet <sebastian.godelet@outlook.com>  
ENV MERCURY_STABLE_CROSS_VERSION $MERCURY_STABLE_VERSION-i686-w64-mingw32  
ENV MERCURY_STABLE_CROSS_PREFIX $MERCURY_STABLE_PREFIX-i686-w64-mingw32  
WORKDIR $MERCURY_TMP/mercury  
RUN tar --strip 1 -x -f $MERCURY_TMP/tarballs/$MERCURY_STABLE_TARGZ \  
&& aclocal -I m4 \  
&& autoconf \  
&& (sh tools/configure_mingw_cross \  
\--host=i686-w64-mingw32 \  
\--enable-libgrades=asm_fast.gc \  
\--with-default-grade=asm_fast.gc \  
\--enable-new-mercuryfile-struct \  
\--prefix=$MERCURY_STABLE_CROSS_PREFIX > build.log \  
&& make >> build.log \  
&& make install >> build.log \  
&& ln -s $MERCURY_STABLE_PREFIX/bin/mercury_compile \  
$MERCURY_STABLE_CROSS_PREFIX/bin \  
&& rm -fR * \  
) || (tail build.log & false)  
ENV PATH ${MERCURY_STABLE_CROSS_PREFIX}/bin:$PATH  
ENTRYPOINT ["mmc"]  

