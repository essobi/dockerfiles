FROM haskell:8.0.2  
WORKDIR /opt/server  
  
RUN apt-get update  
RUN apt-get -y install autoconf libtool python libbsd-dev make  
RUN cabal update  
  
# Add just the .cabal file to capture dependencies  
RUN git clone https://bitbucket.org/owenarden/flame.git  
WORKDIR /opt/server/flame  
RUN git checkout refactor  
RUN cabal install -j4  
  
WORKDIR /opt/server  
RUN git clone https://github.com/rescrv/libmacaroons  
WORKDIR /opt/server/libmacaroons  
RUN autoreconf -i  
RUN ./configure  
RUN make  
RUN make install  
  
ENV LD_LIBRARY_PATH /usr/local/lib:${LD_LIBRARY_PATH}  
  
WORKDIR /opt/server  
RUN git clone https://bitbucket.org/owenarden/macaroons-haskell.git  
WORKDIR /opt/server/macaroons-haskell  
RUN cabal install c2hs  
RUN cabal install -j4  
  
WORKDIR /opt/server  
RUN git clone https://bitbucket.org/owenarden/flame-macaroons.git  
WORKDIR /opt/server/flame-macaroons  
RUN cabal install -j4  
  
WORKDIR /opt/server  
WORKDIR /opt/server  
RUN git clone https://bitbucket.org/owenarden/flame-servant.git  
WORKDIR /opt/server/flame-servant  
RUN cabal install --only-dependencies -j4  
RUN cabal install  
  
WORKDIR /opt/server/flame-servant/examples  
CMD ["ghc", "-e", "NMMemoDBServer.main", "NMMemoDBServer.hs"]  

