FROM haskell:7.10  
# This is a copy-paste from https://github.com/jagregory/pandoc-
docker/blob/ee311915c42da9ac75b687fa971d9866044450b4/Dockerfile with some
tweaks  
MAINTAINER James Porter <james@jamesporter.me>  
  
ENV PANDOC_VERSION "1.14.0.4"  
# install pandoc  
RUN cabal update && cabal install pandoc-${PANDOC_VERSION}  
  
# install latex packages  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
fontconfig  
  
RUN apt-get install -y lmodern  
  
WORKDIR /source  
  
ENTRYPOINT ["/root/.cabal/bin/pandoc"]  
  
CMD ["--help"]  

