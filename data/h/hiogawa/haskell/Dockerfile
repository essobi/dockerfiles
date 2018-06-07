FROM haskell:7.10  
RUN apt-get update && apt-get install -y git autoconf automake libtinfo-dev  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
  
RUN cabal update  
RUN git clone https://github.com/ghcjs/ghcjs.git  
RUN cabal install ./ghcjs  
RUN ghcjs-boot --dev  

