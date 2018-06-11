FROM debian:latest  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN apt-get update \  
&& apt-get --no-install-recommends -y install \  
cabal-install ghc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# http://hub.darcs.net/michal.palka/tf-random/issue/7  
ENV LANG=C.UTF-8  
RUN cabal update \  
&& cabal install --global shellcheck  
  
ENTRYPOINT ["shellcheck"]  
CMD ["-h"]  
  

