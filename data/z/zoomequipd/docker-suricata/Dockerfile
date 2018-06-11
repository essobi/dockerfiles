FROM ubuntu:14.04  
MAINTAINER Brandon Murphy <github@zoomequipd.com>  
  
# Install depends  
RUN apt-get update && apt-get install -y \  
build-essential \  
autoconf \  
automake \  
netbase \  
bison \  
flex  
  
# Add source files  
ADD src/*gz /usr/local/src/  
  
# install specific version of major depends  
RUN cd /usr/local/src/file-5.22 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/file-5.22  
RUN cd /usr/local/src/LuaJIT-2.0.4 && make ; make install ; cd /usr/local/src
; rm -rf /usr/local/src/LuaJIT-2.0.4  
RUN cd /usr/local/src/libnet-1.2-rc3 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/libnet-1.2-rc3  
RUN cd /usr/local/src/libpcap-1.7.3 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/libpcap-1.7.3  
RUN cd /usr/local/src/zlib-1.2.8 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/zlib-1.2.8  
RUN cd /usr/local/src/pcre-8.37 && ./configure --enable-jit --enable-pcregrep-
libz --enable-pcre16 --enable-pcre32 --enable-utf --enable-unicode-properties
; make ; make install ; cd /usr/local/src ; rm -rf /usr/local/src/pcre-8.37  
RUN cd /usr/local/src/jansson-2.7 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/jansson-2.7  
RUN cd /usr/local/src/yaml-0.1.5 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/yaml-0.1.5  
RUN cd /usr/local/src/libcap-ng-0.7.7 && ./configure ; make ; make install ;
cd /usr/local/src ; rm -rf /usr/local/src/libcap-ng-0.7.7  
RUN cd /usr/local/src/libtool-2.4.6 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/libtool-2.4.6  
  
# Install pkg-config - avoiding using the 'bundled' version of glib with pkg-
config  
RUN cd /usr/local/src/libffi-3.2.1 && ./configure ; make ; make install ; cd
/usr/local/src ; rm -rf /usr/local/src/libffi-3.2.1  
RUN cd /usr/local/src/gettext-0.19.4 && ./configure ; make ; make install;
ldconfig ; cd /usr/local/src ; rm -rf /usr/local/src/gettext-0.19.4  
ADD src/glib-2.44.1.tar.xz /usr/local/src/  
RUN cd /usr/local/src/glib-2.44.1 && ./configure
LIBFFI_LIBS="-L/usr/local/lib/ -lffi"
LIBFFI_CFLAGS="-I/usr/local/lib/libffi-3.2.1/include/" ; make ; make install ;
cd /usr/local/src ; rm -rf /usr/local/src/glib-2.44.1  
RUN cd /usr/local/src/pkg-config-0.28 && ./configure
GLIB_LIBS="-L/usr/local/lib -lglib-2.0"
GLIB_CFLAGS="-I/usr/local/include/glib-2.0 -I/usr/local/lib/glib-2.0/include"
; make ; make install ; cd /usr/local/src ; rm -rf /usr/local/src/pkg-
config-0.28  
  
# http://www.linuxfromscratch.org/blfs/view/svn/general/nspr.html  
RUN cd /usr/local/src/nspr-4.10.8/nspr && sed -ri 's#^(RELEASE_BINS =).*#\1#'
pr/src/misc/Makefile.in && sed -i 's#$(LIBRARY) ##' config/rules.mk &&
./configure --enable-ipv6 --enable-64bit --with-pthreads ; make ; make
install; ldconfig  
  
# http://www.linuxfromscratch.org/blfs/view/svn/postlfs/nss.html  
ADD src/nss-3.19.1-standalone-1.patch /usr/local/src/  
RUN cd /usr/local/src/nss-3.19.1/ && patch -Np1 -i
../nss-3.19.1-standalone-1.patch && cd nss && export BUILD_OPT=1 ; export
USE_64=1; export ZLIB_LIBS=-lz; export
NSPR_INCLUDE_DIR=/usr/local/include/nspr; make  
RUN cd /usr/local/src/nss-3.19.1/dist && install -v -m755 Linux*/lib/*.so
/usr/lib && install -v -m644 Linux*/lib/*.chk /usr/lib && install -v -m644
Linux*/lib/libcrmf.a /usr/lib && install -v -m755 -d /usr/include/nss && cp -v
-RL public/nss/* /usr/include/nss && cp -v -RL private/nss/* /usr/include/nss
&& chmod -v 644 /usr/include/nss/* && install -v -m755 Linux*/bin/certutil
/usr/bin && install -v -m755 Linux*/bin/nss-config /usr/bin && install -v
-m755 Linux*/bin/pk12util /usr/bin && install -v -m644
Linux*/lib/pkgconfig/nss.pc /usr/lib/pkgconfig  
RUN cd /usr/local/src ; rm -rf /usr/local/src/nss-3.19.1  
  
# GeoIP Support with updated databases  
RUN cd /usr/local/src/GeoIP-1.6.5 && ./configure ; make ; make install ;
ldconfig ; cd /usr/local/src/; rm -rf /usr/local/src/GeoIP-1.6.5  
RUN cd /usr/local/src/ && gunzip *dat.gz ; mkdir /usr/local/share/GeoIP ; mv
*.dat /usr/local/share/GeoIP  
  
# Complile Suricata  
RUN cd /usr/local/src/suricata-2.0.8 && ./configure --enable-luajit --enable-
geoip --enable-profiling --with-libnss-includes=/usr/include/nss/ -with-
libnss-libraries=/usr/lib/x86_64-linux-gnu --localstatedir=/var/ ; make ; make
install ; ldconfig ; cd /usr/local/src ; rm -rf /usr/local/src/suricata-2.0.8  
  
# make directories for logging  
RUN mkdir /var/log/suricata  
  
RUN /usr/local/bin/suricata --build-info  
  
# CLEAN UP - TODO  

