FROM ubuntu  
  
ENV HOME /root  
  
RUN apt-get update && apt-get -y install haskell-platform ssl-cert ca-
certificates  
RUN cabal update && cabal install cabal-install && cabal install yesod-
platform yesod-bin \--max-backjumps=-1 --reorder-goals  

