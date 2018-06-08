FROM ubuntu:xenial  
  
MAINTAINER Rodrigo de Avila <rodrigo@avila.net.br>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
PATH=$PATH:~/.cabal/bin  
  
# Ubuntu default repo don't have an updated version of ShellCheck.  
# So, let's install cabal first, and shellcheck using cabal.  
RUN apt-get -qq update && \  
apt-get install -y -qq cabal-install && \  
apt-get -qq clean && \  
cabal update && \  
cabal install shellcheck && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/* ~/.cabal/lib ~/.ghc
~/.cabal/packages/* /core  

