FROM haskell:7.10  
MAINTAINER Jonathan Bunde-Pedersen <jonathan@purebadger.com>  
  
ENV ELM_VER=0.18  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
libtinfo-dev \  
nodejs  
  
ENV PATH /opt/Elm-Platform/$ELM_VER/.cabal-sandbox/bin:$PATH  
WORKDIR /opt  
RUN curl https://raw.githubusercontent.com/elm-lang/elm-
platform/master/installers/BuildFromSource.hs > BuildFromSource.hs  
RUN runhaskell BuildFromSource.hs $ELM_VER  
  
CMD ["elm"]  
  

