FROM ubuntu:16.04  
  
MAINTAINER Osones <docker@osones.io>  
  
RUN apt update && apt install -y \  
pandoc \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-extra-utils \  
make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

