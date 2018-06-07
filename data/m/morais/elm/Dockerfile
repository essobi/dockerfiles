FROM haskell:7.10.2  
ENV ELM_VER=master  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
libtinfo-dev  
  
# Install NodeJS  
RUN apt-get update  
RUN apt-get install curl -y  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install nodejs -y  
  
# Install Elm  
ENV PATH /opt/Elm-Platform/$ELM_VER/.cabal-sandbox/bin:$PATH  
WORKDIR /opt  
RUN curl https://raw.githubusercontent.com/elm-lang/elm-
platform/b69d0206b10ebc8c6cbc8b4fbc7033b4cd3e5672/installers/BuildFromSource.hs
> BuildFromSource.hs  
RUN runhaskell BuildFromSource.hs $ELM_VER  

