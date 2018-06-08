FROM alpine:3.5  
LABEL MAINTAINER J. Koppe <post@jankoppe.de>  
RUN apk add --no-cache --virtual .build-deps\  
automake \  
autoconf \  
bison \  
ccache \  
cppunit \  
cppunit-dev \  
g++ \  
git \  
libtool \  
libmicrohttpd-dev \  
libusb-compat-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl \  
protobuf-dev \  
py-pip \  
util-linux-dev \  
&& apk add --no-cache --virtual .runtime-deps \  
flex \  
libmicrohttpd \  
libusb-compat \  
ncurses \  
protobuf \  
util-linux \  
&& pip install --no-cache-dir protobuf==3.1.0 \  
&& git clone https://git.code.sf.net/p/liblo/git --depth 1 -b 0.28 liblo \  
&& cd liblo \  
&& sed -i 's/-Werror/-Wno-error/' configure.ac \  
&& ./autogen.sh --enable-ipv6 \  
&& make && make install \  
&& cd / \  
&& wget
https://www.intra2net.com/en/developer/libftdi/download/libftdi-0.20.tar.gz \  
&& tar xfz libftdi-0.20.tar.gz \  
&& cd libftdi-0.20 \  
&& ./configure --without-examples \  
&& make && make install \  
&& cd / \  
&& git clone https://github.com/OpenLightingProject/ola.git --depth 1 -b
0.10.4 ola \  
&& cd ola \  
&& autoreconf -i \  
&& ./configure \  
&& make && make install \  
&& cd / \  
&& rm -rf /ola /liblo libftdi-0.20 \  
&& apk del .build-deps  
  
EXPOSE 9090  
EXPOSE 9010  
RUN adduser -S olad  
USER olad  
CMD ["olad"]  

