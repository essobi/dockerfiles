FROM gdoteof/ghc  
  
  
RUN apt-get update && apt-get install -y git zlib1g-dev libghc-unix-compat-dev  
  
ENV HOME /root  
  
WORKDIR /root  
  
RUN git clone https://github.com/snoyberg/keter.git  
  
RUN cd keter  
  
RUN cabal update  
  
WORKDIR /root/keter  
  
ENV LANG C.UTF-8  
RUN cabal install --only-dependencies .  
RUN cabal install .  
RUN cabal clean && cabal configure  
RUN cabal build  

