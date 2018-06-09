# version 1.4-1  
FROM mazaclub/coind-base  
# IMAGE mazaclub/btc-therealbitcoin-base  
MAINTAINER guruvan "guruvan@maza.club"  
#XPOSE RPC P2P Testnet  
CMD ["/sbin/my_init"]  
VOLUME ["/home/coin"]  
EXPOSE 8639 8639  
ENV BUILDER DOCKERHUB  
ENV GIT_TAG $(git rev-parse --short HEAD)  
ENV WORKDIR $(pwd)  
ENV IMAGE mazaclub/btc-therealbitcoin-base  
ENV APP bitcoind  
ENV COIN bitcoin  
ENV COIN_SYM btc  
ENV STAGE DEV  
ENV BTC_VERSION thereealbitcoin  
RUN mkdir /patches \  
&& apt-get update \  
&& apt-get install -y libtool \  
wget bsdmainutils autoconf \  
apg libqrencode-dev libcurl4-openssl-dev \  
automake make ntp git build-essential \  
libssl-dev libboost-all-dev \  
libgmp-dev libmpfr-dev  
COPY patches/ /patches  
  
RUN echo "Building Daemon" \  
&& export COIN=bitcoin \  
&& export APP=bitcoind \  
&& wget http://thebitcoin.foundation/v0.5.3-0-gd05c03a.tar.gz \  
&& echo "aab1f8ea8c7f131ff69dfa3b9437ba35531018be760132dd6373f41a591f6382
v0.5.3-0-gd05c03a.tar.gz" > v0.5.3-0-gd05c03a.tar.gz.sha256 \  
&& sha256sum -c v0.5.3-0-gd05c03a.tar.gz.sha256 \  
&& tar -xpzvf v0.5.3-0-gd05c03a.tar.gz \  
&& cd bitcoin-bitcoin-a8def6b/src \  
&& cp /patches//bdb_maxintlocks_corrected.patch . \  
&& patch < bdb_maxintlocks_corrected.patch \  
&& export BDB_INCLUDE_PATH="${BDB_PREFIX}/include" \  
&& export BDB_LIB_PATH="/db-4.8.30.NC/build_unix" \  
&& sed -i 's/USE_UPNP\:\=0/USE_UPNP\:\=\\-/g' makefile.unix \  
&& if [ "${BUILDER}" = "LOCAL" ] ; then export MAKEJOBS="-j3" ; else export
MAKEJOBS="" ; fi \  
&& make ${MAKEJOBS} -f makefile.unix \  
&& mv ${APP} /usr/local/bin/ \  
&& cd / \  
&& rm -rf /src  
  
COPY . /  
RUN chmod 700 /etc/service/bitcoind/run \  
&& groupadd --gid 2211 coin \  
&& adduser --disabled-password --gecos "bitcoin" \--uid 2211 --gid 2211 coin \  
&& chown -R coin.coin /home/coin \  
&& chmod 600 /home/coin/.bitcoin/bitcoin.conf  

