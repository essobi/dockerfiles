FROM haskell:7.8  
MAINTAINER Rodolphe Belouin <rodolphe.belouin@gmail.com>  
  
# We need lilypond for generating music scores  
RUN apt-get update && apt-get install -y --no-install-recommends lilypond  
  
# Update the cabal local repository  
RUN cabal update  
  
# Install music-suite  
RUN cabal install 'music-suite >=1.9 && <1.10'  
  
# Import Music.Prelude at start in GHCI  
RUN echo ':m +Music.Prelude' >> ~/.ghci  
  
WORKDIR /root  
  
CMD "ghci"  

