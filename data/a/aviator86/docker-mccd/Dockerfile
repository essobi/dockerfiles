FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get --no-install-recommends --yes install \  
git \  
automake \  
build-essential \  
libtool \  
autotools-dev \  
autoconf \  
pkg-config \  
libssl-dev \  
libboost-all-dev \  
libevent-dev \  
bsdmainutils \  
vim \  
libgmp3-dev \  
unzip \  
wget \  
libzmq5 \  
software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
  
RUN add-apt-repository ppa:bitcoin/bitcoin && \  
apt-get update && \  
apt-get --no-install-recommends --yes install \  
libdb4.8-dev \  
libdb4.8++-dev \  
libminiupnpc-dev && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /mccproject  
  
ENV MMC_VERSION v1.1  
  
RUN wget https://github.com/mcc-
project/mccproject/releases/download/$MMC_VERSION/linux-$MMC_VERSION.zip && \  
unzip linux-$MMC_VERSION.zip && \  
strip /mccproject/mccd /mccproject/mcc-cli && \  
mv /mccproject/mccd /usr/local/bin/ && \  
mv /mccproject/mcc-cli /usr/local/bin/ && \  
chmod +x /usr/local/bin/mccd && chmod +x /usr/local/bin/mcc-cli && \  
rm -rf /mccproject  
  
VOLUME ["/root/.mcc"]  
  
EXPOSE 29868 29869  
  
CMD /usr/local/bin/mccd && tail -f /root/.mcc/debug.log

