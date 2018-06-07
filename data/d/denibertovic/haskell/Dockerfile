# Haskell  
#  
# VERSION 0.0.1  
FROM debian:wheezy  
MAINTAINER Deni Bertovic "me@denibertovic.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install build-essential libgmp-dev wget bzip2 ca-certificates
zlib1g-dev  
  
RUN wget -q http://www.haskell.org/ghc/dist/7.8.3/ghc-7.8.3-x86_64-unknown-
linux-deb7.tar.bz2 -O /tmp/ghc.tar.bz2  
RUN cd /tmp && bunzip2 /tmp/ghc.tar.bz2 && tar xvf /tmp/ghc.tar  
RUN cd /tmp/ghc-7.8.3 && ./configure --prefix="/root/.ghc" && make install  
  
ENV PATH "$PATH:/root/.ghc/bin:/root/.cabal/bin:/root/.cabal-sandbox/bin"  
ENV EXTRA_CONFIGURE_OPT -p  
  
RUN wget -q http://hackage.haskell.org/package/cabal-install-1.20.0.3/cabal-
install-1.20.0.3.tar.gz -O /tmp/cabal.tar.gz  
  
RUN cd /tmp && tar zxvf /tmp/cabal.tar.gz  
RUN cd /tmp/cabal-install-1.20.0.3 && ./bootstrap.sh  
  
RUN rm -rf /tmp/cabal* && rm -rf /tmp/ghc*  
  
ADD files/ghci /root/.ghci  
RUN chown root. /root/.ghci  
  
CMD ["/bin/bash"]  
  

