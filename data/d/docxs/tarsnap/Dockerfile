########################################################################  
# Dockerfile for Tarsnap  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: Tarsnap  
# Author: pjan vandaele <pjan@pjan.io>  
# Scm url: https://github.com/docxs/tarsnap  
# License: MIT  
########################################################################  
  
# pull base image  
FROM docxs/base:latest  
  
# maintainer details  
MAINTAINER pjan vandaele "pjan@pjan.io"  
  
# Set the environment variables  
ENV TARSNAP_VERSION 1.0.35  
ENV TARSNAP_SHA256
6c9f6756bc43bc225b842f7e3a0ec7204e0cf606e10559d27704e1cc33098c9a  
  
# Install tarsnap  
RUN \  
apt-prepare && \  
apt-get install -q -y \  
wget \  
ca-certificates \  
make \  
libssl-dev \  
zlib1g-dev \  
e2fslibs-dev \  
openssl \  
build-essential && \  
wget https://www.tarsnap.com/download/tarsnap-autoconf-$TARSNAP_VERSION.tgz &&
\  
hash="$(sha256sum tarsnap-autoconf-$TARSNAP_VERSION.tgz | cut -d " " -f1)" &&
\  
( [ "$hash" = "$TARSNAP_SHA256" ] || (echo "hash check failed" && exit 1) ) &&
\  
tar zxf tarsnap-autoconf-$TARSNAP_VERSION.tgz && \  
cd tarsnap-autoconf-$TARSNAP_VERSION && \  
./configure && \  
make all install clean && \  
cd .. && \  
rm -f tarsnap-autoconf-$TARSNAP_VERSION.tgz && \  
rm -rf tarsnap-autoconf-$TARSNAP_VERSION && \  
apt-get -y remove --purge \  
wget \  
ca-certificates \  
make \  
libssl-dev \  
zlib1g-dev \  
e2fslibs-dev \  
build-essential && \  
apt-cleanup  
  
# default command  
CMD \  
["/bin/bash", "-c", "echo 'Available commands: ' && compgen -ca | grep tarsnap
| sort"]  

