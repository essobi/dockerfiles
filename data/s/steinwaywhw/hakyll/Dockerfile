FROM steinwaywhw/pandoc  
  
RUN apt-get install -y ghc cabal-install zlib1g-dev  
RUN cabal update  
RUN cabal install hakyll  
  
WORKDIR /tmp  

