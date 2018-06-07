FROM ubuntu  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-xetex \  
texlive-fonts-recommended \  
texlive-lang-greek texlive-generic-extra texlive-latex-recommended \  
latex-xcolor \  
lmodern \  
fontconfig \  
make \  
mercurial \  
ca-certificates \  
wget \  
curl vile less gnupg \  
libgmp10  
  
RUN \  
cd /tmp && \  
wget
https://github.com/jgm/pandoc/releases/download/1.17.0.2/pandoc-1.17.0.2-1-amd64.deb
&& \  
dpkg -i pandoc-1.17.0.2-1-amd64.deb && rm -f pandoc-1.17.0.2-1-amd64.deb  

