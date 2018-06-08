FROM haskell:7.8  
RUN cabal update  
  
ADD http://www.stackage.org/lts/1/cabal.config?global=true /root/.cabal/lts-
constraints  
RUN cd /root/.cabal/ && cat lts-constraints >> config  
  
RUN cabal update  
RUN cabal install base-prelude basic-prelude  

