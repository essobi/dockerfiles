FROM insecurity/debian-32bit:latest  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set variables  
ENV NODE_VERSION 6.3.1  
ENV NODE_INSTALL_DIR /root/node  
ENV APP_DIR /srv/app  
  
# Patch installation for i386/x87 compatibility  
# (see https://bitbucket.org/jtof_fap/node-32bit-x87 for details)  
# Onelayer optimization: CP in /tmp before RUN  
COPY x87/common.gypi /tmp/common.gypi  
  
# From official image : gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
  
# Install build dependencies \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get
install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
gcc \  
g++ \  
make \  
git \  
python \  
clang-3.5 \  
libclang-3.5-dev \  
  
# Get Node from sources \  
&& git clone https://github.com/nodejs/node.git $NODE_INSTALL_DIR \  
&& cd $NODE_INSTALL_DIR \  
&& git checkout v6.3.1 \  
  
# Patch installation for i386/x87 compatibility \  
# COPY x87/common.gypi $NODE_INSTALL_DIR/common.gypi \  
&& mv -f /tmp/common.gypi $NODE_INSTALL_DIR/common.gypi \  
  
# Compile, install Node and clean install directory \  
&& cd $NODE_INSTALL_DIR \  
&& ./configure --without-snapshot --dest-cpu=ia32 --dest-os=linux \  
&& make \  
&& make install \  
&& mkdir -p $APP_DIR \  
&& cd $APP_DIR \  
&& rm -Rf $NODE_INSTALL_DIR \  
  
# Clean apt \  
&& apt-get autoclean \  
&& apt-get clean \  
&& apt-get remove --purge -y $(apt-mark showauto) \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
# Let's go  
WORKDIR $APP_DIR  
CMD [ "node" ]  

