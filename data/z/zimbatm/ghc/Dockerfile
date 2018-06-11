FROM ubuntu:12.04  
  
ENV LANG C.UTF-8  
  
RUN apt-get update -qq && apt-get install python-software-properties -qy &&
apt-get clean  
RUN add-apt-repository -y ppa:hvr/ghc  
RUN apt-get update -qq && apt-get install -qy ghc-7.8.4 ghc-7.8.4-prof cabal-
install-1.22 && apt-get clean  
  
ENV PATH /opt/ghc/7.8.4/bin:/opt/cabal/1.22/bin:$PATH  

