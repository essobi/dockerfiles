# vim: ft=dockerfile tw=78 ts=4 sw=4 et  
ARG MERCURY_BOOTSTRAP_TAG=latest  
FROM sebgod/mercury-bootstrap:${MERCURY_BOOTSTRAP_TAG} as bootstrap  
  
FROM sebgod/mercury-depend:${MERCURY_BOOTSTRAP_TAG}  
  
ENV MERCURY_TMP /var/tmp  
ARG MERCURY_DOWNLOAD_URL=http://dl.mercurylang.org  
ARG MERCURY_STABLE_VERSION=14.01.1  
ARG MERCURY_STABLE_DEFAULT_GRADE=asm_fast.gc  
ARG MERCURY_STABLE_LIBGRADES=${MERCURY_STABLE_DEFAULT_GRADE}  
  
ENV MERCURY_STABLE_TARGZ mercury-srcdist-${MERCURY_STABLE_VERSION}.tar.gz  
ENV MERCURY_STABLE_PREFIX /usr/local/mercury-stable  
ENV MERCURY_BOOTSTRAP_PREFIX /usr/local/mercury-bootstrap  
ENV PATH_ORIG $PATH  
ENV PATH ${MERCURY_BOOTSTRAP_PREFIX}/bin:$PATH  
  
COPY \--from=bootstrap ${MERCURY_BOOTSTRAP_PREFIX} ${MERCURY_BOOTSTRAP_PREFIX}  
  
WORKDIR $MERCURY_TMP/mercury  
  
RUN curl -sL $MERCURY_DOWNLOAD_URL/release/$MERCURY_STABLE_TARGZ | \  
tar --strip 1 -z -x \  
&& aclocal -I m4 \  
&& autoconf \  
&& (./configure \  
\--enable-libgrades=$MERCURY_STABLE_DEFAULT_GRADE \  
\--with-default-grade=$MERCURY_STABLE_LIBGRADES \  
\--prefix=$MERCURY_STABLE_PREFIX > build.log 2>&1 \  
&& make >> build.log 2>&1 \  
&& make install >> build.log 2>&1 \  
&& rm -fR * \  
&& rm -fR ${MERCURY_BOOTSTRAP_PREFIX} \  
) || (cat build.log & false)  
  
ENV PATH ${MERCURY_STABLE_PREFIX}/bin:${PATH_ORIG}  
  
ENTRYPOINT ["mmc"]  

