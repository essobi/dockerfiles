FROM alpine:latest as bitcoind  
LABEL maintainer="Sergey Nebolsin <sergey@nebols.in>"  
  
ENV BITCOIN_VERSION=0.15.0.1  
ENV BITCOIN_FOLDER_VERSION=0.15.0  
ENV BITCOIN_PREFIX=/opt/bitcoin  
ENV PATH=${BITCOIN_PREFIX}/bin:$PATH  
  
WORKDIR /app  
  
RUN apk add --no-cache \  
autoconf \  
automake \  
boost-dev \  
build-base \  
chrpath \  
file \  
gnupg \  
libevent-dev \  
libressl \  
libressl-dev \  
libtool \  
linux-headers \  
protobuf-dev \  
zeromq-dev  
  
RUN wget -O- https://bitcoin.org/laanwj-releases.asc | gpg --import \  
&& wget https://bitcoin.org/bin/bitcoin-core-${BITCOIN_VERSION}/SHA256SUMS.asc
\  
&& wget https://bitcoin.org/bin/bitcoin-
core-${BITCOIN_VERSION}/bitcoin-${BITCOIN_VERSION}.tar.gz \  
&& gpg --verify SHA256SUMS.asc \  
&& grep " bitcoin-${BITCOIN_VERSION}.tar.gz\$" SHA256SUMS.asc | sha256sum -c -
\  
&& tar -xzf bitcoin-${BITCOIN_VERSION}.tar.gz  
  
WORKDIR /app/bitcoin-${BITCOIN_FOLDER_VERSION}  
RUN sed -i 's|sys/fcntl.h|fcntl.h|g' src/compat.h  
RUN ./autogen.sh  
RUN ./configure \  
\--prefix=${BITCOIN_PREFIX} \  
\--mandir=/usr/share/man \  
\--disable-tests \  
\--disable-bench \  
\--disable-ccache \  
\--disable-wallet \  
\--with-gui=no \  
\--with-utils \  
\--with-libs \  
\--with-daemon  
RUN make install -j 4  
  
WORKDIR "${BITCOIN_PREFIX}"  
RUN strip bin/bitcoin-cli bin/bitcoind bin/bitcoin-tx
lib/libbitcoinconsensus.a lib/libbitcoinconsensus.so.0.0.0  
  
# ===============================================================  
FROM nebolsin/confd as confd  
  
# ===============================================================  
FROM alpine:latest  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer="Sergey Nebolsin <sergey@nebols.in>" \  
org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.vcs-url="https://github.com/nebolsin/docker-bitcoin-rpc"  
  
RUN apk add --no-cache \  
bash \  
boost \  
boost-program_options \  
libevent \  
libressl \  
libzmq \  
su-exec \  
&& adduser -S bitcoin  
  
ENV PATH=/opt/bitcoin/bin:$PATH  
ENV BITCOIND_DATADIR=/home/bitcoin/.bitcoin  
ENV BITCOIND_PORT=8333  
ENV BITCOIND_RPCPORT=8332  
COPY \--from=confd /app/bin/confd /usr/local/bin/confd  
COPY \--from=bitcoind /opt/bitcoin /opt/bitcoin  
  
COPY templates /etc/confd/templates/  
COPY conf.d /etc/confd/conf.d/  
COPY docker-entrypoint.sh /entrypoint.sh  
  
WORKDIR "${BITCOIND_DATADIR}"  
  
VOLUME ["${BITCOIND_DATADIR}"]  
EXPOSE ${BITCOIND_PORT} ${BITCOIND_RPC_PORT}  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bitcoind"]  
  
HEALTHCHECK CMD ["/entrypoint.sh", "bitcoin-cli", "getinfo"]  

