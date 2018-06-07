FROM debian:9.4-slim  
  
LABEL maintainer="https://github.com/e-goz"  
  
VOLUME /project  
  
RUN apt-get update && apt-get install -y git build-essential libssl1.0-dev
libdb++-dev libboost-all-dev libcrypto++-dev libqrencode-dev libminiupnpc-dev
libgmp-dev libgmp3-dev autoconf autogen automake libtool qt5-default qt5-qmake
qtbase5-dev-tools qttools5-dev-tools libboost-dev libboost-system-dev
libboost-filesystem-dev libboost-program-options-dev libboost-thread-dev
libdb++-dev zlib1g-dev  
  
COPY scripts.sh /project/scripts.sh  
  
WORKDIR /project  
  
CMD ./scripts.sh  

