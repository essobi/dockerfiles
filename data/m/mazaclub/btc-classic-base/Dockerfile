# version 1.4-1  
FROM mazaclub/coind-base  
# IMAGE mazaclub/btc-classic-base  
MAINTAINER guruvan "guruvan@maza.club"  
#XPOSE RPC P2P Testnet  
CMD ["/sbin/my_init"]  
VOLUME ["/home/coin"]  
EXPOSE 8332 8333  
ENV BUILDER DOCKERHUB  
ENV WORKDIR $(pwd)  
ENV IMAGE mazalub/btc-classic-base  
ENV APP bitcoind  
ENV COIN bitcoin  
ENV COIN_SYM btc  
ENV STAGE DEV  
ENV BTC_VERSION classic  
RUN set -x && apt-get update \  
&& apt-get install -y libtool \  
wget bsdmainutils autoconf \  
apg libqrencode-dev libcurl4-openssl-dev \  
automake make ntp git build-essential \  
libssl-dev libevent-dev libboost-all-dev  
RUN echo "Building daemon" \  
&& export COIN=bitcoin \  
&& export APP=bitcoind \  
&& if [ "${BUILDER}" = "LOCAL" ] ; then export MAKEJOBS="-j3" ; else export
MAKEJOBS=""; fi \  
&& git clone https://github.com/bitcoinclassic/bitcoinclassic ${COIN} \  
&& cd ${COIN} \  
&& export BDB_INCLUDE_PATH="${BDB_PREFIX}/include" \  
&& export BDB_LIB_PATH="/db-4.8.30.NC/build_unix" \  
&& ./autogen.sh \  
&& LDFLAGS="-L${BDB_PREFIX}/lib" CPPFLAGS="-I${BDB_PREFIX}/include/
${CPPFLAGS}" ./configure --enable-cxx --disable-shared --with-pic \  
&& cd src \  
&& sed -i 's/USE_UPNP\:\=0/USE_UPNP\:\=\\-/g' Makefile \  
&& make \  
&& make install \  
&& mv ${APP} /usr/local/bin/ \  
&& cd /  
  
COPY . /  
RUN chmod 700 /etc/service/bitcoind/run \  
&& groupadd --gid 2211 coin \  
&& adduser --disabled-password --gecos "bitcoin" \--uid 2211 --gid 2211 coin \  
&& chown -R coin.coin /home/coin \  
&& chmod 600 /home/coin/.bitcoin/bitcoin.conf  

