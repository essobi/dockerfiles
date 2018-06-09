FROM golang:alpine as build  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
RUN echo "@edge-testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update  
  
RUN apk add wget gcc make libc-dev sqlite-dev zlib-dev libxml2-dev
"proj4-dev@edge-testing" "geos-dev@edge-testing" "gdal-dev@edge-testing"
"gdal@edge-testing" expat-dev readline-dev ncurses-dev readline-static
ncurses-static libc6-compat  
  
RUN wget "http://www.gaia-gis.it/gaia-sins/freexl-1.0.4.tar.gz" && tar zxvf
freexl-1.0.4.tar.gz && cd freexl-1.0.4 && ./configure && make && make install  
  
RUN wget "http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz" && tar
zxvf libspatialite-4.3.0a.tar.gz && cd libspatialite-4.3.0a && ./configure &&
make && make install  
  
RUN wget "http://www.gaia-gis.it/gaia-sins/readosm-1.1.0.tar.gz" && tar zxvf
readosm-1.1.0.tar.gz && cd readosm-1.1.0 && ./configure && make && make
install  
  
RUN wget "http://www.gaia-gis.it/gaia-sins/spatialite-tools-4.3.0.tar.gz" &&
tar zxvf spatialite-tools-4.3.0.tar.gz && cd spatialite-tools-4.3.0 &&
./configure && make && make install  
  
RUN mv /usr/local/bin/* /usr/bin/  
RUN mv /usr/local/lib/*.so /usr/lib/  
RUN mv /usr/local/lib/*.a /usr/lib/  
  
ADD . /go/src/github.com/terranodo/tegola  
RUN cd /go/src/github.com/terranodo/tegola/cmd/tegola; go build -o tegola; cp
tegola /usr/bin  
  
RUN apk del gcc make  
  
# Create a minimal instance  
FROM alpine  
  
COPY \--from=build /usr/lib/ /usr/lib  
COPY \--from=build /usr/bin/ /usr/bin  

