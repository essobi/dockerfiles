FROM alpine:3.5  
  
RUN set -x \  
&& apk update \  
&& apk \--no-cache add \  
libstdc++ \  
protobuf \  
&& apk \--no-cache add --virtual .builddeps \  
autoconf \  
automake \  
build-base \  
git \  
libtool \  
protobuf-dev \  
&& git clone https://github.com/google/sentencepiece \  
&& cd sentencepiece \  
&& ./autogen.sh \  
&& ./configure \  
&& CPUCOUNT=$(cat /proc/cpuinfo | grep '^processor.*:' | wc -l) \  
&& make -j ${CPUCOUNT} \  
&& make check \  
# && ldconfig -v \  
&& make install \  
## cleanup  
&& make clean \  
&& apk del .builddeps  
  
WORKDIR /sentencepiece

