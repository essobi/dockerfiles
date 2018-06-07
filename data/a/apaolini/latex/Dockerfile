# BUILD: docker build -t apaolini/latex .  
# RUN: docker run --rm -ti --user="$(id -u):$(id -g)" -v $(pwd):/data
apaolini/latex <COMMAND>  
  
FROM debian:stable  
MAINTAINER Andrea Paolini <ap@nuxi.it>  
  
RUN apt-get update \  
&& apt-get -y install texlive-latex-base \  
texlive-latex-extra \  
texlive-lang-italian \  
texlive-lang-english \  
texlive-lang-french \  
texlive-lang-german \  
texlive-lang-portuguese \  
texlive-lang-spanish \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
VOLUME ["/data"]  

