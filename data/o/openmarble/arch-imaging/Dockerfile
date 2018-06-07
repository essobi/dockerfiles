# arch-imaging  
  
FROM openmarble/arch-core:latest  
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>  
  
RUN pacman -Syuq --noconfirm --needed \  
libxslt libxml2 libexif fftw lcms2 libwebp libtiff cfitsio libgsf exiv2 libwmf
ghostscript freeglut \  
openexr glib2 libxml2 libjpeg libpng librsvg imagemagick orc openexr pango
openjpeg2 && \  
pacman --noconfirm -S 'curl' 'geos' 'giflib' 'hdf5' 'libgeotiff' 'libjpeg'
'libpng' 'libtiff' 'netcdf' 'python2' 'python2-numpy' 'cfitsio' 'sqlite3'
'libmariadbclient' 'postgresql-libs' 'podofo' 'perl' 'swig' 'chrpath' && \  
pacman -Sc --noconfirm  
  
RUN sudo -u build pacaur --noedit --noconfirm -S libecwj2 && \  
pacman -Sc --noconfirm  
  
RUN cd / build && \  
curl -LO kakadusoftware.com/wp-
content/uploads/2014/06/KDU77_Demo_Apps_for_Linux-x86-64_150710.zip && \  
unzip KDU77_Demo_Apps_for_Linux-x86-64_150710.zip && \  
cd KDU77_Demo_Apps_for_Linux-x86-64_150710 && \  
cp kdu_* /usr/bin && \  
cp *.so /usr/lib && \  
cd / && \  
rm -rf /build/*  
  
WORKDIR /usr/local/lib  
RUN wget --no-check-certificate https://github.com/loris-
imageserver/loris/raw/development/lib/Linux/x86_64/libkdu_v74R.so \  
&& chmod 755 libkdu_v74R.so  
  
WORKDIR /usr/local/bin  
RUN wget --no-check-certificate https://github.com/loris-
imageserver/loris/raw/development/bin/Linux/x86_64/kdu_expand \  
&& chmod 755 kdu_expand  
  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig  
  
  
RUN cd / build && \  
curl -LO download.osgeo.org/gdal/2.0.1/gdal-2.0.1.tar.xz && \  
tar -xvf gdal-2.0.1.tar.xz && \  
cd gdal-2.0.1 && \  
./configure --prefix=/usr --with-netcdf --with-libtiff --with-sqlite3 \  
\--with-geotiff --with-mysql --with-python=/usr/bin/python2 \  
\--with-curl --with-hdf5 --with-perl --with-geos \  
\--with-png --with-podofo --with-spatialite && \  
make && \  
make install && \  
cd / && \  
rm -rf /build/*  
  

