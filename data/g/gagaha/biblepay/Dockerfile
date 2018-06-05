FROM ubuntu:16.04  
LABEL maintainer="gagaha@gmx.net"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:bitcoin/bitcoin && add-apt-repository ppa:ubuntu-
toolchain-r/test && \  
apt-get update && apt-get install -y --no-install-recommends libdb4.8-dev
libdb4.8++-dev \  
automake bsdmainutils wget gcc-6 g++-6 git make build-essential libzmq3-dev
autoconf libtool \  
libqt4-dev libminiupnpc-dev pkg-config libboost-all-dev libssl-dev libevent-
dev libprotobuf-dev protobuf-compiler htop && \  
BP_ROOT=/root && BDB_PREFIX="${BP_ROOT}/db4" && mkdir -p $BDB_PREFIX && \  
wget 'http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz' && \  
echo '12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef
db-4.8.30.NC.tar.gz' | sha256sum -c && \  
tar -xzvf db-4.8.30.NC.tar.gz && rm db-4.8.30.NC.tar.gz && cd
db-4.8.30.NC/build_unix && \  
../dist/configure --enable-cxx --disable-shared --with-pic
--prefix=$BDB_PREFIX && \  
make install  
  
LABEL version=1.1.2.4b  
  
RUN BP_ROOT=/root && BDB_PREFIX="${BP_ROOT}/db4" && cd /root && git clone
https://github.com/biblepay/biblepay && \  
chmod 777 $BP_ROOT/biblepay/share/genbuild.sh $BP_ROOT/biblepay/autogen.sh &&
\  
$BP_ROOT/biblepay/autogen.sh && \  
$BP_ROOT/biblepay/configure --without-gui --disable-bench --disable-tests
--with-miniupnpc LDFLAGS="-L${BDB_PREFIX}/lib/"
CPPFLAGS="-I${BDB_PREFIX}/include/" && \  
make && \  
mv ${BP_ROOT}/src/biblepayd ${BP_ROOT}/src/biblepay-cli
${BP_ROOT}/src/biblepay-tx /usr/sbin && \  
rm -rf $BP_ROOT/src $BP_ROOT/biblepay/ $BP_ROOT/db4/ ${BP_ROOT}/db-4.8.30.NC
&& \  
apt-get autoremove -y && apt-get remove --purge -y gcc-6 g++-6 git make build-
essential autoconf libzmq3-dev libtool libdb4.8-dev libdb4.8++-dev libqt4-dev
\  
libssl-dev libevent-dev libprotobuf-dev protobuf-compiler automake
bsdmainutils libboost-all-dev libssl-dev libminiupnpc-dev pkg-config && \  
apt-get clean && rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
VOLUME /root/.biblepaycore  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["biblepayd", "-printtoconsole"]  

