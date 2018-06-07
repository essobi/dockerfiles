FROM alpine:3.7  
  
LABEL maintainer="parsemaker <cobays@gmail.com>"  
  
RUN set -xe \  
&& apk add --update --no-cache \  
python \  
man \  
build-base \  
cmake \  
boost \  
gmp \  
gettext \  
boost-dev \  
boost-date_time \  
boost-iostreams \  
gmp-dev \  
mpfr3 \  
mpfr-dev \  
git \  
&& git clone -b next git://github.com/ledger/ledger.git \  
&& cd ledger \  
&& ./acprep dependencies \  
&& ./acprep opt configure \  
&& ./acprep opt update \  
&& make install \  
&& cd .. \  
&& rm -rf ledger \  
&& apk del build-base boost-dev gmp-dev mpfr-dev cmake git  
  
COPY data /data  
  
VOLUME /data  

