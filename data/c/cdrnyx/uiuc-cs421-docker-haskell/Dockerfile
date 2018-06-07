FROM haskell:7  
MAINTAINER Allyson Julian <allyson@allysonjulian.com>  
  
RUN cabal update && cabal install ghc-mod parsec quickcheck unordered-
containers  
  
ENV SRC_DIR /src/cs421  
  
RUN mkdir -p $SRC_DIR  
WORKDIR $SRC_DIR  
  
ADD . $SRC_DIR  
  
ENTRYPOINT ["ghci"]  

