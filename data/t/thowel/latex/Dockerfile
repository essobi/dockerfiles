FROM ubuntu:latest  
MAINTAINER Thomas Welzel <developer@thomaswelzel.de>  
ENV DEBIAN_FRONTEND noninteractive  
  
# update software repository  
RUN apt-get update -q  
  
# install latex  
RUN apt-get install -qy \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
texlive-extra-utils \  
texlive-science \  
texlive-lang-german  
  
# install some additional tools  
RUN apt-get install -qy make latexmk git  

