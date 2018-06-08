FROM haskell  
MAINTAINER /u/dmp1ce  
  
# Install Yesod requriements  
# http://www.yesodweb.com/book/haskell  
RUN apt-get update -yq && \  
apt-get install -yq g++ gcc libc6-dev libffi-dev libgmp-dev make xz-utils
zlib1g-dev git gnupg && \  
stack build --install-ghc yesod persistent-sqlite yesod-static esqueleto  

