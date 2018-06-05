# Docker image mirroring GHC.framework for Linux  
# FIXME: Dockerfile doesn't support variable expansion in FROM and RUN
commands; hence, we have GHC version  
# hardcoded. Should maybe pre-process a Dockerfile template...  
FROM haskell:8.0.2  
  
LABEL maintainer "Manuel M T Chakravarty <chak@applicative.co>"  
ADD extra-packages /opt/  
ADD container-cabal.config /root/.cabal/config  
  
RUN cabal update \  
&& cabal install --global `grep -v language-c-inline /opt/extra-packages` \  
&& rm -rf /root/.cabal/packages /root/.cabal/logs  

