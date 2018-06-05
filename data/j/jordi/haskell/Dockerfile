FROM ubuntu:15.04  
  
ENV TERM linux  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:hvr/ghc  
RUN apt-get -y update  
ENV CABAL_VERSION 1.22  
ENV GHC_VERSION 7.8.4  
RUN apt-get -y install cabal-install-$CABAL_VERSION ghc-$GHC_VERSION  
ENV PATH
/root/.cabal/bin:/opt/cabal/$CABAL_VERSION/bin:/opt/ghc/$GHC_VERSION/bin:$PATH  
RUN cabal update  
RUN cabal install alex happy  
RUN apt-get -y install build-essential zlib1g-dev libmysqlclient-dev libpq-dev  
  
# Install yesod  
RUN cabal update && cabal install yesod yesod-bin persistent-sqlite yesod-
static  
  
CMD ["/opt/ghc/7.8.4/bin/ghci"]  

