FROM ubuntu:14.04  
  
MAINTAINER Valeriy Solovyov <weldpua2008@gmail.com>  
  
RUN set -x && \  
export SAMPLICATOR_VERSION=master && \  
export SAMPLICATOR_BUIL_ROOT=/tmp/samplicator/git && \  
export SAMPLICATOR_FILE=samplicator-$SAMPLICATOR_VERSION.tar.gz &&\  
export SAMPLICATOR_GIT_REPO=https://github.com/sleinen/samplicator.git && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get -y install build-essential libtool && \  
apt-get install automake libtool autogen git autoconf -y && \  
mkdir -p $SAMPLICATOR_BUIL_ROOT && \  
rm -rf $SAMPLICATOR_BUIL_ROOT && \  
git config \--global http.sslVerify false && \  
git clone $SAMPLICATOR_GIT_REPO $SAMPLICATOR_BUIL_ROOT && \  
cd $SAMPLICATOR_BUIL_ROOT && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  
  
#ln -s /$SAMPLICATOR_BUIL_ROOT/samplicate /usr/bin/samplicate  
  
ENTRYPOINT ["samplicate"]  

