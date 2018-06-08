FROM ubuntu:16.04  
ENV S6_FIX_ATTRS_HIDDEN=1  
ENV SRC_DIR /usr/local/src/lux  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
RUN set -x \  
&& buildDeps=' \  
build-essential \  
libtool \  
autotools-dev \  
automake \  
bsdmainutils \  
cmake \  
g++ \  
git \  
make \  
pkg-config \  
' \  
&& apt-get -y update \  
&& apt-get -y --no-install-recommends install software-properties-common \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get -y update \  
&& apt-get -y --no-install-recommends install $buildDeps libboost1.58-all-dev
libdb4.8-dev libdb4.8++-dev libssl-dev libevent-dev ca-certificates \  
&& git clone https://github.com/216k155/lux.git $SRC_DIR \  
&& cd $SRC_DIR \  
&& ./autogen.sh \  
&& ./configure \  
&& make -j$(nproc) \  
&& cp src/lux-cli src/lux-tx src/luxd /usr/local/bin/ \  
&& rm -r $SRC_DIR \  
&& apt-get -y --auto-remove purge $buildDeps \  
&& apt-get autoremove --purge \  
&& apt-get clean  
  
# Contains the blockchain  
VOLUME /root/.lux  
  
# Port  
EXPOSE 28666  
# RPC Port  
EXPOSE 9888  
# Masternode Port  
EXPOSE 28666  
WORKDIR /root  
  
# S6 Overlay  
COPY rootfs /  
ADD env/.bashrc /root/  
RUN apt-get -y install curl && curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C /  
  
ENTRYPOINT [ "/init" ]  

