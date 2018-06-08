FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
## Installs  
# what about haskell-platform-doc and haskell-platform-prof  
# should we install cabal?  
RUN /var/garage/install haskell-platform  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GARAGE_PROVIDES ghc ghci runghc

