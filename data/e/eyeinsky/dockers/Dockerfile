FROM eyeinsky/dockers:haskell-stack-base  
  
RUN apt-get install -y libssl-dev cabal-install && \  
apt-get clean  
  
ADD app.cabal /app/app.cabal  
WORKDIR /app  
  
RUN stack setup  
RUN stack build  

