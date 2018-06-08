  
FROM teego/steem-base:0.3-Ubuntu-xenial  
  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN figlet "MinGW" &&\  
( \  
apt-get install -qy --no-install-recommends \  
build-essential \  
mingw-w64 \  
g++-mingw-w64 \  
git \  
psmisc \  
make \  
nsis \  
autoconf \  
libtool \  
automake \  
pkg-config \  
bsdmainutils \  
python-dev \  
faketime \  
) &&\  
apt-get clean -qy  
  
RUN x86_64-w64-mingw32-g++ --version  
  
ENV BUILDBASE /r  
  
ENV BUILDROOT $BUILDBASE/build  
ENV MINGWROOT $BUILDBASE/mingw  
  
RUN mkdir -p $BUILDROOT $MINGWROOT/lib  
  
RUN figlet "JWasm" &&\  
( \  
cd $BUILDROOT; \  
( \  
git clone https://github.com/JWasm/JWasm.git jwasm &&\  
( \  
cd jwasm; \  
( \  
make -f GccUnix.mak &&\  
cp GccUnixR/jwasm /usr/bin/ \  
) \  
) \  
) \  
)  
  
ENV OPENSSL_VERSION 1.0.2h  
  
RUN figlet "OpenSSL" &&\  
( \  
cd $BUILDROOT; \  
wget -O openssl-$OPENSSL_VERSION.tar.gz \  
https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz &&\  
tar xfz openssl-$OPENSSL_VERSION.tar.gz &&\  
( \  
cd openssl-$OPENSSL_VERSION; \  
( \  
( \  
env CROSS_COMPILE="x86_64-w64-mingw32-" ./Configure mingw64 no-asm
--openssldir="$MINGWROOT" \  
) &&\  
make depend &&\  
make &&\  
make install \  
) \  
) \  
)  
  
RUN figlet "Ready!"  

