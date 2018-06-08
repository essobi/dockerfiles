FROM alpine:latest  
LABEL maintainer="hackaday <hackaday@coz.moe>"  
  
ENV LANG C.UTF-8  
# build and install  
RUN set -ex \  
&& apk add --update --no-cache --virtual .build-deps \  
automake \  
autoconf \  
openssl-dev \  
curl-dev \  
git \  
build-base \  
&& mkdir /opt \  
&& cd /opt \  
&& git clone https://github.com/OhGodAPet/cpuminer-multi \  
&& cd cpuminer-multi \  
&& ./autogen.sh \  
&& CFLAGS="-O3" ./configure --disable-aes-ni \  
&& make \  
&& apk del .build-deps  
  
# run dep  
RUN apk add --update --no-cache openssl libcurl  
  
ENV USERNAME massimo.farinelli.roma@gmail.com  
# ENV PASSWORD password  
ENV POOL xmr.pool.minergate.com:45560  
# ENV THREAD_NUM 8  
USER nobody  
  
WORKDIR /  
  
# ENTRYPOINT ["sh", "-c", "/opt/cpuminer-multi/minerd -a cryptonight -o
stratum+tcp://${POOL} -u ${USERNAME} -p ${PASSWORD} -t ${THREAD_NUM:-8}"]  
ENTRYPOINT ["sh", "-c", "/opt/cpuminer-multi/minerd -a cryptonight -o
stratum+tcp://${POOL} -u ${USERNAME}"]  

