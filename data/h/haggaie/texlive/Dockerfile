FROM debian:jessie  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-
recommends install \  
biber \  
lmodern \  
texlive-bibtex-extra \  
texlive-latex-recommended \  
texlive-font-utils \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-latex-extra \  
texlive-lang-arabic \  
texlive-generic-recommended \  
texlive-publishers \  
texlive-science \  
texlive-xetex \  
ghostscript \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /document  

