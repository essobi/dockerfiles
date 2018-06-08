FROM ubuntu:16.04  
MAINTAINER Ashish Srivastava <me@ashishsrivastav.com>  
  
ENV SRC_DIR /usr/local/Rupee-Core/  
ENV CONF_DIR /root/.RupeeCore/  
  
ADD Rupee.conf $CONF_DIR  
  
RUN set -x \  
&& buildDeps=' \  
ca-certificates \  
cmake \  
g++ \  
git \  
libboost1.58-all-dev \  
libssl-dev \  
make \  
pkg-config \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps  
  
RUN apt-get install qt4-qmake libqt4-dev build-essential libboost-dev
libboost-system-dev \  
libboost-filesystem-dev libboost-program-options-dev libboost-thread-dev \  
libssl-dev libdb++-dev libminiupnpc-dev -y  
  
RUN git clone https://github.com/rupeedigitalassets/RUPEE-Core.git $SRC_DIR  
  
WORKDIR $SRC_DIR/src  
  
RUN make -f makefile.unix  
  
EXPOSE 8518  
EXPOSE 8517  
CMD Rupeed  

