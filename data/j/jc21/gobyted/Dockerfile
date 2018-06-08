FROM ubuntu:16.04  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
ENV S6_FIX_ATTRS_HIDDEN=1  
ENV SRC_DIR /usr/local/src/gobyte  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
RUN set -x \  
&& buildDeps=' \  
build-essential \  
libtool \  
autotools-dev \  
automake \  
pkg-config \  
bsdmainutils \  
make \  
cmake \  
g++ \  
git \  
' \  
&& apt-get -y update \  
&& apt-get -y --no-install-recommends install software-properties-common \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get -y update \  
&& apt-get -y --no-install-recommends install $buildDeps libboost1.58-all-dev
libdb4.8-dev libdb4.8++-dev libevent-dev libssl-dev ca-certificates \  
&& git clone https://github.com/gobytecoin/gobyte.git $SRC_DIR \  
&& cd $SRC_DIR \  
&& ./autogen.sh \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
&& rm -rf $SRC_DIR \  
&& apt-get -y --auto-remove purge $buildDeps \  
&& apt-get autoremove --purge \  
&& apt-get clean  
  
# Contains the blockchain  
VOLUME /root/.gobytecore  
  
# Port  
EXPOSE 12455  
# RPC Port  
EXPOSE 12454  
WORKDIR /root  
  
# S6 Overlay  
COPY rootfs /  
ADD env/.bashrc /root/  
RUN apt-get -y install curl && curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C /  
  
ENTRYPOINT [ "/init" ]  

