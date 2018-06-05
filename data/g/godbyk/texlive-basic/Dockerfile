FROM ubuntu:16.04  
MAINTAINER Kevin M. Godby <kevin@godby.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && \  
apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" \--no-install-
recommends && \  
apt-get -q install -y -o Dpkg::Options::="--force-confnew" \--no-install-
recommends latexmk poppler-utils texlive-binaries texlive-fonts-recommended
texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-
generic-recommended texlive-binaries xindy graphviz lmodern make && \  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
  

