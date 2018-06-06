FROM haskell:7.10  
MAINTAINER Randy Stauner <randy@magnificent-tears.com>  
  
RUN mkdir -p /src  
WORKDIR /src  
  
# http://haste-lang.org/downloads/  
# The "cabal install" used to work, but dependencies (and/or haste-boot) now  
# fails, and it's an old version anyway, so use the pre-built package.  
ADD http://haste-lang.org/downloads/ghc-7.10/haste-compiler_0.5.5.1_amd64.deb
/tmp/haste.deb  
RUN dpkg -i /tmp/haste.deb  
  
# Default command for haskell is "ghci" which makes as much sense as anything.  

