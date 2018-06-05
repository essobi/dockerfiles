FROM haskell:7.10  
MAINTAINER James Gregory <james@jagregory.com>  
  
# will ease up the update process  
# updating this env variable will trigger the automatic build of the Docker
image  
ENV PANDOC_VERSION "1.17.2"  
# install pandoc  
RUN cabal update && cabal install pandoc-${PANDOC_VERSION}  
  
RUN cabal install pandoc-include  
  
# install latex packages  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
fontconfig \  
lmodern \  
python2.7 python-pip \  
inkscape  
  
RUN pip install pandocfilters  
  
ADD courier /usr/share/fonts/courier  
  
RUN fc-cache -fv  
  
WORKDIR /source  
  
ENTRYPOINT ["/root/.cabal/bin/pandoc"]  
  
CMD ["--help"]  

