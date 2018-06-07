FROM debian:wheezy  
  
MAINTAINER alexander@hotwirestudios.com  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /root  
WORKDIR /root  
  
RUN apt-get -qq update && apt-get -qqy install build-essential curl zlib1g-dev
libgmp3-dev libedit2  
  
RUN curl -OL
https://downloads.haskell.org/~ghc/7.10.1/ghc-7.10.1-x86_64-unknown-linux-
deb7.tar.bz2  
RUN tar xjf ghc-7.10.1-x86_64-unknown-linux-deb7.tar.bz2  
RUN cd ghc-7.10.1 && ./configure  
RUN cd ghc-7.10.1 && make install  
RUN ghc --version  
  
RUN curl -OL http://hackage.haskell.org/package/cabal-install-1.22.4.0/cabal-
install-1.22.4.0.tar.gz  
RUN tar xzf cabal-install-1.22.4.0.tar.gz  
RUN (cd cabal-install-1.22.4.0 && ./bootstrap.sh)  
ENV PATH /root/.cabal/bin:$PATH  
ENV LANG C.UTF-8  
RUN rm -fr ghc-7.10.1-x86_64-unknown-linux-deb7.tar.bz2 ghc-7.10.1  
RUN rm -fr cabal-install-1.22.4.0*  
  
#RUN cabal update  
#RUN sed -i 's/remote-repo:.*/remote-repo:
stackage-e36ddac9333f2197ada6883b52f4834ddc0d5e37:http:\/\/www.stackage.org\/stackage\/e36ddac9333f2197ada6883b52f4834ddc0d5e37/'
/root/.cabal/config  
ENV __cabal_update_timestamp 201507101523  
RUN cabal update  

