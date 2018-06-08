from mitchty/alpine-ghc  
  
run apk update && \  
apk add wget gzip && \  
cabal update && \  
cabal install alex happy && \  
cabal install c2hs && \  
cabal install hoogle && \  
hoogle data  
  
workdir /tmp  
cmd ["bash"]  

