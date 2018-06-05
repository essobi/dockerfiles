FROM haskell:7.8  
  
MAINTAINER Ryoma Kawajiri <ryoma.edison@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
graphviz \  
&& rm -rf /var/lib/apt/lists/* \  
&& cabal update \  
&& cabal install erd \  
&& rm -rf ~/.cabal/packages ~/.cabal/logs  
  
RUN mkdir /work  
WORKDIR /work  

