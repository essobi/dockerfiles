FROM haskell:7.10  
MAINTAINER Peter St. John <peter.stjohn@nrel.gov>  
  
# install pandoc filters, inkscape and other tools  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
texlive-extra-utils \  
inkscape \  
bibtool \  
latexmk \  
lmodern \  
&& cabal update && \  
cabal install pandoc-1.17.2 && \  
cabal install pandoc-citeproc-0.10.2.2 && \  
cabal install pandoc-crossref-0.2.3.0  
# Add pandoc to the image path  
ENV PATH root/.cabal/bin:$PATH  
  
ENTRYPOINT []  
CMD ["pandoc"]  

