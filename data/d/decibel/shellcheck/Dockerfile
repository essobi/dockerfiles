FROM ubuntu:14.04  
MAINTAINER Mike Christof <mhristof@gmail.com>  
  
RUN apt-get update && apt-get install -y software-properties-common cabal-
install  
RUN cabal update && cabal install shellcheck && ln -s ~/.cabal/bin/shellcheck
/bin/shellcheck  

