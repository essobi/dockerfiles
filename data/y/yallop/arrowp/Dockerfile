FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
ghc \  
happy \  
cabal-install  
  
RUN cabal update  
  
RUN cabal install arrowp  
  
CMD ["/root/.cabal/bin/arrowp"]  

