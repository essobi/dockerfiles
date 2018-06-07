FROM ubuntu:14.04  
MAINTAINER Piyush P Kurur <ppk@cse.iitk.ac.in>  
  
# Versions of some haskell packages to pre-install  
# GHC Versions to install  
ENV GHCVER "head 8.0.2 8.0.1 7.10.3 7.8.4 7.6.3"  
# cabal-install version  
ENV CABALVER "1.24 1.22 1.20"  
RUN sudo apt-get update -y  
RUN sudo apt-get install software-properties-common -y  
  
# Generate the locales.  
RUN sudo locale-gen en_US en_US.UTF-8  
RUN sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
  
# We enable the repository of hvr so that we can access any of the  
# many versions of ghc that he provides. See  
# https://github.com/hvr/multi-ghc-travis  
RUN sudo add-apt-repository -y ppa:hvr/ghc  
RUN sudo add-apt-repository -y ppa:hvr/z3  
  
# We enable the fpcomplete repository for haskell stack.  
# The appropriate version of stack as described in  
# https://docs.haskellstack.org/en/stable/install_and_upgrade/#ubuntu  
# Add keys of fpcomplete.  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 575159689BEFB442  
  
# Add their repository to the source list.  
RUN echo 'deb http://download.fpcomplete.com/ubuntu trusty main' \  
| sudo tee /etc/apt/sources.list.d/fpco.list  
  
# Update apt- packages.  
RUN sudo apt-get update -y  
  
# Install some basic packages that are required by the haskell  
# environment.  
RUN sudo apt-get install curl wget hlint tar gzip -y  
  
# Installing the z3 sat solver.  
RUN sudo apt-get install z3 -y  
  
# Installing versions of ghc  
RUN for ver in `echo $GHCVER | tr " " "\n"`; do sudo apt-get install
"ghc-$ver" -y; done  
  
# Installing versions of cabal install  
RUN for ver in `echo $CABALVER | tr " " "\n"`; do sudo apt-get install "cabal-
install-$ver" -y; done  
  
# Install haskell stack.  
RUN sudo apt-get install stack -y  

