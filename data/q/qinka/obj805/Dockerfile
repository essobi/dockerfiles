FROM haskell:8.0.1  
MAINTAINER qinka  
ADD obj805-server /src  
RUN cd /src && cabal sandbox init  
RUN cabal update  
RUN cd /src && cabal install --only-dependencies  
RUN cd /src && cabal install .  
RUN cp /src/.cabal-sandbox/bin/* /usr/bin  
RUN rm -rf /src  
EXPOSE 3000

