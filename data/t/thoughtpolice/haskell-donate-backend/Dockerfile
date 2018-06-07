FROM ubuntu:16.04  
MAINTAINER Austin Seipp "aseipp@pobox.com"  
  
COPY *.cabal *.hs *.project /app/  
COPY stripe /app/stripe  
WORKDIR /app/  
  
RUN apt-get -y update && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:hvr/ghc -y && \  
apt-get -y update && \  
apt-get install -y ghc-7.10.3 cabal-install-head libgmp10 zlib1g zlib1g-dev
libssl1.0.0 libssl-dev ca-certificates && \  
/opt/cabal/head/bin/cabal update && \  
/opt/cabal/head/bin/cabal new-build && \  
cp dist-newstyle/build/x86_64-linux/ghc-7.10.3/haskell-
donate-0.0.0.0/c/donate/build/donate/donate /usr/bin/donate && \  
apt-get remove -y ghc-7.10.3 cabal-install-head zlib1g-dev libssl-dev
software-properties-common && \  
apt-get autoremove -y && \  
cd / && \  
rm -rf /root/.cabal /root/.ghc /app/ /var/lib/apt/lists/  
  
USER nobody  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/donate"]  

