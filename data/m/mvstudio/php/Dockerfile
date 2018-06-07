FROM mvstudio/php:5.6-alpine  
# fontforge (required by truck-transport, auto-salon)  
RUN apk \--no-cache add \  
linux-headers autoconf automake libjpeg-turbo-dev libpng-dev giflib-dev \  
tiff-dev libxt-dev freetype-dev libtool libltdl libxml2-dev python-dev \  
pango-dev coreutils m4 file gcc g++ make && \  
cd /tmp && \  
git clone https://github.com/fontforge/libspiro.git && \  
cd libspiro && \  
autoreconf -i && \  
automake \--foreign -Wall && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
git clone https://github.com/fontforge/libuninameslist.git && \  
cd libuninameslist && \  
autoreconf -i && \  
automake \--foreign && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
git clone https://github.com/BWITS/fontforge.git && \  
cd fontforge && \  
./bootstrap \--force && \  
./configure \--without-iconv && \  
make && \  
make install && \  
cd && rm -Rf /tmp/* && \  
apk \--no-cache del \--purge \  
linux-headers autoconf automake libjpeg-turbo-dev libpng-dev giflib-dev \  
tiff-dev libxt-dev freetype-dev libtool libltdl libxml2-dev python-dev \  
pango-dev coreutils m4 file gcc g++ make && \  
apk \--no-cache add \  
libpng python freetype glib libintl libxml2 libltdl cairo giflib pango  
  
# S6  
RUN apk \--no-cache add gcc g++ make && \  
curl -sSL http://skarnet.org/software/s6/s6-2.4.0.0.tar.gz | tar -C /tmp -xz
&& \  
curl -sSL http://skarnet.org/software/skalibs/skalibs-2.4.0.1.tar.gz | tar -C
/tmp -xz && \  
curl -sSL http://skarnet.org/software/execline/execline-2.2.0.0.tar.gz | tar
-C /tmp -xz && \  
cd /tmp/skalibs-2.4.0.1 && \  
./configure && make && make install && \  
cd /tmp/execline-2.2.0.0 && \  
./configure && make && make install && \  
cd /tmp/s6-2.4.0.0 && \  
./configure && make && make install && \  
cd && rm -Rf /tmp/* && \  
apk \--no-cache del \--purge gcc g++ make  

