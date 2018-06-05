FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
patch \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG C.UTF-8  
ENV GEOFILES /opt/geosupport/server/current/fls/  
ENV GEOSUPPORT_HOME /opt/geosupport  
ENV GEOSUPPORT_RELEASE 17a  
ENV GEOSUPPORT_VERSION 17.1  
  
ADD ./headers.patch "${GEOSUPPORT_HOME}/server/headers.patch"  
  
RUN set -o errexit -o nounset \  
echo "Downloading Geosupport" \  
&& mkdir -p "${GEOSUPPORT_HOME}/server" \  
&& cd "${GEOSUPPORT_HOME}/server" \  
&& wget -q -O geosupport.zip
"http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-
data/gdelx_${GEOSUPPORT_RELEASE}.zip" \  
\  
&& echo "Installing Geosupport" \  
&& unzip geosupport.zip \  
&& rm geosupport.zip \  
\  
&& echo "Patching Geosupport" \  
&& patch -b -p0 < headers.patch \  
&& rm headers.patch \  
\  
&& echo "Creating symlinks from system directories" \  
&& ln -nfs
"${GEOSUPPORT_HOME}/server/version-${GEOSUPPORT_RELEASE}_${GEOSUPPORT_VERSION}"
"${GEOSUPPORT_HOME}/server/current" \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/include/foruser/geo.h"
/usr/include/geo.h \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/include/foruser/NYCgeo.h"
/usr/include/NYCgeo.h \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/include/foruser/pac.h"
/usr/include/pac.h \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/include/foruser/wa_fields.h"
/usr/include/wa_fields.h \  
\  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libapequiv.so"
/usr/lib/libapequiv.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libedequiv.so"
/usr/lib/libedequiv.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libgeo.so"
/usr/lib/libgeo.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libNYCgeo.so"
/usr/lib/libNYCgeo.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libsan.so"
/usr/lib/libsan.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libsnd.so"
/usr/lib/libsnd.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libStdLast.so"
/usr/lib/libStdLast.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libStdUniv.so"
/usr/lib/libStdUniv.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libstEnder.so"
/usr/lib/libstEnder.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libstExcpt.so"
/usr/lib/libstExcpt.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libstretch.so"
/usr/lib/libstretch.so \  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/lib/libthined.so"
/usr/lib/libthined.so \  
\  
&& ln -nfs "${GEOSUPPORT_HOME}/server/current/bin/c_client" /usr/bin/goat  
  
VOLUME ["${GEOSUPPORT_HOME}/server/current"]  

