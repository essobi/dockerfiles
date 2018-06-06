FROM ubuntu:16.04 as compile  
LABEL maintainer "Corey Ryan Hanson"  
  
#Installs git and downloads from repository.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
--no-install-recommends -y \  
git \  
ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/EverGreenCoinDev/EverGreenCoin.git && \  
cd EverGreenCoin && \  
git checkout 569e4436c0ecdc912ee6900cc3a2d823dc1d8748  
  
#Installs dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
sudo \  
qt5-default \  
qt5-qmake \  
qtbase5-dev-tools \  
qttools5-dev-tools \  
build-essential \  
libboost-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-thread-dev \  
libssl-dev \  
libdb++-dev \  
libminiupnpc-dev \  
libqrencode-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#Builds EverGreenCoin wallet.  
RUN cd /EverGreenCoin && \  
qmake && \  
make  
  
#Begins stage 2 of image.  
FROM ubuntu:16.04  
#Copies and makes scripts executable.  
COPY create-user.sh /  
RUN chmod +x create-user.sh  
  
#Downloads dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
sudo \  
ca-certificates \  
libminiupnpc10 \  
libssl1.0.0 \  
libdb5.3++ \  
libboost-system1.58.0 \  
libboost-filesystem1.58.0 \  
libboost-program-options1.58.0 \  
libboost-thread1.58.0 \  
libqt5widgets5 \  
libqt5gui5 \  
libqt5network5 \  
libqt5core5a \  
libqrencode3 && \  
rm -rf /var/lib/apt/lists/*  
  
#Imports EverGreenCoin executable from stage 1.  
COPY \--from=compile /EverGreenCoin/EverGreenCoin-Qt /usr/local/bin/  
  
#Creates unprivileged user.  
ARG docker_root_pass=starcatfish  
ARG docker_unprivileged_user=evergreen  
ARG docker_unprivileged_pass=walrus  
RUN /create-user.sh && \  
rm /create-user.sh  
  
USER $docker_unprivileged_user  
WORKDIR /home/evergreen  
  
CMD /usr/local/bin/EverGreenCoin-Qt  

