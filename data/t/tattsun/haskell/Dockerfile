FROM ubuntu:latest  
  
MAINTAINER tattsun <t.t.mc1192.sf@gmail.com>  
  
# install tools  
RUN apt-get update && apt-get -y install gcc libgmp10 git wget zlib1g-dev  
  
# install haskell  
WORKDIR /  
RUN wget https://www.haskell.org/platform/download/2014.2.0.0/haskell-
platform-2014.2.0.0-unknown-linux-x86_64.tar.gz  
RUN tar xvf haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz  
RUN rm haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz  
RUN /usr/local/haskell/ghc-7.8.3-x86_64/bin/activate-hs  
  
# config tools  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgmp.so.10 /usr/lib/x86_64-linux-
gnu/libgmp.so  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# install source  
RUN cabal update && cabal install cabal-install --global  
  
# refresh container  
RUN apt-get clean  

