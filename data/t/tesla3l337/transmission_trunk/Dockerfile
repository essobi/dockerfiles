# transmission light  
#  
# VERSION 0.0.2  
FROM alpine:edge  
MAINTAINER Tesla <tesla@v-ip.fr>  
COPY ./transmission.patch /  
RUN apk update  
RUN apk add \--update libevent ncurses-libs libintl libcurl && \  
apk add \--update \--virtual build-deps build-base make git glib-dev libevent-
dev curl-dev libressl-dev ncurses-dev automake autoconf intltool libtool && \  
git clone https://github.com/transmission/transmission.git && \  
mv /transmission.patch /transmission/ && cd /transmission && patch -p0 <
transmission.patch && \  
rm m4/glib-gettext.m4 && \  
sed -e 's/[Z|X]-\\]/0-]/g' -i configure.ac && \  
./autogen.sh && \  
./configure -prefix=/usr CFLAGS="-Os -s -fomit-frame-pointer -DNO_SYS_QUEUE_H"
LDFLAGS="-Wl,--as-needed" \--enable-daemon && make -j4 install-strip && \  
rm -r /transmission && \  
apk del build-deps && rm -rf /var/lib/apt/lists/*  
  

