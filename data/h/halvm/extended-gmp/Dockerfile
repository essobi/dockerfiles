FROM halvm/base-gmp:fedora22  
  
RUN halvm-cabal update && \  
halvm-cabal install cryptonite && \  
halvm-cabal install hans && \  
halvm-cabal install tls -f-network -fhans  
  
RUN git clone https://github.com/GaloisInc/network-hans && \  
(cd network-hans && halvm-cabal install) && \  
rm -rf network-hans  
  
RUN git clone http://github.com/acw/HTTP && \  
(cd HTTP && halvm-cabal install) && \  
rm -rf HTTP  
  

