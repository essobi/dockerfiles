# -*- coding: utf-8 -*-  
  
FROM teego/system:jessie  
  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
  
RUN echo "Development requirements" &&\  
( \  
apt-get install -qy --no-install-recommends \  
git \  
g++ \  
python3 \  
python3-dev \  
autotools-dev \  
libicu-dev \  
build-essential \  
libbz2-dev \  
libncurses5-dev \  
doxygen \  
libreadline-dev \  
dh-autoreconf \  
python2.7 \  
python2.7-dev \  
) && \  
apt-get clean -qy  
  
RUN ( \  
cd $BUILDROOT &&\  
wget http://www.cmake.org/files/v3.6/cmake-3.6.2.tar.gz &&\  
tar xf cmake-3.6.2.tar.gz &&\  
cd cmake-3.6.2 &&\  
./configure &&\  
make install \  
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
./config no-asm --openssldir="/usr" \  
) &&\  
make depend &&\  
make &&\  
make install \  
) \  
) \  
)  
  
ENV BOOST_VERSION 1.60.0  
  
RUN echo "Boost library" &&\  
mkdir -p /root/tmp && \  
( \  
cd /root/tmp; \  
wget -O boost_`echo $BOOST_VERSION | sed 's/\./_/g'`.tar.gz \  
http://sourceforge.net/projects/boost/files/boost/$BOOST_VERSION/boost_`echo
$BOOST_VERSION | sed 's/\./_/g'`.tar.gz/download &&\  
tar xfz boost_`echo $BOOST_VERSION | sed 's/\./_/g'`.tar.gz &&\  
( \  
cd boost_`echo $BOOST_VERSION | sed 's/\./_/g'`; \  
( \  
./bootstrap.sh --prefix=/usr &&\  
./b2 install \  
) \  
) \  
) && \  
( \  
cd /root/tmp; \  
rm -Rf boost_`echo $BOOST_VERSION | sed 's/\./_/g'` boost_`echo $BOOST_VERSION
| sed 's/\./_/g'`.tar.gz \  
)  
  
RUN figlet "Ready!"  

