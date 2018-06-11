FROM alpine:3.3  
MAINTAINER Pedro Branco <branco@uphold.com> (@pedrobranco)  
  
RUN apk add --no-cache su-exec  
  
ENV GETH_DATA=/home/ethereum/.geth \  
GETH_VERSION=1.4.10 \  
GETH_SHASUM="971f487f4a432cb9d95618cf87bb2d00a9acc3d9c11d152ea3110e7ab2253d87
v1.4.10.tar.gz"  
RUN apk add --no-cache --virtual build-dependencies \  
gcc \  
go \  
make \  
musl-dev \  
openssl \  
&& wget "https://github.com/ethereum/go-
ethereum/archive/v$GETH_VERSION.tar.gz" \  
&& echo "${GETH_SHASUM}" | sha256sum -c && tar -zxf v$GETH_VERSION.tar.gz \  
&& (cd go-ethereum-$GETH_VERSION && make && cp build/bin/geth
/usr/local/bin/geth) \  
&& rm -rf v$GETH_VERSION.tar.gz go-ethereum-$GETH_VERSION/ \  
&& apk del --no-cache build-dependencies  
  
EXPOSE 8545 8546 6060 30301/udp 30303  
RUN adduser -S ethereum  
  
VOLUME ["/home/ethereum/.geth"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["geth"]  

