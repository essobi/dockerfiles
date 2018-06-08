FROM ubuntu:16.04  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
ENV S6_FIX_ATTRS_HIDDEN=1  
ENV SRC_DIR /usr/local/src/lindacoin  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
ADD env/.bashrc /root/  
  
RUN set -x \  
&& buildDeps=' \  
build-essential \  
libtool \  
ca-certificates \  
automake \  
autoconf \  
cmake \  
g++ \  
git \  
autotools-dev \  
libboost1.58-all-dev \  
libssl-dev \  
libgmp3-dev \  
libevent-dev \  
make \  
pkg-config \  
bsdmainutils \  
libdb4.8-dev \  
libdb4.8++-dev \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install software-properties-common \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps  
  
RUN git clone https://github.com/Lindacoin/Linda.git $SRC_DIR  
WORKDIR $SRC_DIR/src  
RUN mv makefile.unix makefile && make -j$(nproc)  
  
RUN cp Lindad /usr/local/bin/ \  
&& rm -r $SRC_DIR \  
&& apt-get -qq --auto-remove purge $buildDeps  
  
# Contains the blockchain and wallet files  
VOLUME /root/.Linda  
  
EXPOSE 15714  
EXPOSE 15715  
WORKDIR /root  
  
# S6 Overlay  
COPY rootfs /  
RUN apt-get -y install curl && curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C /  
  
CMD [ "/init" ]  

