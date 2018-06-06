FROM debian:jessie-slim  
  
MAINTAINER Francesco Serafin <francesco.serafin.3@gmail.com>, Olaf David
<odavid@colostate.edu>  
  
RUN set -x \  
\  
&& apt-get -y update \  
\  
# installation of required packages  
&& apt-get install --no-install-recommends -y \  
ca-certificates \  
wget \  
binutils \  
make \  
cmake \  
g++ \  
gcc \  
libproj-dev \  
libboost-regex1.55-dev \  
libboost-program-options1.55-dev \  
libboost-filesystem1.55-dev \  
libboost-system1.55-dev \  
libboost-iostreams1.55-dev \  
libboost-test1.55-dev \  
\  
# download and unpack MeteoIO 2.5.1  
&& wget https://models.slf.ch/p/meteoio/downloads/get/MeteoIO-2.5.1-src.tar.gz
\  
&& tar xvf MeteoIO-2.5.1-src.tar.gz meteoio \  
# build and install MeteoIO 2.5.1  
&& ( \  
cd meteoio \  
&& cmake -DBUILD_SHARED_LIBS:BOOL=ON \  
-DBUILD_STATIC_LIBS:BOOL=OFF \  
-DBUILD_TESTING:BOOL=OFF \  
-DCMAKE_BUILD_TYPE="minsizerel" \  
-DCMAKE_INSTALL_PREFIX="/usr" \  
-DDATA_QA:BOOL=OFF \  
-DDEST="safe" \  
-DGUI_EXCEPTIONS:BOOL=OFF \  
-DINSTALL_DOC:BOOL=OFF \  
-DLEAKS_CHECK:BOOL=OFF \  
-DPLUGIN_A3DIO:BOOL=ON \  
-DPLUGIN_ALPUG:BOOL=ON \  
-DPLUGIN_ARCIO:BOOL=ON \  
-DPLUGIN_ARPSIO:BOOL=ON \  
-DPLUGIN_BORMAIO:BOOL=OFF \  
-DPLUGIN_CNRMIO:BOOL=OFF \  
-DPLUGIN_COSMOXMLIO:BOOL=OFF \  
-DPLUGIN_GEOTOPIO:BOOL=ON \  
-DPLUGIN_GRASSIO:BOOL=ON \  
-DPLUGIN_GRIBIO:BOOL=OFF \  
-DPLUGIN_GSNIO:BOOL=OFF \  
-DPLUGIN_IMISIO:BOOL=OFF \  
-DPLUGIN_NETCDFIO:BOOL=OFF \  
-DPLUGIN_PGMIO:BOOL=ON \  
-DPLUGIN_PNGIO:BOOL=OFF \  
-DPLUGIN_PSQLIO:BOOL=OFF \  
-DPLUGIN_SASEIO:BOOL=OFF \  
-DPLUGIN_SMETIO:BOOL=ON \  
-DPLUGIN_SNIO:BOOL=ON \  
-DPROJ4:BOOL=ON . \  
&& cmake -LAH \  
&& make -j4 install \  
) \  
\  
# download and unpack GEOtop 2.1  
&& wget https://github.com/geotopmodel/geotop/archive/TRIEST_release.tar.gz \  
&& tar xvf TRIEST_release.tar.gz \  
# build and install GEOtop 2.1  
&& ( \  
cd geotop-TRIEST_release \  
&& cmake -DBUILD_STATIC:BOOL=OFF \  
-DCMAKE_BUILD_TYPE="minsizerel" \  
-DCMAKE_INSTALL_PREFIX="/usr" \  
-DENABLE_INTERNAL_METEODISTR:BOOL=OFF \  
-DMETEOIO_OUTPUT:BOOL=OFF \  
-DMETEOIO_PATH="/usr" \  
-DVERBOSE:BOOL=OFF \  
-DVERY_VERBOSE=OFF \  
-DCMAKE_CXX_FLAGS_RELEASE="-Wextra -Wall -O2 -Wno-unused-parameter \  
-Wno-unused-function -Wno-unused-result \  
-Wno-unused-but-set-variable" . \  
&& make -j4 install \  
) \  
\  
# clean up donwloaded packages and installation folders  
&& rm -rf meteoio \  
geotop-TRIEST_release \  
MeteoIO-2.5.1-src.tar.gz \  
TRIEST_release.tar.gz \  
\  
# purge obsolete packages  
&& apt-get -y remove --purge \  
ca-certificates \  
wget \  
binutils \  
make \  
cmake \  
g++ \  
gcc \  
libboost-regex1.55-dev \  
libboost-program-options1.55-dev \  
libboost-filesystem1.55-dev \  
libboost-system1.55-dev \  
libboost-iostreams1.55-dev \  
libboost-test1.55-dev \  
\  
# purge not needed packages  
&& apt-get -y autoremove --purge \  
\  
# install only required libraries without API  
&& apt-get install --no-install-recommends -y \  
libboost-regex1.55.0 \  
libboost-program-options1.55.0 \  
libboost-filesystem1.55.0 \  
libboost-system1.55.0 \  
libboost-iostreams1.55.0  
  
RUN mkdir /work  
CMD ["/usr/bin/geotop", "/work" ]  

