FROM debian:jessie  
  
ENV BDB_VERSION="db-5.3.28.NC" \  
BDB_HASH="76a25560d9e52a198d37a31440fd07632b5f1f8f9f2b6d5438f4bc3e7c9013ef" \  
BDB_DIR="/usr/local/db5"  
  
RUN BDB_FILE=$BDB_VERSION".tar.gz" \  
BDB_URL="http://download.oracle.com/berkeley-db/"$BDB_FILE \  
&& set -xe \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
g++ \  
make \  
libdb++-dev \  
autoconf \  
libtool \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget $BDB_URL \  
&& echo "$BDB_HASH $BDB_FILE" | sha256sum -c - \  
&& tar -xzvf $BDB_FILE \  
&& cd $BDB_VERSION"/build_unix/" \  
&& ../dist/configure --enable-cxx --disable-shared --with-pic
--prefix=$BDB_DIR \  
&& mkdir -p $BDB_DIR \  
&& make install \  
&& cd ../../ \  
&& rm $BDB_FILE \  
&& rm -rf $BDB_VERSION \  
&& export BDB_INCLUDE_PATH="$BDB_DIR/include" \  
&& export BDB_LIB_PATH="$BDB_DIR/lib" \  
&& ln -s $BDB_DIR/libdb-5.3.so /usr/lib/libdb-5.3.so  

