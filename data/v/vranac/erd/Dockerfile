FROM haskell:8.2  
LABEL maintainer Srdjan Vranac <vranac@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y graphviz \  
&& rm -f /var/cache/apt/archives/*.deb \  
&& rm -f /var/cache/apt/archives/partial/*.deb \  
&& rm -f /var/cache/apt/*.bin \  
&& cabal update \  
&& cabal install 'graphviz ==2999.*' 'parsec ==3.1.*' erd --allow-newer  
  
WORKDIR /erd  
  
ENTRYPOINT ["erd"]  
CMD ["-h"]

