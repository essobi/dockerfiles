#  
# flccsw/gdal  
#  
# This creates an Archlinux derived base image that installs the latest GDAL  
# Use Archlinux base image  
FROM base/devel  
  
MAINTAINER Fernando L. Canizo <fernandocanizo@gmail.com>  
  
# put needed files into the container  
COPY libkml-1.3.0-0-x86_64.pkg.tar.xz /tmp  
COPY gdal-with-libkml-2.2.3-1-x86_64.pkg.tar.xz /tmp  
  
# update system  
RUN pacman --noconfirm -Syu  
RUN pacman --noconfirm -S python2  
RUN pacman --noconfirm -U /tmp/libkml-1.3.0-0-x86_64.pkg.tar.xz  
RUN pacman --noconfirm -S postgresql-libs crypto++ libwebp unixodbc xerces-c
jasper minizip  
RUN pacman --noconfirm -U /tmp/gdal-with-libkml-2.2.3-1-x86_64.pkg.tar.xz  
  
# clean installation files  
RUN rm -f /tmp/libkml-1.3.0-0-x86_64.pkg.tar.xz /tmp/gdal-with-
libkml-2.2.3-1-x86_64.pkg.tar.xz  
  
# Externally accessible data is by default put in /data  
WORKDIR /data  
VOLUME ["/data"]  
  
# Output version and capabilities by default.  
CMD gdalinfo --version && gdalinfo --formats && ogrinfo --formats  

