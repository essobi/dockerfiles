FROM debian:jessie  
MAINTAINER Daan Porru <daan@porru.nl>  
  
# Update package list and install GHC and Cabal requirements.  
RUN apt-get -y update &&\  
apt-get -y install build-essential curl zlib1g-dev libgmp3-dev libedit2 wget  
  
# Install GHC 7.10.2, newer version of GHC comes with an incompatible version
of Base.  
RUN wget https://www.haskell.org/ghc/dist/7.10.2/ghc-7.10.2-x86_64-unknown-
linux-deb7.tar.bz2 &&\  
tar xvfj ghc-7.10.2-x86_64-unknown-linux-deb7.tar.bz2 &&\  
cd ghc-7.10.2 &&\  
./configure &&\  
make install &&\  
ghc --version &&\  
cd .. &&\  
rm -fr ghc-7.10.2-x86_64-unknown-linux-deb7.tar.bz2 ghc-7.10.2  
  
# Install app-specific requirements.  
RUN apt-get update -y &&\  
apt-get install -y git libtinfo-dev texlive-xetex darcs npm nodejs-legacy
libicu-dev  
  
# Install Bower and Gulp sytem wide.  
RUN npm install -g bower &&\  
npm install -g gulp  
  
# Add user ph.  
RUN groupadd -g 9000 ph &&\  
useradd -mg 9000 ph &&\  
chown ph:ph /home/ph &&\  
mkdir -p /hairy-tribble/TCache &&\  
chown -R ph:ph /hairy-tribble  
  
# Run the rest of the statements as user ph.  
USER ph  
  
# Install Cabal install 1.22.6.0  
RUN cd /home/ph &&\  
wget http://hackage.haskell.org/package/cabal-install-1.22.6.0/cabal-
install-1.22.6.0.tar.gz &&\  
tar xvfz cabal-install-1.22.6.0.tar.gz &&\  
cd cabal-install-1.22.6.0 && ./bootstrap.sh &&\  
cd .. &&\  
rm -fr cabal-install-1.22.6.0*  
  

