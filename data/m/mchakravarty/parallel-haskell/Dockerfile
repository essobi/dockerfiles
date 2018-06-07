# Docker image with Haskell libraries for parallel programming based on LTS
Haskell  
  
FROM mchakravarty/ghc-7.10.2:latest  
  
MAINTAINER Manuel M T Chakravarty <chak@justtesting.org>  
  
# For packages in LTS, we give no version number, as that is fixed by LTS.  
#ENV PKGS accelerate accelerate-io-0.15.1.0 \  
# There is no accelerate-io-0.15.1.0 yet  
ENV PKGS accelerate \  
linear-accelerate \  
monad-par monad-par-extras \  
parallel \  
repa repa-algorithms repa-io  
  
RUN cabal update \  
&& curl -LS http://www.stackage.org/snapshot/lts-3.8/cabal.config?global=true
>>/root/.cabal/config \  
&& cabal install $PKGS  

