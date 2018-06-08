FROM haskell:8.0  
  
MAINTAINER Lukas Kallies  
  
RUN useradd -r -m pandoc  
  
# install latex packages  
RUN apt-get update -y \  
&& apt-get install -y -o Acquire::Retries=10 --no-install-recommends \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
texlive-lang-german \  
fontconfig \  
unzip \  
lmodern  
  
USER pandoc  
  
# will ease up the update process  
# updating this env variable will trigger the automatic build of the Docker
image  
ENV PANDOC_VERSION "1.19.2.1"  
ENV PATH "/home/pandoc/.cabal/bin:${PATH}"  
# install pandoc  
RUN cabal update && cabal install pandoc-${PANDOC_VERSION}  
  
WORKDIR /source  
  
CMD ["pandoc","--help"]  

