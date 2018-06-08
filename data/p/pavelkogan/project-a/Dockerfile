FROM pavelkogan/haskell78lts1  
  
RUN cabal update  
  
RUN apt-get install --yes --force-yes \  
libdevil-dev \  
libadns1-dev \  
libcrypto++-dev \  
libssl-dev  
  
ADD ./project.cabal /root/  
RUN cd /root/ && cabal install --dependencies-only  

