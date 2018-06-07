FROM ruby:2.4  
MAINTAINER yamaguchi@vic.co.jp  
  
WORKDIR /tmp  
  
ENV GEOS_VER 3.5.1  
ENV PROJ_VER 4.9.3  
ENV GDAL_VER 2.1.2  
RUN curl http://download.osgeo.org/geos/geos-${GEOS_VER}.tar.bz2 | tar jxf - \  
&& cd geos-${GEOS_VER} \  
&& ./configure \  
&& make -j $(nproc) \  
&& make install \  
&& cd .. \  
&& rm -rf geos-${GEOS_VER}  
  
RUN curl http://download.osgeo.org/proj/proj-${PROJ_VER}.tar.gz | tar zxf - \  
&& cd proj-${PROJ_VER} \  
&& ./configure \  
&& make -j $(nproc) \  
&& make install \  
&& cd .. \  
&& rm -rf proj-${PROJ_VER}  
  
RUN curl http://download.osgeo.org/gdal/${GDAL_VER}/gdal-${GDAL_VER}.tar.gz |
tar zxf - \  
&& cd gdal-${GDAL_VER} \  
&& ./configure \  
&& make -j $(nproc) \  
&& make install \  
&& cd .. \  
&& rm -rf gdal-${GDAL_VER}  
  
RUN ldconfig  
  
RUN echo "deb http://deb.debian.org/debian unstable main contrib non-free" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install \  
-y --no-install-recommends \  
postgresql-client \  
nodejs \  
npm \  
gfortran \  
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10 \  
&& npm install -g bower uglify-es \  
&& npm cache clean \  
&& echo '{ "allow_root": true }' > /root/.bowerrc \  
&& gem update --system  
  
WORKDIR /  
CMD ["/bin/bash"]  

