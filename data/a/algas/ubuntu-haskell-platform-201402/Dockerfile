FROM ubuntu:14.04  
MAINTAINER Masahiro Yamauchi  
  
USER root  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential libgmp-dev  
ADD https://www.haskell.org/platform/download/2014.2.0.0/haskell-
platform-2014.2.0.0-unknown-linux-x86_64.tar.gz /  
WORKDIR /  
RUN tar xvf haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz  
RUN /usr/local/haskell/ghc-7.8.3-x86_64/bin/activate-hs  
RUN rm /haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz  
  

