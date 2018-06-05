FROM haskell  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN groupadd --gid 1000 ghc \  
&& useradd --uid 1000 --gid ghc --shell /bin/bash --create-home ghc \  
&& chown -R ghc:ghc /usr/local  
  
USER ghc  
WORKDIR /home/ghc  
  
ENTRYPOINT ["/bin/bash"]  

