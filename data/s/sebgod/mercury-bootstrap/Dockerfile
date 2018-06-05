# vim: ft=dockerfile tw=78 ts=4 sw=4 et  
FROM sebgod/mercury-depend-essential:latest  
ENV MERCURY_TMP /var/tmp  
ENV MERCURY_DOWNLOAD_URL http://dl.mercurylang.org  
ENV MERCURY_BOOTSTRAP_VERSION 2017-10-19  
ENV MERCURY_BOOTSTRAP_TARGZ mercury-srcdist-
rotd-${MERCURY_BOOTSTRAP_VERSION}.tar.gz  
ENV MERCURY_BOOTSTRAP_PREFIX /usr/local/mercury-bootstrap  
ENV PATH_ORIG $PATH  
ENV PATH ${MERCURY_BOOTSTRAP_PREFIX}/bin:$PATH_ORIG  
RUN mkdir -p $MERCURY_TMP/mercury  
WORKDIR $MERCURY_TMP/mercury  
  
RUN curl -sL $MERCURY_DOWNLOAD_URL/rotd/$MERCURY_BOOTSTRAP_TARGZ | \  
tar --strip 1 -z -x \  
&& (sh configure --enable-minimal-install \  
\--prefix=$MERCURY_BOOTSTRAP_PREFIX > build.log 2>&1 \  
&& make >> build.log 2>&1 \  
&& make install >> build.log 2>&1 \  
&& rm -fR * \  
) || (cat build.log & false)  
  
ENTRYPOINT ["mmc"]

