## Dockerfile for a haskell environment  
FROM ubuntu:15.04  
MAINTAINER Vamshi Surabhi <vamshi@34cross.in>  
  
ENV GHC_VER 7.10.1  
ENV CABAL_VER 1.22  
ENV ALEX_VER 3.1.4  
ENV HAPPY_VER 1.19.5  
## ensure locale is set during build  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
RUN echo 'deb http://ppa.launchpad.net/hvr/ghc/ubuntu vivid main' >
/etc/apt/sources.list.d/ghc.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F6F88286 && \  
apt-get update && \  
apt-get install -y --no-install-recommends cabal-install-$CABAL_VER
ghc-$GHC_VER happy-$HAPPY_VER alex-$ALEX_VER \  
zlib1g-dev git libtinfo-dev libsqlite3-0 libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH
/root/.cabal/bin:/opt/cabal/$CABAL_VER/bin:/opt/ghc/$GHC_VER/bin:/opt/happy/$HAPPY_VER/bin:/opt/alex/$ALEX_VER/bin:.cabal-
sandbox/bin:$PATH  
  
RUN cabal update && cabal install scotty  
  
## run ghci by default unless a command is specified  
CMD ["ghci"]  

